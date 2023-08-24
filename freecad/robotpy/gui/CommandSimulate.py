from os import path
import FreeCADGui
from freecad.robotpy import ICONPATH


class CmdRobotSimulate:
    def __init__(self) -> None:
        pass
    
    def IsActive(self):
        if FreeCAD.ActiveDocument is None:
            return False
        else:
            return True
        
    def Activated(self):
        pass
    
    def GetResources(self):
        return {'Pixmap': path.join(ICONPATH, "Robot_Simulate.svg"),
                'MenuText': "Simulate a trajectory",
                'ToolTip': "Run a simulation on a trajectory"}