from typing import Optional, ClassVar, Any, Self

class PokerHand:
    ''' Набор карт '''
    
    RESULT: ClassVar[list[str]] = ["Loss", "Tie", "Win"]
    RANKS_ID: ClassVar[dict[str:int]] = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, 'T': 10,
        'J': 11,'Q': 12, 'K': 13, 'A': 14
        }
        
    def __init__(self, hand: str):
        ''' Инициилизация экземпляра '''
        self.hand = hand
        self.__ranks = self.get_ranks(hand)
        self.__suits = self.get_suits(hand)

        self.combination = None

    def is_flush(self) -> bool:
        ''' Все карты одной масти '''
        if len(self.__suits) == 1:
            self.combination = 'Flush'
            return True
        else:
            return False

    def is_straight(self) -> bool:
        ranks_set = set(self.__ranks)
        if max(ranks_set) - min(ranks_set) == 4 and len(ranks_set) == 5 or ranks_set == {14, 2, 3, 4, 5}:
            self.combination = 'Straight'
            return True
        else:
            return False

    def is_quads(self) -> bool:
        if max(self.__ranks.count(rank) for rank in set(self.__ranks)) == 4:
            self.combination = 'Quads'
            return True
        else:
            return False

    def is_fullhouse(self) -> bool:
        if len(set(self.__ranks)) == 2 and set(self.__ranks.count(rank) for rank in set(self.__ranks)) == {2, 3}:
            self.combination = 'Full House'
            return True
        else:
            return False

    def is_set(self) -> bool:
        if max(self.__ranks.count(rank) for rank in set(self.__ranks)) == 3:
            self.combination = 'Set'
            return True
        else:
            return False

    def is_two_pair(self) -> bool:
        if len(set(self.__ranks)) == 3 and max(self.__ranks.count(rank) for rank in set(self.__ranks)) == 2:
            self.combination = 'Two Pair'
            return True
        else:
            return False

    def is_pair(self) -> bool:
        if len(set(self.__ranks)) == 4 and max(self.__ranks.count(rank) for rank in set(self.__ranks)) == 2:
            self.combination = 'Pair'
            return True
        else:
            return False

    def combination_id(self) -> tuple[int]:
        if self.is_straight() and self.is_flush():
            return (8, max(self.__ranks))
        elif self.is_quads():
            return (7, max(set(self.__ranks), key=self.__ranks.count), max(rank for rank in set(self.__ranks) if self.__ranks.count(rank) == 1))
        elif self.is_fullhouse():
            return (6, max(set(self.__ranks), key=self.__ranks.count), min(set(self.__ranks), key=self.__ranks.count))
        elif self.is_flush():
            return (5, sorted(self.__ranks, reverse=True))
        elif self.is_straight():
            return (4, max(self.__ranks))
        elif self.is_set():
            return (3, max(set(self.__ranks), key=self.__ranks.count), sorted((rank for rank in set(self.__ranks) if self.__ranks.count(rank) == 1), reverse=True))
        elif self.is_two_pair():
            return (2, sorted((rank for rank in set(self.__ranks) if self.__ranks.count(rank) == 2), reverse=True), max(rank for rank in set(self.__ranks) if self.__ranks.count(rank) == 1))
        elif self.is_pair():
            return (1, max(set(self.__ranks), key=self.__ranks.count), sorted((rank for rank in set(self.__ranks) if self.__ranks.count(rank) == 1), reverse=True))
        else:
            return (0, sorted(self.__ranks, reverse=True))

    def compare_with(self, other: Self):
        if not isinstance(other, PokerHand):
            raise ValueError("Comparison is only supported between instances of PokerHand.")

        self_comb = self.combination_id()
        other_comb = other.combination_id()

        if self_comb > other_comb:
            return PokerHand.RESULT[2]  # Win
        elif self_comb < other_comb:
            return PokerHand.RESULT[0]  # Loss
        else:
            return PokerHand.RESULT[1]  # Tie

    def __str__(self) -> str:
        return self.hand

    def __repr__(self) -> str:
        return f'PokerHand(ranks={self.__ranks}, suits={self.__suits})'
    
    @classmethod
    def get_ranks(cls, hand: str) -> list[int]:
        return [cls.RANKS_ID[card[0]] for card in hand.split()]

    @staticmethod
    def get_suits(hand: str) -> set[str]:
        return set(card[1] for card in hand.split())
