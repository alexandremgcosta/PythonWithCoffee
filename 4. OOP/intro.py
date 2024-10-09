class Student:
    
    def __init__(self, new_name, new_grade):
        self.name = new_name
        self.grade = new_grade
    
    def __len__(self):
        return len(self.grade)
    
    def __getitem__(self, i):
        return self.grade[i]
    
    # TEM COMO OBJETIVO DAR PRINTOUT
    # USADO NO DEBUGGER
    def __repr__(self):
        return f'Student: {self.name}'  
    
    # DA ALGUMA INFORMAÇÃO DA CLASS
    def __str__(self):
        return f'{self.name} have {len(self.grade)} grades'      
        
    def average(self):
        return sum(self.grades)/len(self.grades)
    
student_one = Student('Rolf Smith', [70, 88, 90, 99])
student_two = Student('Jose', [50, 60, 99, 100])



# __class__ method
print(student_one.__class__)

# __len__ method
print(len(student_one.grade))

# __getitem__ method
print(student_two.grade[2])

# ASSIM QUE TEMOS OS METODOS __len__ e __getitem__
# CRIADOS É POSSIVEL USAR O ciclo for

for s in student_two.grade:
    print(s)

# GRAÇAS AO METODO __str__    
print(student_one)