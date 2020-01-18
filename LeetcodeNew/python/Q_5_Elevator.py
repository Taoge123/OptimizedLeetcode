'''
https://stackoverflow.com/questions/12009556/datastructure-for-elevator-mechanism

Below is one way to design Elevator System. Each elevator uses Queue (it could be Blocking Queue) to store floor requests. Also there is a central ElevatorManager which monitors all Elevator queues and it can delegate requests to a certain elevator depending upon some business rules. It's the job of ElevatorManager to efficiently delegate requests to the relevant elevator. Below pseudocode does not optimize the delegation algorithm but it shows how actual delegation could be done to a list of elevators.

Classes needed for Elevator System:

ElevatorManager [Singleton - This is the main elevator program which will manage n elevators in the building]
Members:
List of Elevator
Queue of Floor.Request // This maintains request for both directions. One improvement could be to keep two queues, one for each direction but it would increase complexity
MIN_FLOOR
MAX_FLOOR
Operations:
delgate()
halt() // set whole elevator system in maintenance mode or halt operation


Elevator [Represents individual elevators. There could be n elevators in a building]
Members:
Queue of Floor // this needs to be sorted so may be a PriorityQueue could be used
Direction : Enum [Enum of direction - up, down, wait, idle, maintenance]
CurrentFloor : Floor
Operations:
operate()
moveUp()
moveDown()
openDoor()
closeDoor()
callEmergencyLine()
getDirection()
getCurrentFloor()
setInMaintenanceMode()


Floor [Represents individual floors]
Members:
eNum of Floors
class Request {
currentFloor
destinationFloor
Direction [Up, Down]
}
Operation:
goUp()
goDown()
'''
from enum import Enum
from collections import deque
import bisect

class ElevatorManagerStatus(Enum):
    ACTIVE, HALT = 1,2


class Direction(Enum):
    UP, DOWN, IDLE = 1,2,3


class ElevatorManager:
    _instance = None

    class __OnlyOne:
        def __init__(self, minFloor=0, maxFloor=10):
            self.__elevators = []
            self.__requests = deque([])
            self.__minFloor = minFloor
            self.__maxFloor = maxFloor
            self.__status = ElevatorManagerStatus.ACTIVE

    def __init__(self, minFloor=0, maxFloor=10):
        if ElevatorManager._instance is None:
            ElevatorManager._instance = ElevatorManager.__OnlyOne(minFloor, maxFloor)
        else:
            ElevatorManager._instance.__minFloor = minFloor
            ElevatorManager._instance.____maxFloor = maxFloor

    def __getattr__(self, item):
        return getattr(self._instance, item)

    def ishalt(self):
        return self.__status == ElevatorManagerStatus.HALT

    def setHalt(self):
        self.__status = ElevatorManagerStatus.HALT

    def setActive(self):
        self.__status = ElevatorManagerStatus.ACTIVE

    def delegate(self):
        while not self.ishalt():
            if self.__requests:
                request = self.__requests.popleft()
                elevator = min(self.__elevators, key=lambda x: self.getDistance(x, request.currentFloor, request.direction))
                elevator.addRequest(request)

    def getDistance(self, elevator, currentFloor, direction):
        if elevator.diretion == Direction.IDLE:
            return abs(elevator.currentFloor - currentFloor)

        if elevator.diretion == direction == Direction.UP:
            diff = currentFloor - elevator.currentFloor
            if diff < 0:
                diff = - diff + self.__maxFloor - self.__minFloor + 1
            return diff

        if elevator.diretion == direction == Direction.DOWN:
            diff = -currentFloor + elevator.currentFloor
            if diff < 0:
                diff = - diff + self.__maxFloor - self.__minFloor + 1
            return diff

        if elevator.diretion == Direction.UP:
            return self.__maxFloor - elevator.currentFloor + 1 + currentFloor

        return -self.__minFloor + elevator.currentFloor + 1 + currentFloor


class Floor(Enum):
    ONE, TWO, THREE = 1,2,3

class Request:
    def __init__(self, currentFloor, destinationFloor, direction):
        self.currentFloor = currentFloor
        self.destinationFloor = destinationFloor
        self.direction = direction


class Elevator:
    def __init__(self):
        self.__floors = deque([])
        self.__distance = deque([])
        self.__direction = Direction.IDLE
        self.__currentFloor = Floor.ONE

    def operate(self):
        while self.__floors:
            if self.__direction == Direction.IDLE:
                self.__direction = self.__floors[0][1]

            while self.__currentFloor != self.__floors[0][0]:
                if self.__currentFloor == Floor.THREE:
                    self.__direction = Direction.DOWN
                elif self.__currentFloor == Floor.ONE:
                    self.__direction = Direction.UP

                if self.__direction == Direction.UP:
                    self.moveUp()
                else:
                    self.moveDown()
            floor, direction = self.__floors.popleft()
            self.__distance.popleft()
            self.openDoor()
            self.closeDoor()
            self.__direction = direction

        self.__direction = Direction.IDLE

    def addRequest(self, request):
        d1, d2 = ElevatorManager.getDistance(self, request.currentFloor, request.direction), \
                 ElevatorManager.getDistance(self, request.destinationFloor, request.direction)

        idx = bisect.bisect_left(self.__distance, d1)
        self.__distance.insert(idx, d1)
        self.__floors.insert(idx, (request.currentFloor, request.direction))
        idx2 = bisect.bisect_left(self.__distance, d1, idx)
        self.__distance.insert(idx2, d2)
        self.__floors.insert(idx2, (request.currentFloor, request.direction))

    def moveUp(self):
        self.__currentFloor += 1

    def moveDown(self):
        self.__currentFloor -= 1

    def openDoor(self):
        pass

    def closeDoor(self):
        pass

