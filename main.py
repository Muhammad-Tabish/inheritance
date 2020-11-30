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
    @property
    def weekly_salary (self):
        return self.salary * 37.5


rolf = working_student ('tab', 'waves', 19555)
rolf.marks.append(95)
rolf.marks.append(100)
print(rolf.salary)
print(rolf.name)
print(rolf.school)
print(rolf.weekly_salary)


print(f"my name is {rolf.name} i am from {rolf.school}school. i got {rolf.average()} marks in final year. my salary is {rolf.salary} and my weekly salary is {rolf.weekly_salary}")