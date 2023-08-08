from name_descriptor import NameDescriptor
import csv

# Основной класс
class Student:
    first_name = NameDescriptor()
    middle_name = NameDescriptor()
    last_name = NameDescriptor()

    def __init__(self, first_name, middle_name, last_name, csv_path):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name

        # Загрузка предметов из CSV файла
        with open(csv_path, 'r') as file:
            reader = csv.reader(file)
            self.subjects = {row[0]: {"grades": [], "test_scores": []} for row in reader}

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден.")
        if grade < 2 or grade > 5:
            raise ValueError("Оценка должна быть от 2 до 5.")
        self.subjects[subject]["grades"].append(grade)

    def add_test_score(self, subject, score):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден.")
        if score < 0 or score > 100:
            raise ValueError("Результат теста должен быть от 0 до 100.")
        self.subjects[subject]["test_scores"].append(score)

    def average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден.")
        scores = self.subjects[subject]["test_scores"]
        return sum(scores) / len(scores) if scores else 0

    def average_grade(self):
        total_grades = [grade for subj in self.subjects.values() for grade in subj["grades"]]
        return sum(total_grades) / len(total_grades) if total_grades else 0
