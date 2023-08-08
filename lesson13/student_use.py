from student import Student

# Пример использования:
student = Student("Алексей Петров", "subjects.csv")
student.add_score("Математика", 5)
student.add_test_result("Математика", 95)
print(student.average_test_score("Математика"))
print(student.average_score())