from FreeCAD import Placement


class TrajectoryObject:
    def __init__(self, obj):
        obj.Proxy = self
        obj.addProperty(
            "App::PropertyPlacement",
            "Base",
            "Trajectory",
            "Base frame of the trajectory",
        ).Base = Placement()
        obj.addProperty(
            "App::PropertyPythonObject", "Trajectory", "Trajectory", "Trajectory object"
        ).Trajectory = None

    def mustExecute(self):
        return 0

    def execute(self, fp):
        pass
