class Parent:
    def __init__(self, name, age, eye_color='brown'):
        self.name = name
        self.age = age
        self.eye_color = eye_color


class Child(Parent):
    def __init__(self, name, age, gender, eye_color='blue'):
        self.gender = gender
        super().__init__(
            eye_color=eye_color,
            name=name,
            age=age
        )
