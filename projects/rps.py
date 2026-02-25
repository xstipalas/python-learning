import random
from typing import List

class RPS:
    '''
    Игра "Камень, Ножницы, Бумага" с запоминанием ходов игрока и адаптацией стратегии компьютера.
     - Компьютер запоминает последние 100 ходов игрока и адаптирует свою стратегию, выбирая ход, который чаще всего побеждает последний ход игрока.
     - Игра поддерживает два языка: английский и русский. Все сообщения и выборы отображаются на выбранном языке.
     - Статистика игры отображает количество сыгранных игр и количество побед игрока.
    '''
    LOCAL = {
        'en': {
            'choices': {'rock': 0, 'paper': 1, 'scissors': 2},
            'invalid': 'Invalid choice. Please choose "rock", "paper", or "scissors".',
            'tie': 'Its a tie! Both chose {}.',
            'win': 'You win! {} beats {}.',
            'lose': 'You lose! {} beats {}.',
            'stat': 'Games played: {}, Wins: {}',

        },

        'ru': {
            'choices': {'камень': 0, 'бумага': 1, 'ножницы': 2},
            'invalid': 'Неверный выбор. Пожалуйста, выберите "камень", "бумага" или "ножницы".',
            'tie': 'Ничья! Оба выбрали {}.',
            'win': 'Вы выиграли! {} побеждает {}.',
            'lose': 'Вы проиграли! {} побеждает {}.',
            'stat': 'Игр сыграно: {}, Побед: {}',
        },
    }

    def __init__(self, language: str = 'en'):
        self.language = language
        self.games = 0
        self.wins = 0
        self.logs = []

        self.__choices = self.LOCAL[self.language]['choices']
        self.__cache = list(self.choices)


    def play(self, player_choice: str) -> str:
        '''
        Раунд игры.

        Args:
            player_choice (str): Выбор игрока

        Returns:
            str: Результат раунда
        '''

        if player_choice not in self.choices:
            return self.LOCAL[self.language]['invalid']
            
        computer_choice = random.choice(self.__cache)
        self.games += 1

        self.__cache.append(self.choices[(self.__choices[player_choice] + 1) % len(self.choices)])
        self.logs.append((player_choice, computer_choice))

        self.optimize_cache()

        if player_choice == computer_choice:
            return self.LOCAL[self.language]['tie'].format(player_choice)
        elif (self.__choices[player_choice] == 0 and self.__choices[computer_choice] == 2) or \
             (self.__choices[player_choice] == 1 and self.__choices[computer_choice] == 0) or \
             (self.__choices[player_choice] == 2 and self.__choices[computer_choice] == 1):
            self.wins += 1
            return self.LOCAL[self.language]['win'].format(player_choice, computer_choice)
        else:
            return self.LOCAL[self.language]['lose'].format(computer_choice, player_choice)

    def optimize_cache(self) -> None:
        '''Оптимизация кеша ходов.'''

        if len(self.__cache) > 100:
            self.__cache = self.__cache[-50:]

    @property
    def stat(self) -> str:
        '''Статистика игры.'''

        return self.LOCAL[self.language]['stat'].format(self.games, self.wins)
    
    @property
    def choices(self) -> List[str]:
        '''Возвращает список доступных выборов.'''

        return list(self.__choices.keys())

if __name__ == "__main__":
    game = RPS(language='ru')
    
    for _ in range(50):
        choice = random.choice(game.choices)
        print(game.play(choice))

    print(game.stat)
    print("Game logs:", *game.logs, sep="\n")