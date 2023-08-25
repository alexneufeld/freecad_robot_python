from os import path
import FreeCADGui
from freecad.robotpy import ICONPATH


class CmdRobotRestoreHomePos:
    def __init__(self) -> None:
        pass

    def IsActive(self):
        return FreeCADGui.ActiveDocument is not None

    def Activated(self):
        pass

    def GetResources(self):
        return {
            "Pixmap": path.join(ICONPATH, "Robot_RestoreHomePos.svg"),
            "MenuText": "Move to home",
            "ToolTip": "Move to home",
        }
