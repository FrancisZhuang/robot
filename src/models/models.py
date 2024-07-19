from enum import Enum


class Command(Enum):
    REPORT = "REPORT"
    MOVE = "MOVE"
    END = "END"


class Direction(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class CardinalPoint(Enum):
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"
