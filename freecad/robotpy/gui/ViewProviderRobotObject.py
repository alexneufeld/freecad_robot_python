from freecad.robotpy import ICONPATH
from os import path

class ViewProviderTrajectoryDressUp:
    def __init__(self, vobj):
        vobj.Proxy = self

    def getIcon(self):
        return path.join(ICONPATH, "Robot_CreateRobot.svg")