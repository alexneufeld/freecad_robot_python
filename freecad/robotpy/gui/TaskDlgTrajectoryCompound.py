from os import path
import FreeCADGui
import FreeCAD
from PySide import QtGui
from freecad.robotpy import ICONPATH, UIPATH


class TaskDlgTrajectoryCompound:
    def __init__(self):
        # import GUI from .ui file
        loader = Gui.UiLoader()
        self.form = loader.load(
            path.join(
                os.path.dirname(__file__), "TaskTrajectoryCompmoundParameter.ui"
            )  # TODO: make this actually work!
        )
        self.setupUI()

    def setupUI(self):
        # use the feature's icon for the task panel
        """self.form.setWindowIcon(QtGui.QIcon(os.path.join(ICONPATH, "arb8.svg")))
        self.form.setWindowTitle("Arb8 Parameters")
        # focus keyboard input to the first editable value
        self.form.P1x.setFocus()
        self.form.P1x.selectAll()"""
        pass

    def getStandardButtons(self):
        return int(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)

    def accept(self):
        FreeCAD.ActiveDocument.recompute()
        Gui.ActiveDocument.resetEdit()
        return True

    def reject(self):
        FreeCAD.ActiveDocument.recompute()
        Gui.ActiveDocument.resetEdit()
        return True
