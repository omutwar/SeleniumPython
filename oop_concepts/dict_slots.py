import timeit
from dataclasses import dataclass
from functools import partial


@dataclass(slots=False)
class Person:
    name: str
    address: str
    email: str


@dataclass(slots=True)
class PersonSlots:
    name: str
    address: str
    email: str


# class PersonEmployee(PersonSlots, EmployeeSlots):
# pass

def set_get_delete(person: Person | PersonSlots):
    person.address = "123 Main st"
    person.address
    del person.address


def main():
    person = Person("John", "123 Main st", "john@doe.com")
    person_slots = PersonSlots("John", "123 Main St", "john@doe.com")
    no_slots = min(timeit.repeat(partial(set_get_delete, person), number=1000000))
    slots = min(timeit.repeat(partial(set_get_delete, person_slots), number=1000000))
    print(f'No Slots: {no_slots}')
    print(f'Slots: {slots}')
    print(f"% performance improvements: {(no_slots - slots) / no_slots:.2%}")


if __name__ == "__main__":
    main()
