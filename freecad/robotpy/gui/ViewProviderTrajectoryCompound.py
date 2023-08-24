from freecad.robotpy import ICONPATH
from os import path
from .TaskDlgTrajectoryCompound import TaskDlgTrajectoryCompound 

class ViewProviderTrajectoryDressUp:
    def __init__(self, vobj):
        self.Object = vobj.Object
        vobj.Proxy = self

    def getIcon(self):
        return path.join(ICONPATH, "Robot_TrajectoryCompound.svg")
    
    def claimChildren(self):
        return self.Object.Source
        
    def setEdit(self,vobj,mode):
        taskd = TaskDlgTrajectoryCompound()
        FreeCADGui.Control.showDialog(taskd)
        return True

    def unsetEdit(self,vobj,mode):
        FreeCADGui.Control.closeDialog()
        return False