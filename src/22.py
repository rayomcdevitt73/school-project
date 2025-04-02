class SimpleSchoolProject:
    def __init__(self):
        self.students = []

    def add_student(self, student_name):
        self.students.append(student_name)

    def get_students(self):
        return self.students

if __name__ == "__main__":
    project = SimpleSchoolProject()
    project.add_student("John")
    print(project.get_students())
