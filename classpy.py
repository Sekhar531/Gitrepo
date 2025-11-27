import string
class student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade
class course:
    def __init__(self,name,maxstudents):
        self.name = name
        self.maxstudents = maxstudents
        self.students = []
    def add_student(self,student):
        if len(self.student) < self.maxstudents:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        pass

s1 = student("subbu",17,90)
s2 = student("Ram",17,76)
s3 = student("subbu",17,85)

cs = course("science",2)
cs.add_student(s1)
cs.add_student(s2)

print(cs.students)