from FreeCAD import Placement, Vector
from math import pi
from PyKDL import Waypoint
from freecad.robotpy.kdl2fc import vec2vec, pos2placement


class trajectory:
    def __init__(self) -> None:
        pass

    def getLength(n: int) -> float:
        pass

    def getDuration(n: int) -> float:
        pass

    def getPosition(time: float) -> Placement:
        if tr := self.generated_trajectory:
            return pos2placement(tr.Pos(time))
        else:
            return None

    def getVelocity(time: float) -> Placement:
        if tr := self.generated_trajectory:
            vec = tr.Vel(time).vel
            return vec2vec(vec).Length
        else:
            return 0

    @property
    def generated_trajectory(self) -> list:
        pass
