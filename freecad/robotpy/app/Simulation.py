from .Robot6Axis import Robot6Axis
from .Trajectory import Trajectory
import FreeCAD


class Simulation:
    def __init__(self, Trac: Trajectory, Rob: Robot6Axis.Robot6Axis) -> None:
        self.Trac = Trac
        self.Rob = Rob
        self.Tool = FreeCAD.Placement()
        self.Pos = 0.0
        self.Axis = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.startAxis = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        # simulating a trajectory with only one waypoint makes no sense!
        assert(self.Trac.getSize() > 1)
        self.startAxis[0] = Rob.getAxis(0)
        self.startAxis[1] = Rob.getAxis(1)
        self.startAxis[2] = Rob.getAxis(2)
        self.startAxis[3] = Rob.getAxis(3)
        self.startAxis[4] = Rob.getAxis(4)
        self.startAxis[5] = Rob.getAxis(5)
        self.setToTime(0)
    
    def getLength(self) -> float:
        return self.Trac.getLength()
    
    def getDuration(self) -> float:
        return self.Trac.getDuration()
    
    def getPosition(self) -> FreeCAD.Placement:
        return self.Trac.getPosition(self.Pos)
    
    def getVelocity(self) -> float:
        return self.Trac.getVelocity(self.Pos)
    
    def step(self, tick: float) -> None:
        self.Pos += tick
    
    def setToWaypoint(n: int) -> None:
        pass  # NOTE: this was blank in the original c++ code!
    
    def setToTime(t: float) -> None:
        self.Pos = t
        NeededPos = self.Trac.getPosition(Pos)
        NeededPos =  NeededPos * self.Tool.inverse()
        self.Rob.setTo(NeededPos)
        self.Axis[0] = self.Rob.getAxis(0)
        self.Axis[1] = self.Rob.getAxis(1)
        self.Axis[2] = self.Rob.getAxis(2)
        self.Axis[3] = self.Rob.getAxis(3)
        self.Axis[4] = self.Rob.getAxis(4)
        self.Axis[5] = self.Rob.getAxis(5)
    
    def reset(self) -> None:
        # apply the start axis angles and set to time 0. 
        # Restores the exact start position.
        self.Rob.setAxis(0,self.startAxis[0])
        self.Rob.setAxis(1,self.startAxis[1])
        self.Rob.setAxis(2,self.startAxis[2])
        self.Rob.setAxis(3,self.startAxis[3])
        self.Rob.setAxis(4,self.startAxis[4])
        self.Rob.setAxis(5,self.startAxis[5])
        NeededPos = self.Trac.getPosition(0.0)
        NeededPos =  NeededPos * self.Tool.inverse()
        self.Rob.setTo(NeededPos)
        self.Axis[0] = self.Rob.getAxis(0)
        self.Axis[1] = self.Rob.getAxis(1)
        self.Axis[2] = self.Rob.getAxis(2)
        self.Axis[3] = self.Rob.getAxis(3)
        self.Axis[4] = self.Rob.getAxis(4)
        self.Axis[5] = self.Rob.getAxis(5)
