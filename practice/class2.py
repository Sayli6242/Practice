class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        self.is_active = False

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


s1 = student("Tim", 18, 57)
s2 = student("Bill", 19, 75)
s3 = student("jill", 19, 65)

Course = Course("Science", 2)
Course.add_student(s1)
Course.add_student(s2)
print(Course.add_student(s3))
print(Course.get_average_grade())
