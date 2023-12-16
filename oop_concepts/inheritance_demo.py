"""

"""


class Animal:
    def __init__(self, name):
        self.name = name
        print(f"An animal created! Name: {name}")

    def __str__(self):
        print(f"{self.name}")

    @staticmethod
    def eat():
        print("I am eating")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("Hello World!!")

    person3 = {'Name': 'Ford Prefect', 'Gender': 'Male', 'Organization': 'Researcher', 'Home Planet': 'Betelgeuse '
                                                                                                      'Seven'}


dog1 = Dog("Max")
print(dog1.person3['Name'])
