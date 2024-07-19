import pytest
from models.models import CardinalPoint


@pytest.fixture
def mock_point():
    return CardinalPoint.NORTH
