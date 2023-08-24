from os import path
import FreeCADGui
from freecad.robotpy import ICONPATH


class CmdRobotSetHomePos:
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
        return {'Pixmap': path.join(ICONPATH, "Robot_SetHomePos.svg"),
                'MenuText': "Set the home position",
                'ToolTip': "Set the home position"}