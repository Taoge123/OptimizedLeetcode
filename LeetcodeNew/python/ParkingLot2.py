from typing import List
import collections
from enum import Enum
from abc import ABC, abstractmethod
import datetime
import threading


class VehicleType(Enum):
    CAR, ELECTRIC, TRUCK, MOTOR = 1, 2, 3, 4

    def getSize(self):
        return self.value

class SpotType(Enum):
    MOTOR, MEDIUM, LARGE, ELECTRIC = 1, 2, 3, 4

    def getSize(self):
        return self.value

    def __lt__(self, other):
        return self.getSize() <= other.getSize()


class Vehicle(ABC):
    def __init__(self, type, plate=None, spot=None, ticket=None):
        self.__type = type
        self.__plate = plate
        self.__spot = spot
        self.__ticket = ticket

    def canfit(self, spot):
        return self.__type.getSize() <= spot.getType().getSize()

    def assignSpot(self, spot):
        if not self.canfit(spot):
            return False
        self.__spot = spot
        spot.assignVehicle(self)
        return True

    def removeSpot(self):
        self.__spot.freeSpot()
        self.__spot = None
        self.__ticket.setEndTime = datetime.datetime.now()
        return True


class Car(Vehicle):
    def __init__(self, type, plate=None, spot=None, ticket=None):
        super(Car, self).__init__(VehicleType.CAR, plate, spot, ticket)


class Spot(ABC):
    def __init__(self, level, id, type):
        self.__level = level
        self.__id = id
        self.__type = type
        self.__vehicle = None

    def assignVehicle(self, vehicle):
        self.__vehicle = vehicle

    def freeSpot(self):
        self.__vehicle = None
        self.__level.freeSpot()


class MediumSpot(Spot):
    def __init__(self, level, id):
        super(MediumSpot, self).__init__(level, id, SpotType.MEDIUM)


class Level:
    def __init__(self, id):
        self.__id = id
        self.__spots = []
        self.__active_spots = collections.defaultdict(set)
        self.__available = 0

    def isFull(self):
        return self.__available == 0

    def addSpot(self, spot):
        self.__spots.append(spot)
        self.__active_spots[spot.getType()].add(spot)
        self.__available += 1

    def assignVehicle(self, vehicle):
        if self.isFull():
            return False

        for k in sorted(self.__active_spots.keys()):
            if k.getSize() < vehicle.getType().getSize():
                continue
            if len(self.__active_spots[k]) > 0:
                spot = self.__active_spots[k].pop()
                vehicle.assignSpot(spot)
                self.__available -= 1
                return True

        return False

    def freeSpot(self, spot):
        self.__active_spots[spot.getType()].add(spot)
        self.__available += 1


class Lot:
    _instance = None

    class __OnlyOne:
        def __init__(self, id, address):
            self.__id = id
            self.__address = address
            self.__entrance = []  # Entrance()
            self.__exit = []  # Exit()
            self.__lock = threading.Lock()
            self.__floors = []


    def __init__(self, id, address):
        if not Lot._instance:
            Lot._instance = Lot.__OnlyOne(id, address)
        else:
            Lot._instance.__id = id
            Lot._instance.__address = address

    def __getattr__(self, item):
        return getattr(self._instance, item)

    def addFloor(self, floor):
        self.__floors.append(floor)

    def isfull(self):
        return all([f.isFull() for f in self.__floors])

    def assignVehicle(self):
        if self.isfull():
            return False

        self.__lock.acquire()
        for f in self.__floors:
            if f.assignVehicle(vehicle):
                vehicle.setTicket = Ticket()
                self.__lock.release()
                return True
        self.__lock.release()
        return False

    def removeVehicle(self, vehicle):
        vehicle.removeSpot()