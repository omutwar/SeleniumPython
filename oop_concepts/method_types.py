# Python OOP
class Employee:

    num_of_employees = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = '{}.{}'.format(self.first, self.last)
        self.pay = pay

        Employee.num_of_employees + 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, string: str):
        first, last, pay = string.split("-")
        return cls(first, last, pay)

    @staticmethod
    def this_is_static_method(first, last, pay):
        print("***: Below is coming from static method in the Employee() class")
        return "I am returning empty message"


emp_str_1 = 'Mark-Johnson-120000'
emp_str_2 = 'John-Markson-145000'
emp_str_3 = 'Jane-Doe-155000'

emp_1 = Employee.from_string(emp_str_1)
emp_2 = Employee.from_string(emp_str_2)
emp_3 = Employee.from_string(emp_str_3)

print(emp_1.first)
print(emp_2.last)

# Set new
print(emp_3.pay)
print(emp_3.email)

emp_4 = Employee('Corey', 'Schafer', 50000)
emp_5 = Employee('Test', 'Employee', 100000)

print(Employee.raise_amt)
print(emp_4.raise_amt)
print(emp_5.raise_amt)

print(Employee.num_of_employees)
print(emp_5.this_is_static_method("Benjamin", 'Barry', 150000))
