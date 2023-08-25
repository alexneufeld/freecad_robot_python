import FreeCADGui
from freecad.robotpy import ICONPATH
from os import path


class RobotPyWorkbench(FreeCADGui.Workbench):
    MenuText = "Robot workbench (python version)"
    ToolTip = MenuText
    Icon = path.join(ICONPATH, "RobotWorkbenchPython.svg")

    def Initialize(self):
        from .gui import (
            CmdRobotInsert,
            CmdRobotInsertKukaIR500,
            CmdRobotInsertKukaIR16,
            CmdRobotInsertKukaIR210,
            CmdRobotInsertKukaIR125,
            CmdToolShape,
            CmdRobotSetHomePos,
            CmdRobotRestoreHomePos,
            CmdCreateTrajectory,
            CmdCreateTrajectoryDressUp,
            CmdCreateTrajectoryCompund,
            CmdCreateEdge2Trac,
            CmdRobotSimulate,
            CmdInsertwayPoint,
            CmdInsertwayPointPre,
        )

        FreeCADGui.addCommand("RobotPy_Create", CmdRobotInsert)
        FreeCADGui.addCommand("RobotPy_Robot_InsertKukaIR500", CmdRobotInsertKukaIR500)
        FreeCADGui.addCommand("RobotPy_Robot_InsertKukaIR16", CmdRobotInsertKukaIR16)
        FreeCADGui.addCommand("RobotPy_Robot_InsertKukaIR210", CmdRobotInsertKukaIR210)
        FreeCADGui.addCommand("RobotPy_Robot_InsertKukaIR125", CmdRobotInsertKukaIR125)
        FreeCADGui.addCommand("RobotPy_AddToolShape", CmdToolShape)
        FreeCADGui.addCommand("RobotPy_CreateTrajectory", CmdCreateTrajectory)
        FreeCADGui.addCommand("RobotPy_InsertWayPoint", CmdInsertwayPoint)
        FreeCADGui.addCommand("RobotPy_InsertWayPointPreSelect", CmdInsertwayPointPre)
        FreeCADGui.addCommand("RobotPy_Edge2Trac", CmdCreateEdge2Trac)
        FreeCADGui.addCommand("RobotPy_TrajectoryDressUp", CmdCreateTrajectoryDressUp)
        FreeCADGui.addCommand("RobotPy_TrajectoryCompound", CmdCreateTrajectoryCompund)
        FreeCADGui.addCommand("RobotPy_SetHomePos", CmdRobotSetHomePos)
        FreeCADGui.addCommand("RobotPy_RestoreHomePos", CmdRobotRestoreHomePos)
        FreeCADGui.addCommand("RobotPy_Simulate", CmdRobotSimulate)
        self.toolbar_commands = [
            "RobotPy_Create",
            "RobotPy_CreateTrajectory",
            "RobotPy_InsertWayPoint",
            "RobotPy_InsertWayPointPreSelect",
            "RobotPy_Edge2Trac",
            "RobotPy_TrajectoryDressUp",
            "RobotPy_TrajectoryCompound",
            "RobotPy_SetHomePos",
            "RobotPy_RestoreHomePos",
            "RobotPy_Simulate",
        ]
        self.menu_commands = [
            "RobotPy_CreateTrajectory",
            "RobotPy_InsertWayPoint",
            "RobotPy_InsertWayPointPreSelect",
            "RobotPy_SetHomePos",
            "RobotPy_RestoreHomePos",
            "RobotPy_Simulate",  # TODO ad some missing items here
        ]
        self.robot_add_submenu = [
            "RobotPy_Create",
            "RobotPy_Robot_InsertKukaIR500",
            "RobotPy_Robot_InsertKukaIR16",
            "RobotPy_Robot_InsertKukaIR210",
            "RobotPy_Robot_InsertKukaIR125",
            "RobotPy_AddToolShape",
        ]
        self.appendToolbar("RobotPy", self.toolbar_commands)
        self.appendMenu(["RobotPy", "Insert Robots"], self.robot_add_submenu)
        self.appendMenu("RobotPy", self.menu_commands)

    def Activated(self):
        return

    def Deactivated(self):
        return

    def ContextMenu(self, recipient):
        """This function is executed whenever the user right-clicks on screen"""
        # "recipient" will be either "view" or "tree"
        # self.appendContextMenu("My commands", self.list) # add commands to the context menu
        pass

    def GetClassName(self):
        # This function is mandatory if this is a full Python workbench
        # This is not a template, the returned string should be exactly "Gui::PythonWorkbench"
        return "Gui::PythonWorkbench"


FreeCADGui.addWorkbench(RobotPyWorkbench())
