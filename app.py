"""Простий калькулятор суми двох чисел."""

def add(a, b):
    """Повертає суму аргументів a і b."""
    return a + b


def ask_number(prompt):
    """Запитує число, доки користувач не введе коректне значення."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: введіть число, будь ласка.")


def main():
    a = ask_number("Введіть перше число: ")
    b = ask_number("Введіть друге число: ")
    print(f"Сума: {add(a, b):g}")


if __name__ == "__main__":
    main()