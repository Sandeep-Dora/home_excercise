from server import app
from client import get_employees


def test_add_employee():
    response = client.post("/employees",json={"name": "Employee_Name","title": "Employee_Title","salary": 30000})
    assert response.status_code == 200
    assert response.json()['testName']['title'] == 'Employee_Name'
    assert response.json()['testName']['salary'] == 30000


def test_delete_inexistent_employee():
    response = client.delete("/employees",json={"name": "Non_Existing_Employee"})
    assert response.status_code == 200


def test_delete_employee():
    response = client.delete("/employees",json={"name": "XXX"})		# XXX is to be replaced by the Name of the Employee to Delete
    assert response.status_code == 200


def test_add_employee_with_existing_id():
    response = client.post("/employees",json={"name": "Employee_Name","title": "Employee_Title","salary": 30000})
    assert response.status_code == 200


def test_get_all_employees():
    response = client.get("/employees")
    assert response.status_code == 200
    print(f"Response contents are- {response.content}")
