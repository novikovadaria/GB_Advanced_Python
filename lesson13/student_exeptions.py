class StudentNameError(Exception):
    def __init__(self, message="Имя студента введено неверно. Оно должно содержать только буквы и начинаться с заглавной буквы."):
        self.message = message
        super().__init__(self.message)

class InvalidSubjectError(Exception):
    def __init__(self, subject_name):
        self.message = f"Предмет '{subject_name}' не найден в файле CSV."
        super().__init__(self.message)

class InvalidScoreError(Exception):
    def __init__(self, score, score_type="Оценка"):
        self.message = f"{score_type} '{score}' недействителен. Оценки должны быть от 2 до 5, а результаты тестов от 0 до 100."
        super().__init__(self.message)
