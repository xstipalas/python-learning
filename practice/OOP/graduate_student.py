class Student:
    student_list = []
    
    def __init__(self, student_id, name, surname):
        self.student_id = student_id
        self.name = name
        self.surname = surname

        self.__class__.student_list.append(self)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_id(self):
        return self.student_id

    def __str__(self):
        return f'{self.student_id} {self.name} {self.surname}'

class GraduateStudent(Student):
    def __init__(self, student_id, name, surname, thesis_topic):
        super().__init__(student_id, name, surname)
        self.thesis_topic = thesis_topic

    def __str__(self):
        return f'{self.student_id} {self.name} {self.surname} (Выпускник, тема диплома: "{self.thesis_topic}")'

    def defend_thesis(self):
        return f'Студент {self.name} {self.surname} защитил диплом на тему "{self.thesis_topic}"!'

student1 = Student(0, 'Руслан', 'Сикалиев')
student2 = GraduateStudent(1, 'Иван', 'Иванов', 'Польза пластика')
student3 = Student(2, 'Артем', 'Филатов')
student4 = GraduateStudent(3, 'Данил', 'Парков', 'Влияние работы на безработицу')

for student in Student.student_list:
    print(student)

print(student2.defend_thesis())
