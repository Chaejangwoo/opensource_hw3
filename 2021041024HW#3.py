class Student:
    def __init__(self, student_id, name, english, c_language, python):
        self.student_id = student_id
        self.name = name
        self.english = english
        self.c_language = c_language
        self.python = python
        self.total = self.calculate_total()
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()
        self.rank = None

    def calculate_total(self):
        return self.english + self.c_language + self.python

    def calculate_average(self):
        return self.total / 3

    def calculate_grade(self):
        if self.average >= 90:
            return 'A'
        elif self.average >= 80:
            return 'B'
        elif self.average >= 70:
            return 'C'
        elif self.average >= 60:
            return 'D'
        else:
            return 'F'


students = []

def input_student():
    student_id = input("학번을 입력하세요: ")
    name = input("이름을 입력하세요: ")
    english = int(input("영어 점수를 입력하세요: "))
    c_language = int(input("C-언어 점수를 입력하세요: "))
    python = int(input("파이썬 점수를 입력하세요: "))
    student = Student(student_id, name, english, c_language, python)
    students.append(student)

def calculate_rank():
    sorted_students = sorted(students, key=lambda student: student.total, reverse=True)
    for i, student in enumerate(sorted_students):
        student.rank = i + 1

def search_student(search_term):
    for student in students:
        if student.student_id == search_term or student.name == search_term:
            return student
    return None

def insert_student(student):
    students.append(student)

def delete_student(student_id):
    for i, student in enumerate(students):
        if student.student_id == student_id:
            del students[i]
            return True
    return False

def sort_students():
    return sorted(students, key=lambda student: student.total, reverse=True)

def count_students_above_80():
    count = 0
    for student in students:
        if student.average >= 80:
            count += 1
    return count

def print_students():
    for student in students:
        print(f"학번: {student.student_id}, 이름: {student.name}, 영어: {student.english}, C-언어: {student.c_language}, 파이썬: {student.python}, 총점: {student.total}, 평균: {student.average:.2f}, 학점: {student.grade}, 등수: {student.rank}")

# 예시 사용
for _ in range(5):
    input_student()

calculate_rank()

print_students()

# 탐색 예시
search_term = input("탐색할 학번 또는 이름을 입력하세요: ")
search_result = search_student(search_term)
if search_result:
    print(f"탐색 결과: 학번: {search_result.student_id}, 이름: {search_result.name}")
else:
    print("해당하는 학생을 찾을 수 없습니다.")
