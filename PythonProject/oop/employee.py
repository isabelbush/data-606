class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_details(self):
        print(self.name)
        print(self.employee_id)

    def display_salary(self):
        print(self.salary)