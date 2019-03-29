from Student import Student
from LabClass import LabClass

class Diary:

    def __init__(self):
        self.lab_classes = []
    
    def add_lab_class(self, class_name):
        lab_class = LabClass(class_name)
        self.lab_classes.append(lab_class)