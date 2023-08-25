from os import path
import FreeCADGui
from freecad.robotpy import ICONPATH


class CmdToolShape:
    def __init__(self) -> None:
        pass

    def IsActive(self):
        return FreeCADGui.ActiveDocument is not None

    def Activated(self):
        pass

    def GetResources(self):
        return {
            "Pixmap": path.join(ICONPATH, "Robot_CreateRobot.svg"),
            "MenuText": "Add a tool shape to the robot",
            "ToolTip": "Add a tool shape to the robot",
        }
