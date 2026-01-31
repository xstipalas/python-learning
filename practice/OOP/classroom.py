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

    def __repr__(self):
        return f'Student(student_id={self.student_id}, name={self.name!r}, surname={self.surname!r})'

for student in Student.student_list:
    print(student)


class Classroom:
    def __init__(self, name, student_list):
        self.name = name
        self.student_list = student_list

    def __len__(self):
        return len(self.student_list)

    def __getitem__(self, index):
        return self.student_list[index]

    def __contains__(self, student):
        return student in self.student_list

    def __iter__(self):
        return iter(self.student_list)

    def __repr__(self):
        return f'Classroom(name={self.name!r}, student_list={self.student_list})'

students = [
    Student(0, 'Руслан', 'Сикалиев'),
    Student(1, 'Иван', 'Иванов'),
    Student(2, 'Артем', 'Филатов'),
    Student(3, 'Данил', 'Парков'),
    ]
    
classroom = Classroom('10А', students)

print(len(classroom))
print(classroom[0])
print(Student(1, 'Иван', 'Иванов') in classroom)

for i in range(len(classroom)):
    print(classroom[i])

print(classroom)
