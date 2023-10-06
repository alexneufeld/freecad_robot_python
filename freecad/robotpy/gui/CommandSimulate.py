from os import path
import FreeCADGui
from .data_paths import ICONPATH


class CmdRobotSimulate:
    def __init__(self) -> None:
        pass

    def IsActive(self):
        return FreeCADGui.ActiveDocument is not None

    def Activated(self):
        pass

    def GetResources(self):
        return {
            "Pixmap": path.join(ICONPATH, "Robot_Simulate.svg"),
            "MenuText": "Simulate a trajectory",
            "ToolTip": "Run a simulation on a trajectory",
        }
