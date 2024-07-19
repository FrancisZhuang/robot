import sys
from unittest import mock

import pytest
from apps.robot.service import CardinalDirection
from apps.robot.service import Robot
from exceptions.exceptions import InvalidInitialPosition
from models.models import CardinalPoint
from models.models import Direction


def test_robot(caplog):
    robot = Robot(1, 2, CardinalPoint.EAST)
    robot.move()
    robot.move()
    robot.turn(Direction.LEFT)
    robot.move()
    robot.report()

    assert "3, 3, NORTH" in caplog.text


def test_robot_init_fail(mock_point):
    with pytest.raises(InvalidInitialPosition):
        Robot(5, 0, mock_point)


def test_robot_move(mock_point):
    robot = Robot(0, 0, mock_point)

    robot.move()

    assert (robot.x, robot.y) == (0, 1)


def test_robot_move_out_of_table(mock_point):
    robot = Robot(0, 0, mock_point)

    for _ in range(6):
        robot.move()

    assert (robot.x, robot.y) == (0, 4)


def test_robot_turn(mock_point):
    robot = Robot(0, 0, mock_point)
    right = Direction.RIGHT

    robot.turn(right)

    assert robot.point == CardinalPoint.EAST


def test_robot_report(mock_point, caplog):
    robot = Robot(3, 0, mock_point)

    robot.report()

    assert "3, 0, NORTH" in caplog.text


def test_robot_is_on_table(mock_point):
    robot = Robot(0, 0, mock_point)

    robot.x, robot.y = 6, 7

    assert robot.is_on_table() is False


@mock.patch.object(sys, "exit")
def test_robot_end(mock_exit, mock_point):
    robot = Robot(0, 0, mock_point)

    robot.end()

    mock_exit.assert_called_once()


def test_cardinal_direction_turn():
    cardinal_direction = CardinalDirection()

    result = cardinal_direction.turn(CardinalPoint.WEST, Direction.RIGHT)

    assert result == CardinalPoint.NORTH


@pytest.mark.parametrize(
    "point,expected",
    [
        (CardinalPoint.EAST, CardinalPoint.SOUTH),
        (CardinalPoint.SOUTH, CardinalPoint.WEST),
        (CardinalPoint.WEST, CardinalPoint.NORTH),
        (CardinalPoint.NORTH, CardinalPoint.EAST),
    ],
)
def test_cardinal_direction_turn_right(point, expected):
    cardinal_direction = CardinalDirection()

    result = cardinal_direction.turn_right(point)

    assert result == expected


@pytest.mark.parametrize(
    "point,expected",
    [
        (CardinalPoint.EAST, CardinalPoint.NORTH),
        (CardinalPoint.SOUTH, CardinalPoint.EAST),
        (CardinalPoint.WEST, CardinalPoint.SOUTH),
        (CardinalPoint.NORTH, CardinalPoint.WEST),
    ],
)
def test_cardinal_direction_turn_left(point, expected):
    cardinal_direction = CardinalDirection()

    result = cardinal_direction.turn_left(point)

    assert result == expected
