"""You can add first name last name as well as salary.
you can also add objects just by strings you can also add increment 
and change increment as per requirement"""


class Employee:

    increment = 1.5

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary = int(self.salary * Employee.increment)

    @classmethod
    def changeincrement(cls, amount):
        increment = amount

    @classmethod
    def from_dash(cls, emp_string):
        fname, lname, salary = emp_string.split('-')
        return cls(fname, lname, salary)

    @staticmethod
    def is_holiday(day):
        if day == 'sunday':
            return f'{day} your Holiday'
        else:
            return f'{day} is working day'


print(Employee.is_holiday('sunday'))
dixant = Employee('Dixant', 'Dutt', 45000)
divyank = Employee.from_dash('Divyank-Sharma-42000')


print(dixant.salary)
dixant.increase()
print(dixant.salary)

dixant.changeincrement(2.0)
dixant.increase()
print(dixant.salary)

print(divyank.fname)
print(divyank.lname)
print(divyank.salary)
