
class student:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:

            value +=student    
s1 = Student('Tim', 18,57)
s2 = Student('Bill', 19,75)
s3 = student('jill',19,6500)
course = Course(;='student')

course =Course('Science', 2)
course.add.student(s1)
course.add.student(s2)
