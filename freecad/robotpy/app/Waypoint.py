from FreeCAD import Placement
from dataclass import dataclass
from enum import Enum, auto


class WaypointType(Enum):
    UNDEF = auto()
    PTP = auto()
    LINE = auto()
    CIRC = auto()
    WAIT = auto()


@dataclass(init=False)
class Waypoint:
    """The representation of a waypoint in a trajectory"""

    Name: str
    EndPos: Placement
    Type: WaypointType = WaypointType.LINE
    Velocity: float = 2000
    Acceleration: float = 100
    Cont: bool = False
    Tool: int = 0
    Base: int = 0

    def __init__(self, Name, EndPos) -> None:
        self.Name = Name
        self.EndPos = EndPos
