from student_exeptions import StudentNameError, InvalidSubjectError, InvalidScoreError
import csv

class Student:
    def __init__(self, name, csv_filename):
        if not name.istitle() or not name.replace(" ", "").isalpha():
            raise StudentNameError()

        self.name = name
        self.subjects = self.load_subjects_from_csv(csv_filename)
        self.scores = {subject: [] for subject in self.subjects}
        self.test_results = {subject: [] for subject in self.subjects}

    def load_subjects_from_csv(self, csv_filename):
        """Load subjects from a CSV file and return them as a list."""
        with open(csv_filename, "r") as file:
            reader = csv.reader(file)
            return next(reader)

    def add_score(self, subject, score):
        if subject not in self.subjects:
            raise InvalidSubjectError(subject)
        
        if score < 2 or score > 5:
            raise InvalidScoreError(score)
        
        self.scores[subject].append(score)

    def add_test_result(self, subject, result):
        if subject not in self.subjects:
            raise InvalidSubjectError(subject)
        
        if result < 0 or result > 100:
            raise InvalidScoreError(result, score_type="Результат теста")
        
        self.test_results[subject].append(result)

    def average_test_score(self, subject):
        if subject not in self.subjects:
            raise InvalidSubjectError(subject)
        
        return sum(self.test_results[subject]) / len(self.test_results[subject]) if self.test_results[subject] else 0

    def average_score(self):
        total_scores = sum([sum(scores) for scores in self.scores.values()])
        total_count = sum([len(scores) for scores in self.scores.values()])
        return total_scores / total_count if total_count else 0
