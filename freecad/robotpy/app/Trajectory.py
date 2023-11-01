import FreeCAD
from .Waypoint import Waypoint
from .RobotAlgos import toPlacement
from .RobotAlgos import toFrame
from .Waypoint import WaypointType
from typing import Self
import PyKDL


class Trajectory:
    def __init__(self, tr: Self = None) -> None:
        self._waypoints = []
        self._trajectory = None
        if tr:
            self._waypoints = tr._waypoints

    def generateTrajectory(self) -> None:
        if self._waypoints == []:
            return
        # delete the old trajectory
        self._trajectory = None
        # create a new trajectory
        self._trajectory = PyKDL.Trajectory_Composite()
        round_comp = None
        try:
            first = True  # to special-case the 1st waypoint
            for wp in self._waypoints:
                if first:
                    last_frame = toFrame(wp.EndPos)
                    self._trajectory
                    first = False
                else:
                    match wp.Type:
                        case WaypointType.LINE | WaypointType.PTP:
                            # start of a continous block
                            next_frame = toFrame(wp.EndPos)
                            cont = wp.Cont and wp != self._waypoints[-1]
                            if cont and (round_comp is None):
                                round_comp = PyKDL.Path_RoundedComposite(
                                    3, 3, PyKDL.RotationalInterpolation_SingleAxis()
                                )
                                # vel_prf = PyKDL.VelocityProfile_Trap(
                                #     wp.Velocity, wp.Acceleration
                                # )
                                round_comp.Add(last_frame)
                                round_comp.Add(next_frame)
                            elif cont and (round_comp is not None):
                                # continue a continous block
                                round_comp.Add(next_frame)
                            elif not cont and (round_comp is not None):
                                # end of a continous block
                                round_comp.Add(next_frame)
                                round_comp.Finish()
                                # FIXME
                        case WaypointType.WAIT:
                            pass
                        case _:  # CIRC and UNDEF are handled here
                            pass
        except Exception as E:
            FreeCAD.Console.LogError(E)
            FreeCAD.Console.LogError("\n")
            return

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

    def deletelast(self, n: int) -> None:
        """delete the last n waypoints"""
        self._waypoints = self._waypoints[: -1 * n]

    def getLength(self, n: int) -> float:
        """return the Length (mm) of the Trajectory if -1 or of the Waypoint with
        the given number"""
        self.generateTrajectory()
        if self._trajectory:
            if n < 0:  # length of the entire trajectory
                return self._trajectory.getPath().pathLength()
            else:  # path lenth of the nth move
                return self._trajectory.Get(n).GetPath().PathLength()
        else:
            return 0

    def getDuration(self, n: int) -> float:
        """return the duration (s) of the Trajectory (if n=-1) or of the Waypoint
        with the given number"""
        self.generateTrajectory()
        if self._trajectory:
            if n < 0:  # return the duration of the entire trajectory
                return self._trajectory.Duration()
            else:  # return the duraion of the nth move
                return self._trajectory.Get(n).Duration()
        else:
            return 0

    def getPosition(self, time: float) -> FreeCAD.Placement | None:
        if tr := self.generateTrajectory():
            return toPlacement(tr.Pos(time))
        else:
            return None

    def getVelocity(self, time: float) -> float:
        if tr := self.generated_trajectory:
            vec = tr.Vel(time).vel
            return FreeCAD.Vector(*vec).Length
        else:
            return 0
