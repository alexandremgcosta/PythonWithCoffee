class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self):
        return sum(self.marks) / len(self.marks)
    
# A CLASS WorkingStudent é uma extensão da class Student
# Usado o Super para chamar o self do __init__ de Student
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary= salary
    
    # O decorator property pode ser usado neste método
    # porque o unico parametro é o self
    @property    
    def weekly_salary(self):
        return self.salary * 37.5
  
        
rolf = WorkingStudent('Rolf', 'MIT', 15.50)


print(rolf.weekly_salary)