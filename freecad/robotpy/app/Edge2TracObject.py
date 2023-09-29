from FreeCAD import Console
from FreeCAD import Rotation
from FreeCAD import Placement
from Part import Feature as PartFeature
from Part import getSortedClusters
from .Trajectory import Trajectory
from .Waypoint import Waypoint


class Edge2TracObject():
    def __init__(obj, self) -> None:
        super().__init__(self, obj)
        obj.Proxy = self
        obj.addproperty(
            "App::PropertyLinkSub",
            "Source",
            "Edge2Trac",
            "Edges to generate the Trajectory",
        ).Source = None
        obj.addproperty(
            "App::PropertyFloatConstraint",
            "SegValue",
            "Edge2Trac",
            "Max deviation from original geometry",
        ).SegValue = 0.5
        obj.addproperty(
            "App::PropertyBool",
            "UseRotation",
            "Edge2Trac",
            "Use orientation of the edge",
        ).UseRotation = False
        self.NbrOfEdges = 0
        self.NbrOfCluster = 0

    def execute(self, fp):
        if not fp.Source:
            Console.PrintError("No object linked")
            return
        if not isinstance(fp.Source, PartFeature):
            Console.PrintError("Linked object is not a Part object")
            return
        # TODO: error if something other than an edge is selected
        edges = fp.Source[1]
        if not edges:  # no subshapes selected
            Console.PrintError("No Edges specified")
            return
        clustered_edges = getSortedClusters(edges)  # sort and cluster edges
        # set the number of cluster and edges
        # nbr_of_cluster = len(clustered_edges)
        # nbr_of_edge = sum([len(x) for x in clustered_edges])
        # trajectory to fill
        trac = Trajectory()
        # cycle through the cluster
        first = True
        for cluster in clustered_edges:
            # NOTE: this code currently completely ignores the 'UseRotation' property
            #  of the edges. This behaviour matches tha of the original c++ impl...
            for e in cluster:
                match e.Curve.TypeId:
                    case "Part::GeomLine":
                        p1 = e.firstVertex().Point
                        p2 = e.lastVertex().Point
                        r1 = Rotation()
                        r2 = Rotation()
                        if e.Orientation() == "Reversed":
                            p1, p2 = p2, p1
                            r1, r2 = r2, r1
                        if first:
                            trac.addWayPoint("Pt", Waypoint(Placement(p1, r1)))
                        trac.addWayPoint("Pt", Waypoint(Placement(p2, r2)))
                    case "Part::GeomCircle":
                        length = e.Length
                        parlength = e.LastParameter - e.FirstParameter
                        nbrsegments = round(length / fp.SegValue)
                        seglength = parlength / nbrsegments
                        if e.Orientation == "Reversed":
                            i = e.LastParameter
                            if first:
                                first = False
                            else:
                                i -= seglength
                            while i >= e.FirstParameter:
                                p1 = e.valueAt(i)
                                r1 = Rotation()
                                trac.addWayPoint("Pt", Waypoint(Placement(p1, r1)))
                                i -= seglength
                        else:
                            i = e.FirstParameter
                            if first:
                                first = False
                            else:
                                i += seglength
                            while i <= e.LastParameter:
                                p1 = e.valueAt(i)
                                r1 = Rotation()
                                trac.addWayPoint("Pt", Waypoint(Placement(p1, r1)))
                                i += seglength
                    case "Part::GeomBSplineCurve":
                        length = e.Length
                        parlength = e.LastParameter - e.FirstParameter
                        nbrsegments = round(length / fp.SegValue)
                        start = e.FirstParameter
                        end = e.LastParameter
                        stp = parlength / nbrsegments
                        is_reversed = False
                        if e.Orientation == "Reversed":
                            start, end = end, start
                            stp = -stp
                            is_reversed = True
                        if first:
                            first = False
                        else:
                            start += stp
                        if is_reversed:
                            while start >= stp:
                                p1 = e.valueAt(start)
                                r1 = Rotation()
                                trac.addWayPoint("Pt", Waypoint(Placement(p1, r1)))
                                start += stp
                        else:
                            while start <= stp:
                                p1 = e.valueAt(start)
                                r1 = Rotation()
                                trac.addWayPoint("Pt", Waypoint(Placement(p1, r1)))
                                start += stp
                    case _:
                        Console.PrintError("Unknown Edge type")
                        return
        fp.Trajectory = trac
