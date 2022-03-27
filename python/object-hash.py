from collections import Counter


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f'{self.name} {self.age}'
    
john = Person('John', 18)

eventRegister = {}

# John want to join the event
eventRegister[john] = True

# In the next day,
# he changes his mind

john = Person('John', 18)

eventRegister[john] = False

print(eventRegister)