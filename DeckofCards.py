# TODO: Create a deck of cards
# TODO: Draw five cards
# TODO: Count number of each suit in hand

from random import *

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        if self.suit == 'Hearts' or self.suit == 'Diamonds':
            self.color = 'Red'
        else:
            self.color = 'Black'

    def show(self):
        print('{} of {}'.format(self.value, self.suit))


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def show(self):
        for item in self.cards:
            card.show()

    def shuffle(self):
        for i in range(len(self.cards) -1, 0, -1):
            r = randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []

    def show(self):
        if len(self.cards) == 0:
            print('No cards in your hand!')
        else:
            for item in self.cards:
                item.show()

    def draw(self, deck, num):
        for item in range(num):
            self.cards.append(deck.draw())







deck = Deck()
deck.shuffle()

#card = deck.draw()
#card.show()

hand = Hand()
hand.show()
hand.draw(deck, 5)
hand.show()

