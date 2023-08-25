from os import path
import FreeCADGui
from freecad.robotpy import ICONPATH
from ..app import Edge2TracObject
from .ViewProviderEdge2Trac import ViewProviderEdge2Trac


class CmdCreateEdge2Trac:
    def __init__(self) -> None:
        pass

    def IsActive(self):
        return FreeCADGui.ActiveDocument is not None

    def Activated(self):
        doc = FreeCADGui.ActiveDocument
        tr = doc.addObject("Part::FeaturePython", "Edge2Trac")
        TrajectoryCompound(tr)
        ViewProviderTrajectoryCompound(tr.ViewObject)

    def GetResources(self):
        return {
            "Pixmap": path.join(ICONPATH, "Robot_Edge2Trac.svg"),
            "MenuText": "Generate a trajectory from a set of edges",
            "ToolTip": "Generate a trajectory from a set of edges",
        }
