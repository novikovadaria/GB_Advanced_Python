class Matrix:
    def __init__(self, matrix):
        # Проверим, что матрица задана правильно (все строки имеют одинаковую длину)
        if len(set(len(row) for row in matrix)) != 1:
            raise ValueError("Все строки матрицы должны иметь одинаковую длину")

        self.matrix = matrix

    def __str__(self):
        # Преобразуем матрицу в строку для вывода
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def __eq__(self, other):
        # Сравниваем две матрицы
        return self.matrix == other.matrix

    def __add__(self, other):
        # Сложение двух матриц
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Для сложения размеры матриц должны совпадать")

        result = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ]
        return Matrix(result)

    def __mul__(self, other):
        # Умножение двух матриц
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы")

        result = [
            [
                sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0])))
                for j in range(len(other.matrix[0]))
            ]
            for i in range(len(self.matrix))
        ]
        return Matrix(result)






