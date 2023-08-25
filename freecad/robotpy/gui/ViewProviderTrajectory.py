from freecad.robotpy import ICONPATH
from os import path


# TODO: this needs an attach method, among other things
class ViewProviderTrajectory:
    def __init__(self, vobj):
        vobj.Proxy = self

    def getIcon(self):
        return path.join(ICONPATH, "Robot_Trajectory.svg")
