from enum import Enum
import random
from abc import ABC, abstractmethod

class CardSuit(Enum):
    SPADE, HEART, DIAMOND, CLUB = 1,2,3,4


class CardPoint(Enum):
    CA, C2, C3, C4, C5, C6, C7, C8, C9, C10, CJ, CQ, CK = 1,2,3,4,5,6,7,8,9,10,11,12,13


class Card:
    def __init__(self, suit, point):
        self.__suit = suit
        self.__point = point

    def getSuit(self):
        return self.__suit

    def getPoint(self):
        return self.__point

    def getPoints(self):
        return max(10, self.__point.value())


class Deck:
    def __init__(self):
        self.createDeck()

    def createDeck(self):
        self.__cards = []
        for suit in CardSuit:
            for point in CardPoint:
                self.__cards.append(Card(suit, point))

        self.shuffle()

    def shuffle(self):
        self.__cards = random.shuffle(self.__cards)

    def getCard(self):
        self.__cards.pop()


class Player(ABC):
    def __init__(self, name):
        self.__name = name
        self.__cards = []

    @abstractmethod
    def canPlay(self):
        pass

    @abstractmethod
    def wantPlay(self):
        # strategy
        pass

    def getName(self):
        return self.__name

    def addCard(self, card):
        self.__cards.append(card)

    def getTotalPoints(self):
        min_, max_ = 0, 0
        for card in self.__cards:
            if card.getPoint().value == 1:
                min_ += 1
                max_ += 11
            else:
                min_ += card.getPoint().value
                max_ += card.getPoint().value
        return min_ if max_ > 21 else max_


class CardPlayer(Player):
    def canPlay(self):
        return self.getTotalPoints() < 21

    def wantPlay(self):
        return self.getTotalPoints() < 17

class Dealer(Player):
    def canPlay(self):
        return self.getTotalPoints() < 21

    def wantPlay(self):
        return True

class Move:
    def __init__(self, player, card):
        self.__player = player
        self.__card = card

    def getPlayer(self):
        return self.__player

    def getCard(self):
        return self.__card


class Game:
    def __init__(self, player: Player, dealer: Dealer):
        self.__dealer = dealer
        self.__player = player

        self.__moves = []
        self.__deck = Deck()

    def isEnd(self):
        return self.__player.canPlay() and self.__dealer.canPlay()

    def play(self):
        card = self.__deck.getCard()

        self.giveCard(self.__dealer)
        self.giveCard(self.__player)

        while self.__player.canPlay() and self.__player.wantPlay() and self.isEnd():
            self.giveCard(self.__player)

        if not self.isEnd():
            self.giveCard(self.__dealer, card)
            while self.__dealer.canPlay() and not self.isEnd():
                self.giveCard(self.__dealer)
        return self.showWinner()

    def giveCard(self, player, card=None):
        card = card or self.__deck.getCard()
        move = Move(player, card)
        self.__moves.append(move)
        player.addCard(card)


    def showWinner(self):
        if self.__player.getTotalPoints() >= 21:
            return self.__dealer
        elif self.__dealer.getTotalPoints() >= 21:
            return self.__player
        if self.__player.getTotalPoints() >= self.__dealer.getTotalPoints():
            return self.__dealer.getTotalPoints()
        return self.__player.getTotalPoints()



    def play(self):
        card = self.__deck.getCard()

        self.giveCard(self.__player)
        self.giveCard(self.__dealer)

        while self.__player.canPlay() and self.__player.wantPlay():
            self.giveCard(self.__player)

        if not self.isEnd():
            self.giveCard(self.__dealer, card)
            while self.__dealer.canPlay() and not self.isEnd:
                self.giveCard(self.__dealer)
        return self.showWinner()

    def give_card(self, player, card=None):
        card = card or self.__deck.getCard()
        player.addCard(card)
        move = Move(card, player)
        self.__moves.append(move)
        return

    def is_end(self):
        return self.__player.canPlay() and self.__dealer.canPlay()