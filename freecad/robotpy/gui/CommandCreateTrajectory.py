from os import path
import FreeCADGui
from freecad.robotpy import ICONPATH
from ..app import TrajectoryObject
from .ViewProviderTrajectory import ViewProviderTrajectory


class CmdCreateTrajectory:
    def __init__(self) -> None:
        pass

    def IsActive(self):
        return FreeCADGui.ActiveDocument is not None

    def Activated(self):
        doc = FreeCADGui.ActiveDocument
        tr = doc.addObject("Part::FeaturePython", "Trajectory")
        TrajectoryObject(tr)
        ViewProviderTrajectory(tr.ViewObject)

    def GetResources(self):
        return {
            "Pixmap": path.join(ICONPATH, "Robot_CreateTrajectory.svg"),
            "MenuText": "Create a new empty trajectory",
            "ToolTip": "Create a new empty trajectory",
        }
