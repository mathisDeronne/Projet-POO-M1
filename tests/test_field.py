from pytest import fixture, mark  # type: ignore
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
    "content, expected",
    [
        ("NONE", True),
        ("POTATO", False),
        ("LEEK", False),
        ("TOMATO", False),
        ("ONION", False),
        ("ZUCCHINI", False),
        ("test", False),
        (123, False),
        (-123, False),
        (123.4, False),
    ],
)
def test_field_content(base_field_data, content, expected):
    base_field_data["content"] = content
    field = Field(base_field_data)
    assert field.is_content_empty() is expected


@mark.parametrize(
    "content, expected",
    [
        ("POTATO", True),
        ("LEEK", True),
        ("TOMATO", True),
        ("ONION", True),
        ("ZUCCHINI", True),
        ("NONE", False),
        ("test", False),
        (123, False),
        (-123, False),
        (123.4, False),
    ],
)
def test_field_full(base_field_data, content, expected):
    base_field_data["content"] = content
    field = Field(base_field_data)
    assert field.is_content_full() is expected


@mark.parametrize(
    "needed_water, expected",
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
        (False, False),
        (True, False),
    ],
)
def test_field_needed_water(base_field_data, needed_water, expected):
    base_field_data["needed_water"] = needed_water
    field = Field(base_field_data)
    assert field.is_needed_water() is expected


@mark.parametrize(
    "bought, expected",
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
def test_field_bought(base_field_data, bought, expected):
    base_field_data["bought"] = bought
    field = Field(base_field_data)
    assert field.is_bought() is expected


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
def test_field_location(base_field_data, location, expected):
    base_field_data["location"] = location
    field = Field(base_field_data)
    assert field.is_location_valid() is expected


@fixture
def base_field_data2():
    return {
        "fields": [
            {
                "content": "POTATO",
                "needed_water": 6,
                "bought": True,
                "location": "FIELD1",
            },
            {
                "content": "TOMATO",
                "needed_water": 0,
                "bought": True,
                "location": "FIELD2",
            },
            {
                "content": "NONE",
                "needed_water": 0,
                "bought": False,
                "location": "FIELD3",
            },
            {
                "content": "NONE",
                "needed_water": 5,
                "bought": False,
                "location": "FIELD4",
            },
            {
                "content": "NONE",
                "needed_water": 4,
                "bought": True,
                "location": "5",
            },
        ]
    }


def test_watered_field_1(base_field_data2):
    assert Field.watered_field_1(base_field_data2) is True


def test_watered_field_2(base_field_data2):
    assert Field.watered_field_2(base_field_data2) is False


def test_watered_field_3(base_field_data2):
    assert Field.watered_field_3(base_field_data2) is False


def test_watered_field_4(base_field_data2):
    assert Field.watered_field_4(base_field_data2) is False


def test_watered_field_5(base_field_data2):
    assert Field.watered_field_5(base_field_data2) is False
