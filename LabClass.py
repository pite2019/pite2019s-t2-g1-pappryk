from Student import Student
class LabClass:
    def __init__(self, class_name):
        self.students = []
        self.name = class_name
    
    def add_student(self, first_name, last_name):
        student = Student(first_name, last_name)
        self.students.append(student)
    
    def print_students(self):
        print(self.name + " :")
        for s in self.students:
            print("  " + s.first_name + " " + s.last_name)

    def add_grade(self, student_index, grade):
        self.students.add_grade(student_index, grade)
