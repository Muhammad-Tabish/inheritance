class student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
     return sum(self.marks) / len(self.marks)

class working_student (student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary    


rolf = working_student ('tab', 'waves', 19555)
print(rolf.salary)