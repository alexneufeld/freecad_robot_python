from FreeCAD import Console
from Part import Feature as PartFeature
from freecad.robotpy import edgecluster, trajectory
from freecad.robotpy import TrajectoryObject


class Edge2TracObject(TrajectoryObject):
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
        # TODO: error if someting other than an edge is selected
        edges = fp.Source[1]
        if not edges:  # no subshapes selected
            Console.PrintError("No Edges specified")
            return
        clustered_edges = edgecluster(edges)  # sort and cluster edges
        for cluster in clustered_edges:
            for e in cluster:
                match type(e):
                    case "Part::Line":
                        pass
                    case "Part::ArcOfCircle":
                        pass
                    case "Part::BSplineCurve":
                        pass
                    case _:
                        Console.PrintError("Unknown Edge type")
                        return
