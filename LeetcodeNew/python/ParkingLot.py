'''
Use case:
is the parking spot assigned by system or picked up by the customer through some app?
ticket fee by vehicle type or spot type?

'''

from enum import Enum
from abc import ABC, abstractmethod
import threading
import collections
import bisect
from datetime import datetime

class VehicleType(Enum):
    CAR, TRUCK, ELECTRIC, MOTORBIKE = 1, 2, 3, 4
    def size(self):
        return self.value

class ParkingSpotType(Enum):
    COMPACT, LARGE, MOTOR, ELECTRIC = 1, 2, 3, 4
    def size(self):
        return self.value

class AccountStatus(Enum):
    ACTIVE, BLOCKED = 1, 2


class ParkingTicketStatus(Enum):
    ACTIVE, PAID, LOST = 1, 2, 3


class Address:
    def __init__(self, street, city, state, zipcode, country):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode
        self.__country = country


class Person:
    def __init__(self, name, address, email, phone):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone


class Account:
    def __init__(self, username, password, person, status=AccountStatus.ACTIVE):
        self.__username = username
        self.__password = password
        self.__person = person
        self.__status = status

    def resetPassword(self):
        pass


class Admin(Account):
    def addParkingFloor(self, floor):
        pass

    def addParkingSpot(self, floor_name, spot):
        pass

    def addEntrancePanel(self, entrance_panel):
        pass

    def addExitPanel(self, exit_panel):
        pass


class ParkingAssistant(Account):
    def process_ticket(self, ticket):
        pass


class ParkingSpot(ABC):
    def __init__(self, parking_floor, number, parking_spot_type):
        self.__parking_floor = parking_floor
        self.__number = number
        self.__parking_spot_type = parking_spot_type
        self.__free = True
        self.__vehicle = None

    def isFree(self):
        return self.__free

    def assignVehicle(self, vehicle):
        self.__vehicle = vehicle
        self.__free = False

    def removeVehicle(self):
        self.__vehicle = None
        self.__free = True
        self.__parking_floor.freeSpot()

    def getType(self):
        return self.__parking_spot_type

    def __lt__(self, other):
        return self.__parking_spot_type.size() < other.__parking_spot_type.size()


class CompactSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.COMPACT)


class LargeSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.LARGE)


class MotorbikeSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.MOTORBIKE)


class ElectricSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.ELECTRIC)


class Vehicle(ABC):
    def __init__(self, license_number, vehicle_type, ticket=None):
        self.__license_number = license_number
        self.__vehicle_type = vehicle_type
        self.__ticket = ticket
        self.__spot = None

    def assignTicket(self, ticket):
        self.__ticket = ticket

    def IsFittedInSpot(self, spot: ParkingSpot) -> bool:
        return self.__vehicle_type.size() <= spot.getType().size()

    def getType(self):
        return self.__vehicle_type

    def assignSpot(self, spot: ParkingSpot):
        self.__spot = spot
        spot.assignVehicle(self)

    def removeSpot(self):
        self.__spot.removeVehicle()
        self.__spot = None
        self.__ticket.setEndTime(datetime.now())

class Car(Vehicle):
    def __init__(self, license_number, ticket=None):
        super().__init__(license_number, VehicleType.CAR, ticket)


class Van(Vehicle):
    def __init__(self, license_number, ticket=None):
        super().__init__(license_number, VehicleType.VAN, ticket)


class Truck(Vehicle):
    def __init__(self, license_number, ticket=None):
        super().__init__(license_number, VehicleType.TRUCK, ticket)


class ParkingFloor:
    def __init__(self, name):
        self.__name = name
        self.__spots_counter = collections.Counter()
        self.__spots = []
        self.__available = 0
        self.__ParkingLotStats = ParkingLotStats()


    def addParkingSpot(self, spot: ParkingSpot):
        self.__spots_counter[spot.getType()] += 1
        bisect.bisect_left(self.__spots, spot)
        self.__available += 1
        self.__ParkingLotStats.addSpot(spot)
        return


    def assignVehicle(self, vehicle: Vehicle) -> bool:
        if self.__available == 0 or sum([v for k, v in self.__spots_counter.items() if k.size() >= vehicle.getType().size()]) == 0:
            return False

        for spot in self.__spots:
            if vehicle.IsFittedInSpot(spot):
                self.__spots_counter[spot.getType()] -= 1
                vehicle.assignSpot(spot)
                self.__available -= 1
                self.__ParkingLotStats.fitinSpot(spot)

                return True


    def freeSpot(self, spot: ParkingSpot):
        self.__spots_counter[spot.getType()] += 1
        self.__available += 1


class ParkingRate:
    def __init__(self):
        self.__hours = None
        self.__rate = None


class ParkingLot:
    _instance = None
    class __OnlyOne:
        def __init__(self, name, address):
            self.__name = name
            self.__address = address
            self.__parking_rate = ParkingRate()
            self.__entrance_panels = {}
            self.__exit_panels = {}
            self.__active_tickets = {}
            self.__parking_floors = []
            self.__parking_lot_stats = ParkingLotStats()
            self.__lock = threading.Lock()

    def __init__(self, name: str, address: Address) -> None:
        if not ParkingLot.instance:
            ParkingLot._instance = ParkingLot.__OnlyOne(name, Address)
        else:
            ParkingLot.__name = name
            ParkingLot.__address = address

    def add_parking_floor(self, parking_floor: ParkingFloor):
        self.__parking_floors.append(parking_floor)

    def parkvehicle(self, vehicle: Vehicle):
        if self.__parking_lot_stats.isfull():
            raise Exception('Is full.')
        self.__lock.acquire()
        for parking_floor in self.__parking_floors:
            if parking_floor.assignVehicle(Vehicle):
                ticket = ParkingTicket()
                vehicle.assignTicket(ticket)
                ticket.type = vehicle.getType()
                ticket.save_in_db()
                self.__lock.release()
                return ticket
        self.__lock.release()
        raise Exception('Is full.')

    def releaseVehicle(self, vehicle):
        pass

class ParkingLotStats:
    _instance = None
    class __OnlyOne:
        def __init__(self):
            self.__spots_counter = collections.Counter()
            self.__available = 0
    def __init__(self):
        if ParkingLotStats._instance is None:
            ParkingLotStats._instance = ParkingLotStats.__OnlyOne()

    def addSpot(self, spot):
        self.__spots_counter[spot.getType()] += 1
        self.__available += 1

    def fitinSpot(self, spot):
        self.__spots_counter[spot.getType()] -= 1
        self.__available -= 1


    def isfull(self, vehicle):
        return self.__available == 0 or sum([v for k, v in self.__spots_counter.items() if k.size() >= vehicle.getType().size()]) == 0