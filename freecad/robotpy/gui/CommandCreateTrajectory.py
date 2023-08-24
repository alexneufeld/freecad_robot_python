from os import path
import FreeCADGui
from freecad.robotpy import ICONPATH
from freecad.robotpy import Trajectory
from freecad.robotpy.gui import ViewProviderTrajectory


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
        tr = doc.addObject("Part::FeaturePython", "Trajectory")
        Trajectory(tr)
        ViewProviderTrajectory(tr.ViewObject)

    def GetResources(self):
        return {
            "Pixmap": path.join(ICONPATH, "Robot_CreateTrajectory.svg"),
            "MenuText": "Create a new empty trajectory",
            "ToolTip": "Create a new empty trajectory",
        }
