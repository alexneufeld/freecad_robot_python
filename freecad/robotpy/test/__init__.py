import unittest
from FreeCAD import GuiUp
from .app import TestWaypoint

TestRobotPy = [
    TestWaypoint,
]

if GuiUp:
    # from .gui import someTest
    TestRobotPyGui = []
else:
    # create a dummy class to print a clean error message when trying to run the GUI
    # tests without a GUI:
    class dummy(unittest.TestCase):
        def test_incorrect_usage(self):
            raise RuntimeError("Tried to run RobotPy GUI tests without a GUI!")

    TestRobotPyGui = [
        dummy,
    ]


__all__ = [
    "TestRobotPy",
    "TestRobotPyGui",
]
