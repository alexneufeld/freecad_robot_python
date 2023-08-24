from os import path
import FreeCADGui
from freecad.robotpy import ICONPATH
from freecad.robotpy import TrajectoryDressUp
from freecad.robotpy.gui import ViewProviderTrajectoryDressUp


class CmdCreateTrajectory:
    def __init__(self) -> None:
        pass

    def IsActive(self):
        if FreeCAD.ActiveDocument is None:
            return False
        else:
            return True

    def Activated(self):
        doc = FreeCADGui.ActiveDocument
        trd = doc.addObject("Part::FeaturePython", "TrajectoryDressUp")
        Trajectory(trd)
        ViewProviderTrajectory(trd.ViewObject)

    def GetResources(self):
        return {
            "Pixmap": path.join(ICONPATH, "Robot_CreateTrajectory.svg"),
            "MenuText": "Create a dress-up object which overrides some aspects of a trajectory",
            "ToolTip": "Create a dress-up object which overrides some aspects of a trajectory",
        }
