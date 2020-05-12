class Student:
    def __init__(self, name, laptop):
        self.name = name
        self.laptop = laptop
        self.wisdom = 0
        self.homework=[]
    def __str__(self):
        return self.name
    def studentInfo(self):
        return self.name
    def study(self):
        self.wisdom += 1
    def doHomework(self, i):
        del self.homework[i]
               
class ClassManager:
    def __init__(self, name):
        self.name = name
        self.helpStudent = 0
    def __str__(self):
        return self.name
    def managerInfo(self):
        return self.name
    def doHelpStudent(self):
        self.helpStudent += 1
  
class Lecture:
    def __init__(self, name):
        self.name = name
        self.teacher = []
        self.lectureDay = []
    def __str__(self):
        return self.name
    def lectureInfo(self):
        return self.name
        
    
    

