class MatrixOperations:
    def __init__(self):
        self.matrix1 = []
        self.matrix2 = []

    def input_matrices(self):
        pass  # Заглушка для ввода матриц

    def add_matrices(self, matrix1, matrix2):
        return "образец"  # Заглушка для сложения матриц

    def calculate_determinant(self, matrix):
        return "образец"  # Заглушка для вычисления определителя

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
            elif choice == '2':
                self.add_matrices(self.matrix1, self.matrix2)  # Временные пустые матрицы
            elif choice == '3':
                self.calculate_determinant(self.matrix1)  # Временная пустая матрица

if __name__ == "__main__":
    matrix_ops = MatrixOperations()
    matrix_ops.main_menu()
