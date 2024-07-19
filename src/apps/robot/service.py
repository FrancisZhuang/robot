import sys

from exceptions.exceptions import InvalidInitialPosition
from models.models import CardinalPoint
from models.models import Direction
from utils.logger import logger


class Robot:
    def __init__(
        self, x: int, y: int, point: CardinalPoint, rows: int = 5, cols: int = 5
    ):
        self.rows = rows
        self.cols = cols
        self.x = x
        self.y = y
        self.point = point
        self.is_initial_valid()

    def is_initial_valid(self):
        if not self.is_on_table():
            raise InvalidInitialPosition()

    def move(self):
        temp = (self.x, self.y)

        match self.point:
            case CardinalPoint.EAST:
                self.x += 1
            case CardinalPoint.WEST:
                self.x -= 1
            case CardinalPoint.NORTH:
                self.y += 1
            case CardinalPoint.SOUTH:
                self.y -= 1

        if not self.is_on_table():
            self.x, self.y = temp

    def turn(self, direction: Direction):  # direction: left or right
        cardinal_direction = CardinalDirection()
        self.point = cardinal_direction.turn(point=self.point, direction=direction)

    def report(self):
        logger.info(msg=f"{self.x}, {self.y}, {self.point.value}")

    def is_on_table(self) -> bool:  # out of table
        return (0 <= self.x < self.rows) and (0 <= self.y < self.cols)

    def end(self):
        sys.exit()


class CardinalDirection:
    def turn(self, point: CardinalPoint, direction: Direction):
        if direction == Direction.RIGHT:
            return self.turn_right(point)
        elif direction == Direction.LEFT:
            return self.turn_left(point)

    def turn_right(self, point: CardinalPoint) -> CardinalPoint:
        match point:
            case CardinalPoint.EAST:
                return CardinalPoint.SOUTH
            case CardinalPoint.WEST:
                return CardinalPoint.NORTH
            case CardinalPoint.NORTH:
                return CardinalPoint.EAST
            case CardinalPoint.SOUTH:
                return CardinalPoint.WEST

    def turn_left(self, point: CardinalPoint) -> CardinalPoint:
        match point:
            case CardinalPoint.EAST:
                return CardinalPoint.NORTH
            case CardinalPoint.WEST:
                return CardinalPoint.SOUTH
            case CardinalPoint.NORTH:
                return CardinalPoint.WEST
            case CardinalPoint.SOUTH:
                return CardinalPoint.EAST
