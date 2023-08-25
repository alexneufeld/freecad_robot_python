from freecad.robotpy import ICONPATH
from os import path


class ViewProviderEdge2Trac:
    def __init__(self, vobj):
        vobj.Proxy = self

    def getIcon(self):
        return path.join(ICONPATH, "Robot_Edge2Trac.svg")
