class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def show_info(self):
        print('student name:', self.name)
        print('student age :', self.age)
        print('student grade', self.grade)

# create object 
student1 = student('israr', 18, "A")

# call method
student1.show_info()

        