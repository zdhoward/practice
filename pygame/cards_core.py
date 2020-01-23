#!/usr/bin/env python3
import random
import operator


class Card:
    def __init__(self, _number, _suit="None", _value=0):
        self.number = _number
        self.value = int(_value)
        self.suit = _suit

    def __str__(self):
        if self.suit:
            return "{} of {}".format(self.number, self.suit)
        return str(self.number)

    def get(self):
        return self.value, self.suit


class Deck:
    def __init__(
        self,
        _num_per_suit=13,
        _suits=["Hearts", "Spades", "Diamonds", "Clubs"],
        _named_cards={11: "Jack", 12: "Queen", 13: "King", 1: "Ace"},
        _extra_cards=["Joker", "Joker"],
    ):
        self.num_per_suit = _num_per_suit
        self.suits = _suits
        self.extra_cards = _extra_cards
        self._named_cards = _named_cards
        self.cards = self.generate_cards()

    def generate_cards(self):
        cards = []
        for suit in self.suits:
            for num in range(1, self.num_per_suit + 1):
                if num in self._named_cards.keys():
                    cards.append(Card(self._named_cards[num], suit, _value=num))
                else:
                    cards.append(Card(num, suit, _value=num))

        for extra in self.extra_cards:
            cards.append(Card(extra, _suit="Extra"))
        return cards

    def show_cards(self):
        card_str = ""
        for card in self.cards:
            card_str += str(card) + "\n"
        return card_str

    def __str__(self):
        return self.show_cards()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, _number=1):
        cards = []
        for num in range(_number):
            cards.append(self.cards.pop())
        return cards

    def burn(self, _number=1):
        for num in range(_number):
            self.cards.pop()

    def get(self):
        cards = []
        for card in self.cards:
            cards.append(card.get())
        return cards


class Hand:
    def __init__(self, _cards=[]):
        self.cards = _cards

    def __str__(self):
        return self.show()

    def __iadd__(self, _other):
        self.cards += _other
        return self

    def show(self):
        card_str = ""
        for card in self.cards:
            card_str += str(card) + "\n"
        return card_str

    def sort(self):
        self.cards = sorted(self.cards, key=operator.attrgetter("suit", "value"))

    def get(self):
        cards = []
        for card in self.cards:
            cards.append(card.get())
        return cards


def main():
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck.deal(7))
    print(hand)
    deck.burn(1)
    hand += deck.deal(4)
    # print(hand.show())
    hand.sort()
    print(hand)


if __name__ == "__main__":
    main()
