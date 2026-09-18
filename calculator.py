# calculator.py — Простой мини-калькулятор на Python

def add(x, y):
    """Функция сложения"""
    return x + y

def subtract(x, y):
    """Функция вычитания"""
    return x - y

def multiply(x, y):
    """Функция умножения"""
    return x * y

def divide(x, y):
    """Функция деления с защитой от деления на ноль"""
    if y == 0:
        return "Ошибка: Деление на ноль невозможно!"
    return x / y

def main():
    print("=== Простой калькулятор ===")
    print("Доступные операции:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")

    choice = input("Выберите номер операции (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: Вводите только числа!")
            return

        if choice == '1':
            print(f"Результат: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Результат: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Результат: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Результат: {num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Неверный ввод операции.")

if __name__ == "__main__":
    main()