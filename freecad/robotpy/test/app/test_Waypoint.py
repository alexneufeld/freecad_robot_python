import unittest
from freecad.robotpy.app import Waypoint, WaypointType
from FreeCAD import Placement


class TestWaypoint(unittest.TestCase):
    def test_waypoint(self):
        pl = Placement()
        wp = Waypoint("MyWaypoint", pl)
        self.assertEqual(wp.Name, "MyWaypoint")
        self.assertEqual(wp.EndPos, pl)
        self.assertEqual(wp.Type, WaypointType.LINE)
        self.assertEqual(wp.Velocity, 2000)
        self.assertEqual(wp.Acceleration, 100)
        self.assertEqual(wp.Cont, False)
        self.assertEqual(wp.Tool, 0)
        self.assertEqual(wp.Base, 0)
