import json
import random
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Employee(BaseModel):
    name: str
    id: int
    title: str


class Delete_Employee(BaseModel):
    name: str


@app.post("/employees")
def add_employee(New_Employee: Employee):
    #Unique ID generation 
    list_IDs = random.sample(range(1, 1000), 999)
    c = 0
    id = list_IDs[c]
    c = c + 1      
    with open("entities.json", "w") as file:
        content = json.load(file)
        Temp = {New_Employee.name: {"id": id, "title": New_Employee.title, "salary": New_Employee.salary}}
        content.update(Temp)
    with open("entities.json", "w") as file:
        json.dump(content, file, indent=5)
        return temp    

@app.get("/employees")
def get_employees(filter: str) -> dict:
    with open("entities.json", "r") as file:
        content = json.load(file)
    return content


@app.delete("/employees")
def delete_employees(DE: Delete_Employee):
    try:    
    employees = get_employees()
    del employees[DE.name]
    with open("entities.json", "w") as file:
        json.dump(employees, file, indent=5)
    except KeyError:
        error_message= 'Employee Not Found'
        print(error_message)
    return DE.name    

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
