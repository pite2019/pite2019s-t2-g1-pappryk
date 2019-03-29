class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = []
        self.attendance_counter = 0
    
    def add_grade(self, grade):
        grades.append(grade)
    
    def get_avarage_score(self):
        return sum(grades)/len(grades)

    def add_attendance(self):
        self.attendance_counter += 1    