from src.farm.field import Field


def test_field():
    field = Field(
        {"content": "NONE", "needed_water": 6, "bought": True, "location": "FIELD2"}
    )
    assert field.is_content_empty() is True
    assert field.is_bought() is True
    assert field.is_needed_water() is True
    assert field.is_location() is True
