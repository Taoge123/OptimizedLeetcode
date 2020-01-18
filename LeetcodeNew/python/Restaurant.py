'''
Does the restaurant have many branches or only on location?
How many menus for one branch? like drinking menu, dinner menu? Or only one
Do we accept reservation, how will that work? send notification.
take out orders?
payments?
Is this for the dinning hall? Or we should consider chef too
For the same table, should we reserve the order for differents seats or they share different seat
Assume we will have manager, receptionist, cashier, waiter, chef
DO we need to consider tax and tip when checking out?


add/modify tables
search table
place/update/make a payment for an order
make/cancel reservation
check in
'''
from enum import Enum
from abc import ABC, abstractmethod

class ReservationStatus(Enum):
    REQUESTED, CONFIRMED, CANCELLED, CHECKED_IN, ABANDONED = 1,2,3,4,5


class PaymentStatus(Enum):
    UNPAID, PAIDED, FAILED = 1,2,3


class OrderStatus(Enum):
    RECEIVED, PREPARING, COMPLETE, CANCELED = 1,2,3,4

class TableStatus(Enum):
    FREE, OCCUPIED, RESERVED = 1,2,3

class AccountStatus(Enum):
    ACTIVE, BLACKLISTED, CLOSED = 1,2,3


class Address:
    def __init__(self, street, city, state, zipcode):
        pass


class Person(ABC):
    def __init__(self, name, address, phone, email):
        pass


class Account:
    def __init__(self, username, password, status=AccountStatus.ACTIVE):
        pass

class Guest(Person):
    pass


class Employee(ABC, Person):
    def __init__(self, name, address, phone, email, id, datejoined, account):
        pass

    @abstractmethod
    def employeeType(self):
        pass


class Receptionist(Employee):
    def create_reservation(self):
        pass
    def modify_reservation(self, reservation):
        pass
    def search_table(self, time, party):
        pass


class Manager(Employee):
    def add_employee(self):
        pass


class Chef(Employee):
    pass


class Restaurant:
    def __init__(self, id, address):
        self.__id = id
        self.__address = address
        self.__branches = []

    def addBranch(self, branch):
        pass


class Branch:
    def __init__(self, name, location):
        self.__name = name
        self.__location = location
        self.__tables = []
        self.__menue = None
        self.__kitchen = None

    def updateMenu(self, menu):
        pass

    def updateKitchen(self, kitchen):
        pass

    def addTable(self, table):
        self.__tables.append(table)

    def checkout(self, table):
        return table.checkout()

    def reserveTable(self, reservation):
        pass

    def walkin(self, party):
        for table in self.__tables:
            if table.__status == TableStatus.FREE and table.capacity >= party:
                table.__status = TableStatus.OCCUPIED
                return table
        raise Exception('No available')


class Table:
    def __init__(self, id, capacity, status=TableStatus.FREE):
        self.__id = id
        self.__capacity = capacity
        self.__status = status
        self.__reservations = []
        self.__order = None

    def iscurrentfree(self):
        return self.__status == TableStatus.FREE

    def searchAvailability(self, start, end):
        pass

    def updateOrder(self, order):
        if self.__order is None:
            self.__order = order
        else:
            if order is None:
                return
            self.__order.update(order)

    def checkout(self):
        checks = self.__order.checkout()
        self.__order = None
        self.__status = TableStatus.FREE
        return checks

class Reservation:
    def __init__(self, id, party, notes, guest, start, end):
        pass


class Menu:
    def __init__(self, id, title, description):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__menu_selections = []

    def addMenuSelection(self, menu_selection):
        self.__menu_selections.append(menu_selection)


class MenuSelection:
    def __init__(self, id, title, description):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__menu_items = []

    def addMenuItem(self, menu_item):
        self.__menu_items.append(menu_item)


class MenuItem:
    def __init__(self, id, title, description, price):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__price = price


class MealItem:
    def __init__(self, id, quantity, menu_item):
        self.__meal_item_id = id
        self.__quantity = quantity
        self.__menu_item = menu_item

    def update_quantity(self, quantity):
        pass


# 同一个桌大家分单
class Meal:
    def __init__(self, id, seat):
        self.__meal_id = id
        self.__seat = seat
        self.__meal_items = []

    def add_meal_item(self, meal_item):
        pass

    def remove_meal_item(self):
        pass

class Order:
    def __init__(self, id, status, table, waiter, chef):
        self.__order_id = id
        self.__OrderStatus = status
        self.__creation_time = datetime.datetime.now()

        self.__meals = []
        self.__table = table
        self.__waiter = waiter
        self.__chef = chef
        self.__start = datetime.now()
        self.__end = None

    def add_meal(self, meal):
        pass

    def remove_meal(self, meal):
        pass

    def get_status(self):
        return self.__OrderStatus

    def set_status(self, status):
        pass

    def checkout(self, tax):
        self.__OrderStatus = OrderStatus.COMPLETE
        return [Check(id=self.__order_id + meal.__id, amount=meal.quantity * meal.price, tax=tax) for meal in self.__meals]


class Check:
    def __init__(self, id, amount, tax):
        pass