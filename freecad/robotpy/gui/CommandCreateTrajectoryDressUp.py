from os import path
import FreeCADGui
from .data_paths import ICONPATH
from ..app import TrajectoryDressUpObject
from .ViewProviderTrajectoryDressUp import ViewProviderTrajectoryDressUp


class CmdCreateTrajectoryDressUp:
    def __init__(self) -> None:
        pass

    def IsActive(self):
        return FreeCADGui.ActiveDocument is not None

    def Activated(self):
        doc = FreeCADGui.ActiveDocument
        trd = doc.addObject("Part::FeaturePython", "TrajectoryDressUp")
        TrajectoryDressUpObject(trd)
        ViewProviderTrajectoryDressUp(trd.ViewObject)

    def GetResources(self):
        return {
            "Pixmap": path.join(ICONPATH, "Robot_CreateTrajectory.svg"),
            "MenuText": "Create a dress-up object which "
            "overrides some aspects of a trajectory",
            "ToolTip": "Create a dress-up object which "
            "overrides some aspects of a trajectory",
        }
