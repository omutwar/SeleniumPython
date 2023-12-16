import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


@dataclass(kw_only=True)
class Person:
    name: str
    address: str
    active: bool = True
    email_addresses: list[str] = field(default_factory=list)
    # If we want to stop some of the field from being initialized, we can set 'init=False'
    id: str = field(init=False, default_factory=generate_id)
    search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.search_string = f"{self.name} {self.address}"


def main() -> None:
    person = Person(name="John", address="123 Main St")
    print(person)


if __name__ == "__main__":
    main()
