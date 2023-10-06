from os import path
import FreeCADGui
from .data_paths import ICONPATH


class CmdRobotSetHomePos:
    def __init__(self) -> None:
        pass

    def IsActive(self):
        return FreeCADGui.ActiveDocument is not None

    def Activated(self):
        pass

    def GetResources(self):
        return {
            "Pixmap": path.join(ICONPATH, "Robot_SetHomePos.svg"),
            "MenuText": "Set the home position",
            "ToolTip": "Set the home position",
        }
