from freecad.robotpy import ICONPATH

# from freecad.robotpy import RobotObject
import FreeCAD
import FreeCADGui
from os import path
from pivy import coin
from enum import Enum
from math import pi


class highlightModes(Enum):
    """reimplements the c++ equivalent for this, because I can't figure out a way to
    access the original from python.
    ref: https://github.com/FreeCAD/FreeCAD/blob/5a81fcd7a5019a5cbf35f9d410e629aae6a486a7/src/Gui/SoFCSelection.h
    """

    AUTO = 0
    ON = 1
    OFF = 2


class ViewProviderRobotObject:
    def __init__(self, vobj) -> None:
        vobj.addProperty("App::PropertyBool", "Manipulator").Manipulator = False
        self.selnode = coin.SoType.fromName("SoFCSelection").createInstance()
        # ref: https://github.com/FreeCAD/FreeCAD/blob/d95b26dfb5dd23eaee004b4af3cf5cf4766e7f9c/src/Mod/Draft/draftguitools/gui_trackers.py#L832
        self.pcRobotRoot = coin.SoType.fromName("SoFCSelection").createInstance()
        self.pcRobotRoot.highlightMode = highlightModes.OFF.value

        self.pcSimpleRoot = coin.SoType.fromName("SoFCSelection").createInstance()
        self.pcSimpleRoot.highlightMode = highlightModes.OFF.value

        self.pcOffRoot = coin.SoGroup()

        # set nodes for the manipulator outfit
        self.pcTcpRoot = coin.SoGroup()
        self.Axis1Node = None
        self.Axis2Node = None
        self.Axis3Node = None
        self.Axis4Node = None
        self.Axis5Node = None
        self.Axis6node = None
        self.pcDragger = None
        vobj.Proxy = self

    def setDragger(self) -> None:
        assert self.pcDragger is None
        self.pcDragger = coin.SoJackDragger()
        self.pcDragger.addMotionCallback(self.soDraggerMotionCallback)
        self.pcTcpRoot.addChild(self.pcDragger)
        # set the actual TCP position
        # TODO: missing PyKDL bindings for this to work
        # robObj = static_cast<Robot::RobotObject*>(pcObject);
        # robObj = pcObject
        loc = self.obj.Tcp.getValue()
        M = coin.SbMatrix()
        M.setTransform(
            coin.SbVec3f(loc.getPosition().x, loc.getPosition().y, loc.getPosition().z),
            coin.SbRotation(*loc.getRotation()),
            coin.SbVec3f(150, 150, 150),
        )
        self.pcDragger.setMotionMatrix(M)

    def resetDragger(self) -> None:
        assert self.pcDragger is not None
        FreeCADGui.coinRemoveAllChildren(self.pcTcpRoot)
        self.pcDragger = None

    def attach(self, vobj) -> None:
        vobj.addDisplayMode(self.pcRobotRoot, "VRML")
        self.pcRobotRoot.objectName = vobj.Object.Name
        self.pcRobotRoot.documentName = vobj.obj.Document.Name
        self.pcRobotRoot.subElementName = "Main"
        self.pcRobotRoot.addChild(self.pcTcpRoot)

        vobj.addDisplayMode(self.pcSimplRoot, "Simple")
        self.pcSimpleRoot.objectName = vobj.Object.Name
        self.pcSimpleRoot.documentName = vobj.obj.Document.Name
        self.pcSimpleRoot.subElementName = "Main"
        self.pcSimpleRoot.addChild(self.pcTcpRoot)

        vobj.addDisplayMode(self.pcOffRoot, "Off")
        self.pcOffRoot.addChild(self.pcTcpRoot)

    def getDisplayModes(self, vobj) -> list[str]:
        return ["VRML", "Simple", "Off"]

    def getDefaultDisplayMode(self) -> str:
        return "VRML"

    def setDisplayMode(self, mode):
        return mode

    def onChanged(self, vobj, prop) -> None:
        if prop == "Manipulator":
            if vobj.Manipulator:
                if not self.pcDragger:
                    self.setDragger()
            else:
                if self.pcDragger:
                    self.resetDragger()
        else:
            pass

    def updateData(self, obj, prop) -> None:
        if prop == "RobotVrmlFile":
            FreeCADGui.coinRemoveAllChildren(self.pcRobotRoot)
            # ref: https://github.com/MariwanJ/COIN3D_Snippet/blob/main/11.1.ReadFile.py
            mySceneInput = coin.SoInput()
            if not mySceneInput.openFile(obj.RobotVrmlFile):
                raise RuntimeError(f"Cannot open file {obj.RobotVrmlFile}")
            node = coin.SoDB.readAll(mySceneInput)
            if node:
                self.pcRobotRoot.addChild(node)
            self.pcRobotRoot.addChild(self.pcTcpRoot)

            # search for the connection points
            self.Axis1Node = None
            self.Axis2Node = None
            self.Axis3Node = None
            self.Axis4Node = None
            self.Axis5Node = None
            self.Axis6node = None

            searchAction = coin.SoSearchAction()
            path = coin.SoPath()

            # Axis 1
            searchAction.setName("FREECAD_AXIS1")
            searchAction.setInterest(coin.SoSearchAction.FIRST)
            searchAction.setSearchingAll(False)
            searchAction.apply(self.pcRobotRoot)
            path = searchAction.getPath()
            if path:
                node = path.getTail()
                if node and (node.getTypeId() == coin.SoVRMLTransform.getClassTypeId()):
                    self.Axis1Node = node
            # Axis 2
            searchAction.setName("FREECAD_AXIS2")
            searchAction.setInterest(coin.SoSearchAction.FIRST)
            searchAction.setSearchingAll(False)
            searchAction.apply(self.pcRobotRoot)
            path = searchAction.getPath()
            if path:
                node = path.getTail()
                if node and (node.getTypeId() == coin.SoVRMLTransform.getClassTypeId()):
                    self.Axis2Node = node
            # Axis 3
            searchAction.setName("FREECAD_AXIS3")
            searchAction.setInterest(coin.SoSearchAction.FIRST)
            searchAction.setSearchingAll(False)
            searchAction.apply(self.pcRobotRoot)
            path = searchAction.getPath()
            if path:
                node = path.getTail()
                if node and (node.getTypeId() == coin.SoVRMLTransform.getClassTypeId()):
                    self.Axis3Node = node
            # Axis 4
            searchAction.setName("FREECAD_AXIS4")
            searchAction.setInterest(coin.SoSearchAction.FIRST)
            searchAction.setSearchingAll(False)
            searchAction.apply(self.pcRobotRoot)
            path = searchAction.getPath()
            if path:
                node = path.getTail()
                if node and (node.getTypeId() == coin.SoVRMLTransform.getClassTypeId()):
                    self.Axis4Node = node
            # Axis 5
            searchAction.setName("FREECAD_AXIS5")
            searchAction.setInterest(coin.SoSearchAction.FIRST)
            searchAction.setSearchingAll(False)
            searchAction.apply(self.pcRobotRoot)
            path = searchAction.getPath()
            if path:
                node = path.getTail()
                if node and (node.getTypeId() == coin.SoVRMLTransform.getClassTypeId()):
                    self.Axis5Node = node

            # Axis 6
            searchAction.setName("FREECAD_AXIS6")
            searchAction.setInterest(coin.SoSearchAction.FIRST)
            searchAction.setSearchingAll(False)
            searchAction.apply(self.pcRobotRoot)
            path = searchAction.getPath()
            if path:
                node = path.getTail()
                if node and (node.getTypeId() == coin.SoVRMLTransform.getClassTypeId()):
                    self.Axis6Node = node

            if self.Axis1Node:
                self.Axis1Node.rotation.setValue(
                    coin.SbVec3f(0.0, 1.0, 0.0),
                    obj.Axis1 * pi / 180,
                )
            if self.Axis2Node:
                self.Axis2Node.rotation.setValue(
                    coin.SbVec3f(0.0, 1.0, 0.0),
                    obj.Axis2 * pi / 180,
                )
            if self.Axis3Node:
                self.Axis3Node.rotation.setValue(
                    coin.SbVec3f(0.0, 1.0, 0.0),
                    obj.Axis3 * pi / 180,
                )
            if self.Axis4Node:
                self.Axis4Node.rotation.setValue(
                    coin.SbVec3f(0.0, 1.0, 0.0),
                    obj.Axis4 * pi / 180,
                )
            if self.Axis5Node:
                self.Axis5Node.rotation.setValue(
                    coin.SbVec3f(0.0, 1.0, 0.0),
                    obj.Axis5 * pi / 180,
                )
            if self.Axis6Node:
                self.Axis6Node.rotation.setValue(
                    coin.SbVec3f(0.0, 1.0, 0.0),
                    obj.Axis6 * pi / 180,
                )

    def setAxisTo(
        self,
        A1: float,
        A2: float,
        A3: float,
        A4: float,
        A5: float,
        A6: float,
        Tcp: FreeCAD.Placement,
    ) -> None:
        pass

    def getIcon(self):
        return path.join(ICONPATH, "Robot_CreateRobot.svg")
