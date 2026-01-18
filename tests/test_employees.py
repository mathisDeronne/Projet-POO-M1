from pytest import fixture, mark  # type: ignore
from src.farm.employees import Employee


@fixture
def base_data():
    return {
        "id": 1,
        "location": "FIELD1",
        "tractor": {"location": "FIELD1", "id": 1},
        "salary": 1000,
    }


def test_base_employees(base_data):
    employee = Employee(base_data)
    assert employee.id_valid() is True
    assert employee.is_location_valid() is True
    assert employee.is_salary() is True
    assert employee.is_tractor() is True
