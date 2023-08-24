import PyKDL
import FreeCAD


def vec2vec(vec: PyKDL.Vector) -> FreeCAD.Vector:
    return FreeCAD.Vector(*vec)


def pos2placement(pos) -> FreeCAD.Placement:
    pass
