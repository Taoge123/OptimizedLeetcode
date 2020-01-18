from abc import abstractmethod, ABC
from enum import Enum
from collections import Counter


class ProductType(Enum):
    COKE = 1


class State(ABC):
    def __init__(self, vendingMachine):
        self.__vendingMachine = vendingMachine

    @abstractmethod
    def selectItem(self, item: Product):
        pass

    @abstractmethod
    def insertPayment(self, value: int):
        pass

    @abstractmethod
    def executeTransaction(self):
        pass

    @abstractmethod
    def cancelTransaction(self):
        pass

    @abstractmethod
    def name(self):
        pass


class NoSelectionState(State):
    def selectItem(self, item: Product):
        self.__vendingMachine.addSelectedItem(item)
        self.__vendingMachine.changeToHasSelectionState()

    def insertPayment(self, value: int):
        raise Exception('No selected item.')

    def executeTransaction(self):
        raise Exception('No selected item.')

    def cancelTransaction(self):
        return 0

    def name(self):
        return 'No selection'


class HasSelectionState(State):
    def selectItem(self, item: Product):
        raise Exception('Has selected item.')

    def insertPayment(self, value: int):
        self.__vendingMachine.addMoney(value)
        self.__vendingMachine.changeToInsertMoneyState()

    def executeTransaction(self):
        raise Exception('No payment made')

    def cancelTransaction(self):
        self.__vendingMachine.changeToNoSelectionState()
        self.__vendingMachine.cancelSelectedItem()
        return 0

    def name(self):
        return 'Has selection'


class InsertMoneyState(State):
    def selectItem(self, item: Product):
        raise Exception('Has selected item.')

    def insertPayment(self, value: int):
        self.__vendingMachine.addMoney(value)

    def executeTransaction(self):
        diff = self.__vendingMachine.getInsertedMoney() - self.__vendingMachine.getPrice()
        if diff >= 0:
            self.__vendingMachine.setSelectedItem(None)
            self.__vendingMachine.changeToNoSelectionState()
        else:
            raise Exception('Not enough')

    def cancelTransaction(self):
        money = self.__vendingMachine.getInsertedMoney()
        self.__vendingMachine.changeToNoSelectionState()
        self.__vendingMachine.cancelSelectedItem()
        return money

    def name(self):
        return 'Has selection'

class Product(ABC):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def updatePrice(self, price):
        self.__price = price


class Coke(Product):
    def __init__(self, price):
        super(Coke, self).__init__(ProductType.COKE, price)


class VendingMachine:
    def __init__(self):
        self.__inventory = Counter()
        self.__selectedItem = None

        self.__noSelectionState = NoSelectionState(self)
        self.__hasSelectionState = HasSelectionState(self)
        self.__insertPaymentState = InsertPaymentState(self)

        self.__state = self.__noSelectionState
        self.__currentMoney = 0


    def getMoney(self):
        return self.__currentMoney

    def addMoney(self, value):
        self.__currentMoney += value

    def clearMoney(self):
        self.__currentMoney = None

    def addInventory(self, product, quantity):
        self.__inventory[product] += quantity

    def getPrice(self):
        if self.__selectedItem is None:
            return 0
        return self.__selectedItem.getPrice()

    def setSelectedItem(self, item):
        self.__selectedItem = item

    def addSelectedItem(self, item):
        if self.__inventory[item] == 0:
            raise Exception('')

        self.__inventory[item] -= 1
        self.__selectedItem = item

    def cancelSelectedItem(self):
        item = self.__selectedItem
        self.__inventory[item] += 1
        self.__selectedItem = None
        self.__currentMoney = 0

    def changeToNoSelectionState(self):
        self.__state = self.__noSelectionState

    def changeToHasSelectionState(self):
        self.__state = self.__hasSelectionState

    def changeToInsertPaymentState(self):
        self.__state = self.__insertPaymentState

    def selectItem(self, item: Product):
        self.__state.selectItem(item)

    def insertPayment(self, value: int):
        self.__state.insertPayment(value)

    def executeTransaction(self):
        self.__state.executeTransaction()

    def cancelTransaction(self):
        self.__state.cancelTransaction()
