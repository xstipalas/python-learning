class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

class Department:
    def __init__(self, name):
        self.name = name
        self.course_list = [
            Course('Литература', 'Филатова М.Е.'),
            Course('Математика', 'Громов А.С.'),
            Course('Черчение', 'Баюгужина Р.Д.'),
            ]

class University:
    def __init__(self, name, department_list):
        self.name = name
        self.department_list = department_list

departments = [
    Department('Отдел А'),
    Department('Отдел Б'),
    Department('Отдел В'),
    ]

university = University('ГГНТУ', departments)
