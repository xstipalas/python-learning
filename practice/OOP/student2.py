class Student:
    student_list = []
    
    def __init__(self, student_id, name, surname):
        self.__student_id = student_id
        self.name = name
        self.surname = surname
        self.email = f'{surname.lower()}.{name.lower()}@mail.ru'

        self.__class__.student_list.append(self)

    @property
    def student_id(self):
        return self.__student_id

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'

    def __str__(self):
        return f'{self.student_id} {self.full_name} (Почта: {self.email})'

student1 = Student(0, 'Руслан', 'Сикалиев')
student2 = Student(1, 'Иван', 'Иванов')
student3 = Student(2, 'Артем', 'Филатов')
student4 = Student(3, 'Данил', 'Парков')

for student in Student.student_list:
    print(student)


