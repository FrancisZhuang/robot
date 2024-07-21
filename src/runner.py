from typing import Tuple

from apps.robot.service import Robot
from exceptions.exceptions import IncorrectCommand
from exceptions.exceptions import InvalidInitialPosition
from models.models import CardinalPoint
from models.models import Command
from models.models import Direction
from utils.logger import logger


def valid_first_command(command: str) -> Tuple[int, int, CardinalPoint] | None:
    command = command.upper().replace("PLACE", "").strip()
    try:
        x, y, point = command.split(",")
        if not x.isnumeric() or not y.isnumeric() or point not in CardinalPoint:
            raise IncorrectCommand("Expected format like (x, y, point).")
        return int(x), int(y), CardinalPoint(point)

    except IncorrectCommand and ValueError:
        logger.error("Invalid Command - Expected format like (x, y, point).")

    except InvalidInitialPosition:
        logger.error("Invalid initial position.")


def valid_command(command: str) -> Command | Direction | None:
    command = command.upper().strip()
    try:
        if command in Command:
            return Command(command)
        if command in Direction:
            return Direction(command)
        raise IncorrectCommand("Expected Move, Left, Right or Report.")

    except IncorrectCommand:
        logger.error("Invalid Command - Expected Move, Left, Right or Report.")


def main():
    initial_place = False
    x, y, point = -1, -1, None

    while not initial_place:
        init_command = input("Place your robot - Place X, Y, CardinalPoint\n")
        init_command = valid_first_command(init_command)
        if init_command:
            x, y, point = init_command
            initial_place = True

    if x >= 0 and y >= 0 and point:
        robot = Robot(x, y, point)
    else:
        return

    while True:
        command = input("Execute Robot - Move, Left, Right or Report\n")
        command = valid_command(command)
        if type(command) is Command:
            match command:
                case Command.MOVE:
                    robot.move()
                case Command.REPORT:
                    robot.report()
                case Command.END:
                    robot.end()
        elif type(command) is Direction:
            robot.turn(command)


if __name__ == "__main__":
    main()
