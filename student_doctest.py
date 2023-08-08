import csv
from lesson13.student_exeptions import StudentNameError, InvalidScoreError, InvalidSubjectError
import doctest

class Student:
    def __init__(self, name, csv_filename):
        """
        Initializes a Student with a name and subjects loaded from a CSV file.
        
        >>> s = Student("John Doe", "sample.csv")
        >>> s.name
        'John Doe'
        
        >>> s2 = Student("john", "sample.csv")
        Traceback (most recent call last):
        ...
        StudentNameError
        
        """
        if not name.istitle() or not name.replace(" ", "").isalpha():
            raise StudentNameError()

        self.name = name
        self.subjects = self.load_subjects_from_csv(csv_filename)
        self.scores = {subject: [] for subject in self.subjects}
        self.test_results = {subject: [] for subject in self.subjects}

    def load_subjects_from_csv(self, csv_filename):
        """
        Load subjects from a CSV file and return them as a list.
        
        Assuming sample.csv contains:
        Math,Physics,History
        
        >>> s = Student("John Doe", "sample.csv")
        >>> s.load_subjects_from_csv("sample.csv")
        ['Math', 'Physics', 'History']
        
        """
        with open(csv_filename, "r") as file:
            reader = csv.reader(file)
            return next(reader)

    def add_score(self, subject, score):
        """
        Add a score for a subject.
        
        >>> s = Student("John Doe", "sample.csv")
        >>> s.add_score("Math", 4)
        >>> s.add_score("Math", 7)
        Traceback (most recent call last):
        ...
        InvalidScoreError: Invalid score: 7
        """
        if subject not in self.subjects:
            raise InvalidSubjectError(subject)
        
        if score < 2 or score > 5:
            raise InvalidScoreError(f"Invalid score: {score}")
        
        self.scores[subject].append(score)


if __name__ == "__main__":
    doctest.testmod()