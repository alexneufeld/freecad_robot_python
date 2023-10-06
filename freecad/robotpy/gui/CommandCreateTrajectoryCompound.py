from os import path
import FreeCADGui
from .data_paths import ICONPATH
from ..app import TrajectoryCompoundObject
from .ViewProviderTrajectoryCompound import ViewProviderTrajectoryCompound


class CmdCreateTrajectoryCompound:
    def __init__(self) -> None:
        pass

    def IsActive(self):
        return FreeCADGui.ActiveDocument is not None

    def Activated(self):
        doc = FreeCADGui.ActiveDocument
        trc = doc.addObject("Part::FeaturePython", "TrajectoryCompound")
        TrajectoryCompoundObject(trc)
        ViewProviderTrajectoryCompound(trc.ViewObject)

    def GetResources(self):
        return {
            "Pixmap": path.join(ICONPATH, "Robot_TrajectoryCompound.svg"),
            "MenuText": "Group and connect some trajectories to one",
            "ToolTip": "Group and connect some trajectories to one",
        }
