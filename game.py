import random


def get_user_choice():
    """Получает и проверяет выбор пользователя."""
    valid_choices = ['камень', 'ножницы', 'бумага']
    while True:
        choice = input("Введите ваш выбор (камень, ножницы, бумага) или 'выход' для завершения: ").lower().strip()

        # Возможность выхода из игры
        if choice == 'выход':
            return 'выход'

        # Проверка корректности ввода
        if choice in valid_choices:
            return choice

        print("Ошибка! Пожалуйста, введите 'камень', 'ножницы' или 'бумага'.")


def get_computer_choice():
    """Генерирует случайный выбор компьютера."""
    choices = ['камень', 'ножницы', 'бумага']
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    """Определяет победителя."""
    if user_choice == computer_choice:
        return "Ничья!"

    winning_combinations = {
        'камень': 'ножницы',
        'ножницы': 'бумага',
        'бумага': 'камень'
    }

    if winning_combinations[user_choice] == computer_choice:
        return "Вы победили!"
    else:
        return "Компьютер победил!"


def main():
    """Главная функция запуска игры (основной игровой цикл)."""
    print("=" * 45)
    print("Добро пожаловать в игру 'Камень, Ножницы, Бумага'!")
    print("=" * 45)

    while True:
        print("\n" + "-" * 45)
        user_choice = get_user_choice()

        # Выход из основного цикла
        if user_choice == 'выход':
            print("\nСпасибо за игру! До свидания!")
            break

        computer_choice = get_computer_choice()

        print(f"Ваш выбор: {user_choice}")
        print(f"Выбор компьютера: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(f"Результат: {result}")


if __name__ == "__main__":
    main()