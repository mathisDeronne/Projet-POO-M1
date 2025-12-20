from pytest import fixture, mark
from src.farm.field import Field


@fixture
def base_field_data():
    return {
        "content": "POTATO",
        "needed_water": 6,
        "bought": True,
        "location": "FIELD2",
    }


def test_base_field(base_field_data):
    field = Field(base_field_data)
    assert field.is_content_empty() is False
    assert field.is_bought() is True
    assert field.is_needed_water() is True
    assert field.is_location_valid() is True


@mark.parametrize(
    "content, val1",
    [
        ("NONE", True),
        ("test", False),
    ],
)
def test_field_content(base_field_data, content, val1):
    base_field_data["content"] = content
    field = Field(base_field_data)
    assert field.is_content_empty() is val1


@mark.parametrize(
    "needed_water, val2",
    [
        (1, True),
        (6, True),
        (10, True),
        (20, True),
        (+8, True),
        (+15, True),
        (-5, False),
        (1.5, False),
        (-1.5, False),
        (0, False),
        (+0, False),
        (-0, False),
        ("", False),
        ("4", False),
        ("+5", False),
        ("-12", False),
        ("test", False),
    ],
)
def test_field_needed_water(base_field_data, needed_water, val2):
    base_field_data["needed_water"] = needed_water
    field = Field(base_field_data)
    assert field.is_needed_water() is val2


@mark.parametrize(
    "bought, val3",
    [
        (True, True),
        (False, False),
        ("True", False),
        ("False", False),
        (10, False),
        (10.10, False),
        (-10, False),
        ("10", False),
        ("test", False),
    ],
)
def test_field_bought(base_field_data, bought, val3):
    base_field_data["bought"] = bought
    field = Field(base_field_data)
    assert field.is_bought() is val3


@mark.parametrize(
    "location, val4",
    [
        ("FIELD1", True),
        ("FIELD2", True),
        ("FIELD3", True),
        ("FIELD4", True),
        ("FIELD5", True),
        ("FIELD6", False),
        ("FIELD0", False),
        ("FIELD-2", False),
        ("1", False),
        ("FIELD", False),
        ("test", False),
        ("test2", False),
        ("True", False),
        (10, False),
        (10.10, False),
        (-10, False),
        ("10", False),
    ],
)
def test_field_location(base_field_data, location, val4):
    base_field_data["location"] = location
    field = Field(base_field_data)
    assert field.is_location_valid() is val4
