import PyKDL
import FreeCAD
import csv
import math
from dataclass import dataclass
from . import RobotAlgos
import csv
import os


@dataclass
class AxisDefinition
    a: float = 0.0  # a of the Denavit-Hartenberg parameters (mm)
    alpha: float = 0.0  # alpha of the Denavit-Hartenberg parameters (°)
    d: float = 0.0  # d of the Denavit-Hartenberg parameters (mm)
    theta: float = 0.0  # a of the Denavit-Hartenberg parameters (°)
    rotDir: float = 0.0  # rotational direction (1|-1)
    maxAngle: float = 0.0  # soft ends + in °
    minAngle: float = 0.0  # soft ends - in °
    velocity: float = 0.0  # max vlocity of the axle in °/s


KukaIR500 = [
    # (a    ,alpha ,d    ,theta ,rotDir ,maxAngle ,minAngle ,AxisVelocity 
    AxisDefinition(500  ,-90   ,1045 ,0     , -1    ,+185     ,-185     ,156         ), # Axis 1
    AxisDefinition(1300 ,0     ,0    ,0     , 1     ,+35      ,-155     ,156         ), # Axis 2
    AxisDefinition(55   ,+90   ,0    ,-90   , 1     ,+154     ,-130     ,156         ), # Axis 3
    AxisDefinition(0    ,-90   ,-1025,0     , 1     ,+350     ,-350     ,330         ), # Axis 4
    AxisDefinition(0    ,+90   ,0    ,0     , 1     ,+130     ,-130     ,330         ), # Axis 5
    AxisDefinition(0    ,+180  ,-300 ,0     , 1     ,+350     ,-350     ,615         )  # Axis 6
]

class Robot6Axis
    def __init__(self) -> None:
        self._Kinematic = PyKDL.Chain()
        self._Actual = PyKDL.JntArray(6)
        self._Min = PyKDL.JntArray(6)
        self._Max = PyKDL.JntArray(6)
        self._Tcp = PyKDL.Frame()
        self._Velocity = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self._RotDir = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.setKinematic(KukaIR500)
    
    def setKinematic(self, KinDef: list[AxisDefinition) -> None:
        temp = PyKDL.Chain()
        for i in range(6):
            temp.addSegment(
                PyKDL.Segment(
                    PyKDL.Joint(PyKDL.Joint.RotZ),
                    PyKDL.Frame.DH(KinDef[i].a, KinDef[i].alpha * (math.pi/180) ,KinDef[i].d ,KinDef[i].theta * (math.pi/180)))
            )
            self._RotDir  [i] = KinDef[i].rotDir
            self._Max(i) = KinDef[i].maxAngle * (math.pi/180)
            self._Min(i) = KinDef[i].minAngle * (math.pi/180)
            self._Velocity[i] = KinDef[i].velocity
        self._Kinematic = temp
        self.calcTcp()
    
    def readKinematic(self FileName: os.PathLike) -> None:
        with open(FileName, 'r') as f:
            reader = csv.reader(f, dialect="excel")
            # skip header
            next(reader)
            temp = [AxisDefinition(*row) for row in reader]
            self.setKinematic(temp)

    def setTo(self, To: FreeCAD.Placement) -> bool:
        fksolver1 = PyKDL.ChainFkSolverPos_recursive(self._Kinematic)  # Forward position solver
        iksolver1v = PyKDL.ChainIkSolverVel_pinv(self._Kinematic)  # Inverse velocity solver
        iksolver1 = ChainIkSolverPos_NR_JL(self._Kinematic,self._Min,self._Max,fksolver1,iksolver1v,100,1e-6)  # Maximum 100 iterations, stop at accuracy 1e-6
        # Creation of jntarrays:
        result = PyKDL.JntArray(self._Kinematic.getNrOfJoints())
        # Set destination frame
        F_dest = RobotAlgos.toFrame(To)
        # solve
        if (iksolver1.CartToJnt(self._Actual,F_dest,result) < 0):
            return false
        else:
            self._Actual = result;
            self._Tcp = F_dest;
            return true
    
    def setAxis(self, Axis: int, Value: float) ->bool:
        self._Actual[Axis] = self._RotDir
    
    def getAxis(self, Axis: int) -> float:
        return self._RotDir[Axis] * (self._Actual[Axis] / (math.pi / 180.0))
    
    def getMaxAngle(self, Axis: int) -> float:
        return self._Max[Axis] * 180.0 / math.pi
    
    def getMinAngle(self, Axis: float) -> float:
        return self._Min[Axis] * 180.0 / math.pi
    
    def calcTcp(self) -> bool:
        fksolver = PyKDL.ChainFkSolverPos_recursive(self._Kinematic)
        cartpos = PyKDL.Frame()
        kinematics_status = fksolver.JntToCart(self._Actual, self.cartpos)
        return (kinematics_status >= 0)
    
    def getTcp(self) -> FreeCAD.Placement:
        return RobotAlgos.toPlacement(self._Tcp)