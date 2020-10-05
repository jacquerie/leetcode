# -*- coding: utf-8 -*-


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.availabities = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        self.availabities[carType - 1] -= 1
        return self.availabities[carType - 1] >= 0


if __name__ == '__main__':
    obj = ParkingSystem(1, 1, 0)
    assert obj.addCar(1)
    assert obj.addCar(2)
    assert not obj.addCar(3)
    assert not obj.addCar(1)
