#!/usr/bin/python3
import tempfile
import FreeCADGui

x = 1920
y = 1080
Background = "White"

OutDir = tempfile.gettempdir()

def run(Robot, Trajectory):
    Tool = Robot.Tool
    Tool = Tool.inverse()
    # duration in seconds time the pictures per second gives the size
    size = int(Trajectory.Duration * 24.0)
    for x in range(size):
        Robot.Tcp = Trajectory.position(x / 24.0).multiply(Tool)
        FreeCADGui.updateGui()
        FreeCADGui.ActiveDocument.ActiveView.saveImage(
            OutDir + "Rob_" + x + ".jpg", x, y, "White"
        )


if __name__ == "__main__":
    # attempt to run using the currently selected items.
    # This assumes that a Robot object, then a trajectory were selected.
    run(FreeCADGui.Selection.getSelection())