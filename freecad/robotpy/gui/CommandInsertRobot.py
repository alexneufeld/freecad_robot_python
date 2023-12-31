import FreeCAD
import FreeCADGui
from ..app import RobotObject
from .ViewProviderRobotObject import ViewProviderRobotObject
from .data_paths import ICONPATH, RESOURCEPATH
from os import path


class CmdRobotInsert:
    menutext = ""
    tooltip = ""
    iconpath = path.join(ICONPATH, "Robot_CreateRobot.svg")

    def __init__(self):
        pass

    def IsActive(self):
        return FreeCADGui.ActiveDocument is not None

    def Activated(self):
        doc = FreeCAD.ActiveDocument
        obj = doc.addObject("App::FeaturePython", "Robot")
        RobotObject(obj)
        ViewProviderRobotObject(obj.ViewObject)
        obj.RobotVrmlFile = path.join(RESOURCEPATH, "Kuka/kr500_1.wrl")
        obj.RobotKinematicFile = path.join(RESOURCEPATH, "Kuka/kr500_1.csv")
        obj.Axis2 = -90
        obj.Axis3 = 90
        obj.Axis5 = 45
        obj.Home = [0.0, -90.0, 90.0, 0.0, 45.0, 0.0]
        doc.recompute()

    def GetResources(self):
        return {
            "Pixmap": self.iconpath,
            "MenuText": self.menutext,
            "ToolTip": self.tooltip,
        }


class CmdRobotInsertKukaIR500(CmdRobotInsert):
    menutext = "Kuka IR500"
    tooltip = "Insert a Kuka IR500 into the document."

    def Activated(self):
        doc = FreeCAD.ActiveDocument
        obj = doc.addObject("App::FeaturePython", "Robot")
        RobotObject(obj)
        ViewProviderRobotObject(obj.ViewObject)
        obj.RobotVrmlFile = path.join(RESOURCEPATH, "Kuka/kr500_1.wrl")
        obj.RobotKinematicFile = path.join(RESOURCEPATH, "Kuka/kr500_1.csv")
        obj.Axis2 = -90
        obj.Axis3 = 90
        obj.Axis5 = 45
        obj.Home = [0.0, -90.0, 90.0, 0.0, 45.0, 0.0]
        doc.recompute()


class CmdRobotInsertKukaIR16(CmdRobotInsert):
    menutext = "Kuka IR16"
    tooltip = "Insert a Kuka IR16 into the document."

    def Activated(self):
        doc = FreeCAD.ActiveDocument
        obj = doc.addObject("App::FeaturePython", "Robot")
        RobotObject(obj)
        ViewProviderRobotObject(obj.ViewObject)
        obj.RobotVrmlFile = path.join(RESOURCEPATH, "Kuka/kr16.wrl")
        obj.RobotKinematicFile = path.join(RESOURCEPATH, "Kuka/kr16.csv")
        obj.Axis2 = -90
        obj.Axis3 = 90
        obj.Axis5 = 45
        doc.recompute()


class CmdRobotInsertKukaIR210(CmdRobotInsert):
    menutext = "Kuka IR210"
    tooltip = "Insert a Kuka IR210 into the document."

    def Activated(self):
        doc = FreeCAD.ActiveDocument
        obj = doc.addObject("App::FeaturePython", "Robot")
        RobotObject(obj)
        ViewProviderRobotObject(obj.ViewObject)
        obj.RobotVrmlFile = path.join(RESOURCEPATH, "Kuka/kr210.WRL")
        obj.RobotKinematicFile = path.join(RESOURCEPATH, "Kuka/kr_210_2.csv")
        obj.Axis2 = -90
        obj.Axis3 = 90
        obj.Axis5 = 45
        doc.recompute()


class CmdRobotInsertKukaIR125(CmdRobotInsert):
    menutext = "Kuka IR125"
    tooltip = "Insert a Kuka IR125 into the document."

    def Activated(self):
        doc = FreeCAD.ActiveDocument
        obj = doc.addObject("App::FeaturePython", "Robot")
        RobotObject(obj)
        ViewProviderRobotObject(obj.ViewObject)
        obj.RobotVrmlFile = path.join(RESOURCEPATH, "Kuka/kr125_3.wrl")
        obj.RobotKinematicFile = path.join(RESOURCEPATH, "Kuka/kr_125.csv")
        obj.Axis2 = -90
        obj.Axis3 = 90
        obj.Axis5 = 45
        doc.recompute()
