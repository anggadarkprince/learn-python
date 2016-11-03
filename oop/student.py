class Student:
    # fields = name, id, grades(list)
    grades = []

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def addGrade(self, grade):
        self.grades.append(grade)

    def showGrades(self):
        grds = ''
        for grade in self.grades:
            grds += str(grade) + ' '
        return grds

student = Student('Jones', '123')
student.addGrade(89)
student.addGrade(54)
student.addGrade(87)
print(student.showGrades())
