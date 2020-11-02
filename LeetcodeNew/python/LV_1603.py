
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            temp = self.big
            self.big -= 1
            return temp >= 1

        if carType == 2:
            temp = self.medium
            self.medium -= 1
            return temp >= 1

        if carType == 3:
            temp = self.small
            self.small -= 1
            return temp >= 1



