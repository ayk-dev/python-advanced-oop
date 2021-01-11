class Person:
    def sleep(self):
        return 'sleeping...'


class Employee:
    def get_fired(self):
        return 'fired...'


class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'


person = Person()
employee = Employee()
teacher = Teacher()

print(person.sleep())
print(employee.get_fired())
print(teacher.teach())
print(teacher.sleep())
print(teacher.get_fired())
print(Person.__subclasses__())


