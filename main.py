class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

    def add_grade(self, course, grade):
        if course in self.courses_attached:
            if course in self.grades:
                self.grades[course].append(grade)
            else:
                self.grades[course] = [grade]

    def middle_grades(self):
        total_grades = 0
        count = 0
        for course in self.grades:
            total_grades += sum(self.grades[course])
            count += len(self.grades[course])
        if count:
            return round(total_grades / count, 2)
        else:
            return 0

    def __lt__(self, other):
        return self.middle_grades() < other.middle_grades()

    def __gt__(self, other):
        return self.middle_grades() > other.middle_grades()

    def __eq__(self, other):
        return self.middle_grades() == other.middle_grades()

    def __le__(self, other):
        return self.middle_grades() <= other.middle_grades()

    def __ge__(self, other):
        return self.middle_grades() >= other.middle_grades()

    def __str__(self):
        middle_grades = self.middle_grades()
        return f"Имя: {self.name}" \
               f"\nФамилия: {self.surname}" \
               f"\nСредняя оценка за домашние задания: {middle_grades}"\
               f"\nКурсы в процессе обучения: {', '.join(self.courses_in_progress)}"\
               f"\nЗавершенные курсы: {', '.join(self.finished_courses)}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def add_grade(self, course, grade):
        if course in self.courses_attached:
            if course in self.grades:
                self.grades[course].append(grade)
            else:
                self.grades[course] = [grade]

    def middle_grades(self):
        total_grades = 0
        count = 0
        for course in self.grades:
            total_grades += sum(self.grades[course])
            count += len(self.grades[course])
        if count:
            return round(total_grades / count, 1)
        else:
            return 0

    def __lt__(self, other):
        return self.middle_grades() < other.middle_grades()

    def __gt__(self, other):
        return self.middle_grades() > other.middle_grades()

    def __eq__(self, other):
        return self.middle_grades() == other.middle_grades()

    def __le__(self, other):
        return self.middle_grades() <= other.middle_grades()

    def __ge__(self, other):
        return self.middle_grades() >= other.middle_grades()

    def __str__(self):
        return f"Имя:{self.name}" \
               f"\nФамилия:{self.surname}" \
               f"\nСредняя оценка за курсы: {Lecturer.middle_grades(self)}"


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}" \
               f"\nФамилия: {self.surname}"


some_student = [Student('Sergey', 'Artiomov'),
                Student('Matvey', 'Artiomov')]
some_student[0].courses_in_progress += ['Python']
some_student[1].courses_in_progress += ['Python']
some_student[0].courses_in_progress += ['Git']
some_student[1].courses_in_progress += ['Git']
some_student[0].finished_courses += ['Введение в программирование']
some_student[1].finished_courses += ['Введение в программирование']
some_student[0].courses_attached += ['Python']
some_student[1].courses_attached += ['Python']
some_student[0].courses_attached += ['Git']
some_student[1].courses_attached += ['Git']
some_student[0].courses_attached += ['Java']
some_student[1].courses_attached += ['Java']
some_student[0].add_grade('Python', 7)
some_student[1].add_grade('Python', 6)
some_student[0].add_grade('Python', 9)
some_student[1].add_grade('Python', 5)
some_student[0].add_grade('Python', 10)
some_student[1].add_grade('Python', 10)
some_student[0].add_grade('Java', 5)
some_student[1].add_grade('Java', 10)
some_student[0].add_grade('Git', 8)
some_student[1].add_grade('Git', 9)


some_reviewer = Reviewer('Master', 'Yoda')
some_reviewer.courses_attached += ['Python']

some_lecturer = [Lecturer('Professor', 'Kyzmina'),
                 Lecturer('Professor', 'Saharov')]

some_lecturer[0].courses_attached += ['Python']
some_lecturer[1].courses_attached += ['Python']
some_lecturer[0].courses_attached += ['Git']
some_lecturer[1].courses_attached += ['Git']
some_lecturer[0].add_grade('Python', 10)
some_lecturer[1].add_grade('Git', 9.9)
some_lecturer[0].add_grade('Java', 10)
some_lecturer[1].add_grade('Python', 9.9)
some_lecturer[0].add_grade('Python', 10)
some_lecturer[1].add_grade('Python', 10)
some_lecturer[0].add_grade('Python', 10)
some_lecturer[1].add_grade('Python', 10)
some_lecturer[0].add_grade('Java', 10)
some_lecturer[1].add_grade('Git', 9.5)

print(some_reviewer)
print(some_lecturer[0])
print(some_lecturer[1])
print(some_student[0])
print(some_student[1])
print(some_student[0] > some_student[1])
print(some_student[0] < some_student[1])