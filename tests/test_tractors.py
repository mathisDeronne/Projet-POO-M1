from pytest import fixture, mark  # type: ignore
from src.farm.tractors import Tractors


@fixture
def base_data():
    return {
        "location": "FIELD2",
        "id": 1,
    }


def test_base_tractors(base_data):
    tractor = Tractors(base_data)
    assert tractor.id_is() is True
    assert tractor.is_location_valid() is True


@mark.parametrize(
    "location, expected",
    [
        ("FIELD1", True),
        ("FIELD2", True),
        ("FIELD3", True),
        ("FIELD4", True),
        ("FIELD5", True),
        ("FIELD6", False),
        ("FIELD0", False),
        ("FIELD-2", False),
        ("FIELD", False),
        ("test", False),
        ("1", False),
        (10, False),
        (10.10, False),
        (0, False),
        (1, False),
        (False, False),
        (True, False),
    ],
)
def test_field_location(base_data, location, expected):
    base_data["location"] = location
    tractor = Tractors(base_data)
    assert tractor.is_location_valid() is expected
