import Part
from Typing import Self


class EdgeCluster:
    def __init__(self, unsorted_edges: list[Part.Edge]) -> None:
        self._m_unsorted_edges = unsorted_edges
        self._m_edges = []
        self._m_vertices = []
        self._m_final_cluster = []

    def GetClusters(self) -> Self:
        self._Perform()
        return self._m_final_cluster

    def _Perform(self, edge: Part.Edge = None) -> None:
        if self._m_unsorted_edges == []:
            return
        # adds all the vertices to a map, and store the associated edges
        for e in self._m_unsorted_edges:
            if self._IsValidEdge(e):
                self._Perform_edge(e)
        # now, iterate through the edges to sort and cluster them
        while True:
            self._m_edges = []
            # Lets start with a vertice that only has one edge
            # (that means start or end point of the merged edges!)
            closed = True
            myvar = None
            for x in self._m_vertices:
                myvar = x
                if len(x[1]) == 1:
                    closed = False
                    break
            if closed:
                myvar = self._m_vertices[0]
            firstPoint = myvar[0]
            currentPoint = firstPoint
            while True:
                toContinue = self._PerformEdges(currentPoint)
                if not toContinue:
                    break
            # Store the current adjacent edges as a cluster
            self._m_final_cluster.push_back(self._m_edges)
            # and continue now with the still existing edges in the m_vertices
            if self._m_vertices == []:
                break
        self._m_done = True

    def Perform_one_edge(self, edge: Part.Edge) -> None:
        if edge.isNull():  # should we also check that the edge is valid?
            return
        p1, p2 = [v.Point for v in edge.Vertexes]
        # empty_list = []

    def _PerformEdges(self, point: Part.Point) -> None:
        pass

    def _IsValidEdge(edge: Part.Edge) -> bool:
        if edge.isNull():
            return False
        # note that isValid may throw an exception on null edges
        if not edge.isValid():
            return False
        # check that the midpoint <-> endpoint and midpoint <-> startpoint distances
        # are greater than an epsilon value.
        # We don't check the startpoint <-> endpoint distance to avoid false
        # negatives on closed edges
        start = edge.firstVertex().Point
        mid = edge.valueAt(0.5 * sum(edge.ParameterRange))
        end = edge.lastVertex().Point
        eps = 1e-5
        if start.distanceToPoint(mid) <= eps:
            return False
        if end.distanceToPoint(mid) <= eps:
            return False
        return True
