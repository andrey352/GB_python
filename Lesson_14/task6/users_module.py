

import json

class User:
    def __init__(self, name: str, id: int, level: int):
        self.id = id
        self.name = name
        self.level = level

    def __eq__(self, other: "User") -> bool:
        return self.name == other.name and self.id == other.id
    
    def __hash__(self) -> int:
        return self.id

    def __repr__(self):
        return f"User({self.name}, {self.id}, {self.level})"


def load_users(filename: str = "users.json") -> set[User]:
    with open("users.json", 'r') as source:
        data = json.load(source)
    return set(map(lambda x: User(**x), data))       # User(id=id, name=name, level=level)


if __name__ == "__main__":
    print(load_users())









