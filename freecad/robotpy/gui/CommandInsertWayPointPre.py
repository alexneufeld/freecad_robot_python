from os import path
import FreeCADGui
from .data_paths import ICONPATH


class CmdInsertwayPointPre:
    def __init__(self) -> None:
        pass

    def IsActive(self):
        return FreeCADGui.ActiveDocument is not None

    def Activated(self):
        pass

    def GetResources(self):
        return {
            "Pixmap": path.join(ICONPATH, "Robot_InsertWaypointPre.svg"),
            "MenuText": "Insert preselection position into trajectory",
            "ToolTip": "Insert preselection position into trajectory",
        }
