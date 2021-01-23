class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_name(self):
        return self.name


class StudentDAO:
    # This class can be abstract because it doesn't have implamentation
    def create(self, student):
        # Store student in the database
        pass

    def read(self, id):
        # get record by id
        pass

    def update(self, id, updated_student):
        pass

    def delete(self):
        pass


class StudentMySQLDAO(StudentDAO):
    pass


class StudentMongoDBDAO(StudentDAO):
    pass



