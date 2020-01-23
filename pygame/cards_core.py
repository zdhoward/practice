#!/usr/bin/env python3


class Card:
    def __init__(self, _number, _suit=None):
        self.number = _number
        self.suit = _suit

    def __str__(self):
        if self.suit:
            return "{} of {}".format(self.number, self.suit)
        return str(self.number)

    def get(self):
        return self.number, self.suit


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
                    cards.append(Card(self._named_cards[num], suit))
                else:
                    cards.append(Card(num, suit))

        for extra in self.extra_cards:
            cards.append(Card(extra))
        return cards

    def show_cards(self):
        card_str = ""
        for card in self.cards:
            card_str += str(card) + "\n"
        return card_str

    def __str__(self):
        return self.show_cards()


def main():
    deck = Deck()
    print(deck)


if __name__ == "__main__":
    main()
