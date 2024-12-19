import numpy as np

class MatrixOperations:
    def __init__(self):
        self.matrix1 = None
        self.matrix2 = None
        self.result_matrix = None
        self.determinant_matrix1 = None
        self.determinant_matrix2 = None

    def input_matrices(self):
        size = int(input("Введите размер матриц: "))
        matrix1 = []
        matrix2 = []

        print("Введите элементы первой матрицы:")
        for i in range(size):
            row = list(map(int, input().split()))
            if len(row) != size:
                print("Ошибка: количество элементов в строке должно быть равно размеру матрицы.")
                return None, None
            matrix1.append(row)

        print("Введите элементы второй матрицы:")
        for i in range(size):
            row = list(map(int, input().split()))
            if len(row) != size:
                print("Ошибка: количество элементов в строке должно быть равно размеру матрицы.")
                return None, None
            matrix2.append(row)

        self.matrix1 = np.array(matrix1)
        self.matrix2 = np.array(matrix2)

    def add_matrices(self):
        if self.matrix1 is not None and self.matrix2 is not None:
            self.result_matrix = self.matrix1 + self.matrix2
        else:
            print("Сначала введите матрицы.")

    def calculate_determinant(self):
        if self.matrix1 is not None:
            self.determinant_matrix1 = np.linalg.det(self.matrix1)
        if self.matrix2 is not None:
            self.determinant_matrix2 = np.linalg.det(self.matrix2)

    def main_menu(self):
        while True:
            print("1. Ввод исходных данных")
            print("2. Выполнение алгоритма")
            print("3. Вывод результата")
            print("4. Завершение работы программы")
            choice = input("Выберите пункт меню: ")

            if choice == '4':
                break
            elif choice == '1':
                self.input_matrices()
                if self.matrix1 is None or self.matrix2 is None:
                    print("Ошибка ввода матриц. Попробуйте снова.")
            elif choice == '2':
                self.add_matrices()
                self.calculate_determinant()
            elif choice == '3':
                if self.result_matrix is not None:
                    print("Сумма матриц:\n", self.result_matrix)
                    print("Определитель первой матрицы:", self.determinant_matrix1)
                    print("Определитель второй матрицы:", self.determinant_matrix2)
                else:
                    print("Сначала выполните алгоритм.")

if __name__ == "__main__":
    matrix_ops = MatrixOperations()
    matrix_ops.main_menu()
