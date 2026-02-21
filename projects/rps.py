import random

class Rps:
    def __init__(self, language='en'):
        self.language = language
        self.games = 0
        self.wins = 0
        self.logs = []

        if self.language == 'en':
            self.choices = ('rock', 'paper', 'scissors')
            self.__cache = ['rock', 'paper', 'scissors']
        elif self.language == 'ru':
            self.choices = ('камень', 'бумага', 'ножницы')
            self.__cache = ['камень', 'бумага', 'ножницы']

    def play(self, player_choice):
        if player_choice not in self.choices:
            if self.language == 'en':
                return "Invalid choice. Please choose 'rock', 'paper', or 'scissors'."
            elif self.language == 'ru':
                return "Неверный выбор. Пожалуйста, выберите 'камень', 'бумага' или 'ножницы'."
            
        computer_choice = random.choice(self.__cache)
        self.games += 1

        self.__cache.append(self.choices[(self.choices.index(player_choice) + 1) % len(self.choices)])
        self.logs.append((player_choice, computer_choice))

        self.optimize_cache()

        if self.language == 'en':
            if player_choice == computer_choice:
                return f"It's a tie! Both chose {player_choice}."
            elif (player_choice == 'rock' and computer_choice == 'scissors') or \
                 (player_choice == 'paper' and computer_choice == 'rock') or \
                 (player_choice == 'scissors' and computer_choice == 'paper'):
                self.wins += 1

                return f"You win! {player_choice} beats {computer_choice}."
            else:
                return f"You lose! {computer_choice} beats {player_choice}."
        elif self.language == 'ru':
            if player_choice == computer_choice:
                return f"Ничья! Оба выбрали {player_choice}."
            elif (player_choice == 'камень' and computer_choice == 'ножницы') or \
                 (player_choice == 'бумага' and computer_choice == 'камень') or \
                 (player_choice == 'ножницы' and computer_choice == 'бумага'):
                self.wins += 1

                return f"Вы выиграли! {player_choice} побеждает {computer_choice}."
            else:
                return f"Вы проиграли! {computer_choice} побеждает {player_choice}."

    def optimize_cache(self):
        if len(self.__cache) > 10:
            self.__cache = self.__cache[-5:]

    def stat(self):
        if self.language == 'en':
            return f"Games played: {self.games}, Wins: {self.wins}"
        elif self.language == 'ru':
            return f"Игр сыграно: {self.games}, Побед: {self.wins}"

if __name__ == "__main__":
    game = Rps(language='ru')
    
    for _ in range(50):
        choice = random.choice(game.choices)
        print(game.play(choice))

    print(game.stat())
    print("Game logs:", *game.logs, sep="\n")