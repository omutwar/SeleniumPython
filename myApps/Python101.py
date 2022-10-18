import datetime
from typing import List

x = datetime.datetime.now()
y = datetime.datetime(2022, 10, 5)
print(x)

time1 = datetime.datetime(2018, 6, 1)
print(x.strftime("%z") + " <<< UTC offset")
print(x.strftime("%B"))
print(x.strftime("%W") + " <<< This is '%W' format")

# Take input from the user
name = input("What is your name? ")
print("Hello " + name)
birth_year = input("What year you were born? ")
age = x.year - int(birth_year)
print(age)


# ===================================================== TODO: This is conditional in Python, may need to spend more time on this
def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean


monday_temperature = [8.8, 9.1, 9.9]
student_grades = {"Mary": 9.1, "Sam": 8.8, "John": 7.5}

print(mean(monday_temperature))
print(mean(student_grades))
