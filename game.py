import random
import os


class ScoreBoard:
    def __init__(self, filename="score.txt"):
        self.filename = filename
        self.player_wins = 0
        self.computer_wins = 0
        self.ties = 0
        self._load_score()

    def _load_score(self):
        """Загружает счет из файла, если он существует."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    if len(lines) >= 3:
                        self.player_wins = int(lines[0].strip())
                        self.computer_wins = int(lines[1].strip())
                        self.ties = int(lines[2].strip())
            except (ValueError, IOError):
                # Если файл поврежден, начинаем с нуля
                pass

    def update_score(self, result):
        """Обновляет счетчики в зависимости от результата раунда."""
        if result == "Вы победили!":
            self.player_wins += 1
        elif result == "Компьютер победил!":
            self.computer_wins += 1
        else:
            self.ties += 1
        self._save_score()

    def _save_score(self):
        """Сохраняет текущий счет в файл."""
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write(f"{self.player_wins}\n{self.computer_wins}\n{self.ties}\n")

    def display_score(self):
        """Выводит текущий счет на экран."""
        print("\n" + "=" * 25)
        print(f"🏆 СЧЕТ: Игрок {self.player_wins} | Компьютер {self.computer_wins} | Ничьи {self.ties}")
        print("=" * 25 + "\n")


def get_user_choice():
    """Получает и проверяет выбор пользователя."""
    valid_choices = ['камень', 'ножницы', 'бумага']
    while True:
        choice = input("Ваш выбор (камень, ножницы, бумага) или 'выход': ").lower().strip()

        if choice == 'выход':
            return 'выход'

        if choice in valid_choices:
            return choice

        print("⚠️ Ошибка! Пожалуйста, введите 'камень', 'ножницы' или 'бумага'.")


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
    print("\n" + "=" * 45)
    print("🎮 Добро пожаловать в игру 'Камень, Ножницы, Бумага'!")
    print("=" * 45)

    # Инициализируем систему подсчета очков
    scoreboard = ScoreBoard()
    scoreboard.display_score()

    while True:
        print("-" * 45)
        user_choice = get_user_choice()

        if user_choice == 'выход':
            print("\n👋 Спасибо за игру! До свидания!")
            break

        computer_choice = get_computer_choice()

        print(f"\n👤 Ваш выбор: {user_choice}")
        print(f"🤖 Выбор компьютера: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(f"🎯 Результат: {result}")

        # Обновляем и показываем счет
        scoreboard.update_score(result)
        scoreboard.display_score()


if __name__ == "__main__":
    main()