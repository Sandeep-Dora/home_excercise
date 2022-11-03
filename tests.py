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
    assert response.json() == 'Non_Existing_Employee'               # Will throw the name of the "Non_Existing_Employee" in the response if name is not found


def test_delete_employee():
    response = client.delete("/employees",json={"name": "XXX"})		# XXX is to be replaced by the Name of the Employee to Delete
    assert response.status_code == 200


def test_add_employee_with_existing_id():
    response = client.post("/employees",json={"name": "Employee_Name","title": "Employee_Title","salary": 30000})
    assert response.status_code == 200
    
    
def test_add_employee_with_empty_data():
    response = client.post("/employees",json={}    )
    assert response.status_code == 400                              # Error reponse code for mandatory fields missing   

    
def test_add_multiple_employees(name, title, salary):
    for i in range(0, 3):
        response = client.post("/employees",json={"name": name,"salary": salary,"title": title}
        assert response.status_code == 200
        assert response.json()[name]['title'] == title
        assert response.json()[name]['salary'] == salary        


def test_get_all_employees():
    response = client.get("/employees")
    assert response.status_code == 200
    print(f"Response contents are- {response.content}")
