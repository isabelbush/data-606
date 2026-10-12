from employee import Employee

class Contractor(Employee):
    def __init__(self, name, employee_id, hours, rate):
        super().__init__(name, employee_id)
        self.hours = hours
        self.rate = rate

    def display_salary(self):
        print(self.hours * self.rate)