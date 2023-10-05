import PyKDL
import FreeCAD


def toFrame(To: FreeCAD.Placement) -> PyKDL.Frame:
    return PyKDL.Frame(PyKDL.Rotation.Quaternion(*To.Rotation), PyKDL.Vector(*To.Base))


def toPlacement(To: PyKDL.Frame) -> FreeCAD.Placement:
    x, y, z, w = To.M.GetQuaternion()
    return FreeCAD.Placement(
        FreeCAD.Vector(*To.p), FreeCAD.Rotation(*To.M.GetQuaternion())
    )
