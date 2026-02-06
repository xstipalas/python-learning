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

    @classmethod
    def from_string(cls, string):
        student_id, name, surname = string.split(',')

        return cls(int(student_id), name, surname)

    @classmethod
    def get_count(cls):
        return len(cls.student_list)

    @staticmethod
    def validate_email(email):
        return '@' in email and '.' in email

    @staticmethod
    def name_normalize(name):
        return name.title()

student1 = Student(0, 'Руслан', 'Сикалиев')
student2 = Student(1, 'Иван', 'Иванов')
student3 = Student(2, 'Артем', 'Филатов')
student4 = Student.from_string('3,Данил,Парков')

for student in Student.student_list:
    print(student)

print(Student.get_count())
print(Student.validate_email(student4.email))
print(Student.name_normalize('вАся'))


