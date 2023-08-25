from os import path
# from . import gui
# from . import app

ICONPATH = path.join(path.dirname(__file__), "icons")
RESOURCEPATH = path.join(path.dirname(__file__), "resources")
UIPATH = path.join(path.dirname(__file__), "ui")

__all__ = ["ICONPATH", "RESOURCEPATH", "UIPATH"]
