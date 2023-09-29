import Part
import FreeCAD
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
                if not toContinue: break
            # Store the current adjacent edges as a cluster
            self._m_final_cluster.push_back(self._m_edges)
            # and continue now with the still existing edges in the m_vertices
            if self._m_vertices == []:
                break
        self._m_done = True

    def PerformEdges(self, point):
        iter = next((key, value) for key, value in self.m_vertices.items() if key == point)
        if iter is None:
            return False
        edges = iter[1]
        edgeIt = iter[1].__iter__()
        if next(edgeIt, None) is None:
            del self.m_vertices[iter[0]]
            return False
        theEdge = next(edgeIt)
        edges.remove(theEdge)
        if len(edges) == 0:
            del self.m_vertices[iter[0]]
        V1, V2 = TopExp.Vertices(theEdge)
        P1 = BRep_Tool.Pnt(V1)
        P2 = BRep_Tool.Pnt(V2)
        if theEdge.Orientation() == TopAbs_REVERSED:
            tmpP = P1
            P1 = P2
            P2 = tmpP
        nextPoint = gp_Pnt()
        if P2.IsEqual(point, 0.2):
            theEdge.Reverse()
            nextPoint = P1
        else:
            nextPoint = P2
        iter = next((key, value) for key, value in self.m_vertices.items() if key == nextPoint)
        if iter is not None:
            nextEdges = iter[1]
            for edgeIt in nextEdges:
                if theEdge.IsSame(edgeIt):
                    nextEdges.remove(edgeIt)
                    break
        self.m_edges.append(theEdge)
        point = nextPoint
        return True







    def Perform():
        if len(m_unsortededges) == 0:
            return
        for aVectorIt in m_unsortededges:
            if IsValidEdge(aVectorIt):
                Perform(aVectorIt)
        
        while True:
            m_edges.clear()
            closed = True
            for iter in m_vertices:
                if len(m_vertices[iter]) == 1:
                    closed = False
                    break
            if closed:
                iter = next(iter(m_vertices))
            firstPoint = iter
            currentPoint = firstPoint
            toContinue = True
            while toContinue == True:
                toContinue = PerformEdges(currentPoint)
            m_final_cluster.append(m_edges)
            
            if len(m_vertices) == 0:
                break
        m_done = True


    def Perform_one_edge(self. edge: Part.Edge) -> None:
        if edge.isNull():  # should we also check that the edge is valid?
            return
        p1, p2 = [v.Point for v in edge.Vertexes]
        empty_list = []
        


    def Perform_one_edge(self, edge: Part.Edge) -> None:
        if edge.IsNull():
            return
        V1, V2 = TopExp.Vertices(edge)
        P1 = BRep_Tool.Pnt(V1)
        P2 = BRep_Tool.Pnt(V2)
        emptyList = []
        iter = self._m_vertices.insert((P1, emptyList))
        iter.first[1].append(edge)
        iter = self.m_vertices.insert((P2, emptyList))
        iter.first[1].append(edge)


    
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
