def log_creation(cls):
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        print(f'Создан объект класса {cls.__name__} с аргументами {args} и {kwargs}')
        original_init(self, *args, **kwargs)

    cls.__init__ = new_init
    return cls

@log_creation
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

student1 = Student(0, 'Руслан', 'Сикалиев')
student2 = Student(1, 'Иван', 'Иванов')
student3 = Student(2, 'Артем', 'Филатов')
student4 = Student(3, 'Данил', 'Парков')
