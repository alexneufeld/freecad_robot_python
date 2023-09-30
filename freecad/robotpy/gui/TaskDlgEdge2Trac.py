import FreeCADGui
from freecad.robotpy import ICONPATH, UIPATH
import os
from PySide import QtGui


class TaskDlgEdge2Trac:
    def __init__(self, obj) -> None:
        self._obj = obj
        loader = FreeCADGui.UiLoader()
        self.form = loader.load(os.path.join(UIPATH, "TaskEdge2TracParameter.ui"))
        self.setupUI()

    def setupUI(self) -> None:
        # use the feature's icon for the task panel
        self.form.setWindowIcon(
            QtGui.QIcon(os.path.join(ICONPATH, "Robot_Edge2Trac.svg"))
        )
        self.form.setWindowTitle("Edge2Trac Parameters")
        # focus keyboard input to the first editable value
        self.form.lineEdit_ObjectName.setFocus()
        self.form.lineEdit_ObjectName.selectAll()

    def accept(self) -> bool:
        # TODO
        return True

    def reject(self) -> bool:
        # TODO
        return True

    def getStandardButtons(self) -> int:
        return int(
            QtGui.QDialogButtonBox.Ok
            | QtGui.QDialogButtonBox.Apply
            | QtGui.QDialogButtonBox.Cancel
        )
