from os import path
import FreeCADGui
from .data_paths import ICONPATH


class CmdInsertwayPoint:
    def __init__(self) -> None:
        pass

    def IsActive(self):
        return FreeCADGui.ActiveDocument is not None

    def Activated(self):
        pass

    def GetResources(self):
        return {
            "Pixmap": path.join(ICONPATH, "Robot_InsertWaypoint.svg"),
            "MenuText": "Insert robot tool location into trajectory",
            "ToolTip": "Insert robot tool location into trajectory",
        }
