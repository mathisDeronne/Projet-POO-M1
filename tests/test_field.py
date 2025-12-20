from src.farm.field import Field


def test_field():
    field = Field(
        {"content": "NONE", "needed_water": 6, "bought": True, "location": "FIELD2"}
    )
    assert field.is_content_empty() is True
    assert field.is_bought() is True
    assert field.is_needed_water() is True
    assert field.is_location() is True


def test_field2():
    field = Field(
        {"content": "POTATO", "needed_water": 0, "bought": False, "location": "test"}
    )
    assert field.is_content_empty() is False
    assert field.is_bought() is False
    assert field.is_needed_water() is False
    assert field.is_location() is False


def test_field3():
    field = Field(
        {"content": "POTATO", "needed_water": -1, "bought": False, "location": "FIELD7"}
    )
    assert field.is_needed_water() is False
    assert field.is_location() is False
