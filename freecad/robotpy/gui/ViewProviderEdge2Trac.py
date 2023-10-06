from .data_paths import ICONPATH
from os import path
import FreeCADGui
from .TaskDlgEdge2Trac import TaskDlgEdge2Trac


class ViewProviderEdge2Trac:
    def __init__(self, vobj: FreeCADGui.ViewProvider) -> None:
        vobj.Proxy = self

    def getIcon(self) -> str:
        return path.join(ICONPATH, "Robot_Edge2Trac.svg")

    def setEdit(self, vobj: FreeCADGui.ViewProvider, mode: int) -> None:
        dlg = TaskDlgEdge2Trac(vobj.Object)
        FreeCADGui.Control.showDialog(dlg)
