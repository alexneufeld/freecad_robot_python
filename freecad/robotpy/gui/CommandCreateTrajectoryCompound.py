from os import path
import FreeCADGui
from freecad.robotpy import ICONPATH
from freecad.robotpy import TrajectoryCompound
from freecad.robotpy.gui import ViewProviderTrajectoryCompound


class CmdCreateTrajectoryCompund:
    def __init__(self) -> None:
        pass
    
    def IsActive(self):
        if FreeCAD.ActiveDocument is None:
            return False
        else:
            return True
        
    def Activated(self):
        doc = FreeCADGui.ActiveDocument
        trc = doc.addObject("Part::FeaturePython", "TrajectoryCompound")
        TrajectoryCompound(trc)
        ViewProviderTrajectoryCompound(trc.ViewObject)
    
    def GetResources(self):
        return {'Pixmap': path.join(ICONPATH, "Robot_TrajectoryCompound.svg"),
                'MenuText': "Group and connect some trajectories to one",
                'ToolTip': "Group and connect some trajectories to one"}