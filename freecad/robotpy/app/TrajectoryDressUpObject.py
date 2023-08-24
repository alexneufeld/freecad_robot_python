from FreeCAD import Console, Placement

ContTypeEnums = ["DontChange","Continues","Discontinues",]
AddTypeEnums = ["DontChange","UseOrientation","AddPosition","AddOrintation","AddPositionAndOrientation",]


class TrajectoryDressUpObject:
    def __init__(self, obj) -> None:
        obj.Proxy = self
        obj.addProperty("App::PropertyLink", "Source", "TrajectoryDressUp", "Trajectory to dress up").Source = None
        obj.addProperty("App::PropertySpeed", "Speed", "TrajectoryDressUp", "Speed to use").Speed = 1000
        obj.addProperty("App::PropertyBool", "UseSpeed", "TrajectoryDressUp","Switch the speed usage on").UseSpeed = False
        obj.addProperty("App::PropertyAcceleration", "Acceleration", "TrajectoryDressUp","Acceleration to use").Acceleration = 1000
        obj.addProperty("App::PropertyBool", "UseAcceleration", "TrajectoryDressUp","Switch the acceleration usage on").UseAcceleration = False
        obj.addProperty("App::PropertyEnumeration", "ContType", "TrajectoryDressUp", "Define the dress up of continuity").ContType = ContTypeEnums
        obj.addProperty("App::PropertyPlacement", "PosAdd", "TrajectoryDressUp","Position & Orientation to use").PosAdd = Placement()
        obj.addProperty("App::PropertyEnumeration", "AddType", "TrajectoryDressUp","How to change the Position & Orientation").AddType = AddTypeEnums
    
    def execute(self, fp):
        pass
    
    
