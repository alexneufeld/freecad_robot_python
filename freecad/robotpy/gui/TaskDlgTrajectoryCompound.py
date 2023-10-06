import os
import FreeCADGui
import FreeCAD
from PySide import QtGui
from .data_paths import ICONPATH, UIPATH


class TaskDlgTrajectoryCompound:
    def __init__(self):
        # import GUI from .ui file
        loader = FreeCADGui.UiLoader()
        self.form = loader.load(
            os.path.join(UIPATH, "TaskTrajectoryCompmoundParameter.ui")
        )
        self.setupUI()

    def setupUI(self):
        # use the feature's icon for the task panel
        self.form.setWindowIcon(
            QtGui.QIcon(os.path.join(ICONPATH, "Robot_TrajectoryCompound.svg"))
        )
        self.form.setWindowTitle("Trajectory Compound Parameters")
        # focus keyboard input to the first editable value
        # self.form.some_widget.setFocus()
        # self.form.some_widget.selectAll()

    def getStandardButtons(self):
        return int(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)

    def accept(self):
        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.ActiveDocument.resetEdit()
        return True

    def reject(self):
        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.ActiveDocument.resetEdit()
        return True
