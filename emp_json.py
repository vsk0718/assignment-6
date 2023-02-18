import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

with open("D:\\vaishali\\python\\assignments\\json\\employees.json") as file:
    employee_data = json.load(file)

employee_list = []
for emp in employee_data:
    employee_list.append(Employee(emp['Name'], emp['DOB'], emp['Height'], emp['City'], emp['State']))

for emp in employee_list:
    print(emp.name, emp.dob, emp.height, emp.city, emp.state)
