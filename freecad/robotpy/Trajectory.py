from FreeCAD import Placement, Vector
from math import pi
from .Waypoint import WaypointType, Waypoint


class trajectory:
    def __init__(self, tr: trajectory = None) -> None:
        self._waypoints = []
        self._trajectory = None
        if tr:
            self._waypoints = tr._waypoints

    def generateTrajectory(self) -> None:
        if self._waypoints == []:
            return
        # delete the old trajectory
        self._trajectory = None
    
    def addWaypoint(self, pnt: Waypoint) -> None:
        self._waypoints.append(pnt)
    
    def getSize(self) -> int:
        return len(self._waypoints)
    
    def getWaypoint(self, pos: int) -> Waypoint:
        """get the nth waypoint"""
        return self._waypoints[pos]
    
    def getUniqueWaypointName(self, name: str) -> str:
        raise NotImplementedError("Do we actually need this for anything?")
    
    def getWaypoints(self) -> list[Waypoint]:
        """Get the full list of waypoints in this trajectory"""
        return self._waypoints

    def deletelast(n: int) -> None:
        """delete the last n waypoints"""
        self._waypoints = self._waypoints[:-1*n]
    
    def getLength(self, n: int) -> float:
        """return the Length (mm) of the Trajectory if -1 or of the Waypoint with the given number"""
        raise NotImplementedError("Nope!")

    def getDuration(n: int) -> float:
        """return the duration (s) of the Trajectory if -1 or of the Waypoint with the given number"""
        raise NotImplementedError("Nope!")

    def getPosition(time: float) -> Placement:
        if tr := self.generateTrajectory():
            return None  # FIXME pos2placement(tr.Pos(time))
        else:
            return None

    def getVelocity(time: float) -> Placement:
        if tr := self.generated_trajectory:
            vec = tr.Vel(time).vel
            return FreeCAD.Vector(*vec).Length
        else:
            return 0