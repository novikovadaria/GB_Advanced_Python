def triangle_type(a, b, c):
    # Проверка существования треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        return "Треугольник с такими сторонами не существует"

    # Определение типа треугольника
    if a != b and b != c and a != c:
        return "Треугольник разносторонний"
    elif a == b and b == c:
        return "Треугольник равносторонний"
    else:
        return "Треугольник равнобедренный"

# Примеры использования функции
print(triangle_type(3, 4, 5))  # Разносторонний
print(triangle_type(5, 5, 5))  # Равносторонний
print(triangle_type(5, 5, 3))  # Равнобедренный