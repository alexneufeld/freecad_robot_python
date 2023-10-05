import FreeCAD
from .Robot6Axis import Robot6Axis


class RobotObject(Robot6Axis):
    def __init__(self, obj) -> None:
        obj.Proxy = self
        obj.addProperty(
            "App::PropertyFileIncluded",
            "RobotVrmlFile",
            "Robot definition",
            "Included file with the VRML representation of the robot",
        ).RobotVrmlFile = ""
        obj.addProperty(
            "App::PropertyFileIncluded",
            "RobotKinematicFile",
            "Robot definition",
            "Included file with kinematic definition of the robot Axis",
        ).RobotKinematicFile = ""
        obj.addProperty(
            "App::PropertyFloat",
            "Axis1",
            "Robot kinematic",
            "Axis 1 angle of the robot in degre",
        ).Axis1 = 0.0
        obj.addProperty(
            "App::PropertyFloat",
            "Axis2",
            "Robot kinematic",
            "Axis 1 angle of the robot in degre",
        ).Axis2 = 0.0
        obj.addProperty(
            "App::PropertyFloat",
            "Axis3",
            "Robot kinematic",
            "Axis 1 angle of the robot in degre",
        ).Axis3 = 0.0
        obj.addProperty(
            "App::PropertyFloat",
            "Axis4",
            "Robot kinematic",
            "Axis 1 angle of the robot in degre",
        ).Axis4 = 0.0
        obj.addProperty(
            "App::PropertyFloat",
            "Axis5",
            "Robot kinematic",
            "Axis 1 angle of the robot in degre",
        ).Axis5 = 0.0
        obj.addProperty(
            "App::PropertyFloat",
            "Axis6",
            "Robot kinematic",
            "Axis 1 angle of the robot in degre",
        ).Axis6 = 0.0
        # what does this do?
        obj.addProperty(
            "App::PropertyString",
            "Error",
            "Robot kinematic",
            "Robot error while moving",
        ).Error = ""
        obj.addProperty(
            "App::PropertyPlacement", "Tcp", "Robot kinematic", "Tcp of the robot"
        ).Tcp = FreeCAD.Placement()
        obj.addProperty(
            "App::PropertyPlacement",
            "Base",
            "Robot kinematic",
            "Actual base frame of the robot",
        ).Base = FreeCAD.Placement()
        obj.addProperty(
            "App::PropertyPlacement",
            "Tool",
            "Robot kinematic",
            "Tool frame of the robot (Tool)",
        ).Tool = FreeCAD.Placement()
        obj.addProperty(
            "App::PropertyLink",
            "ToolShape",
            "Robot definition",
            "Link to the Shape is used as Tool",
        ).ToolShape = None
        obj.addProperty(
            "App::PropertyPlacement",
            "ToolBase",
            "Robot definition",
            "Defines where to connect the ToolShape",
        ).ToolBase = FreeCAD.Placement()
        obj.addProperty(
            "App::PropertyFloatList", "Home", "Robot kinematic" "Axis position for home"
        ).Home = [
            0,
        ]

    def mustExecute(self, fp):
        return 0

    def execute(self, fp):
        pass

    def onChanged(self, fp, prop):
        pass
