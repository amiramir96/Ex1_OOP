from unittest import TestCase

from Ex1Objects import Building
from Ex1Objects import CallForElevator
from Ex1Objects import Elevator
from Brain.TimeAndPathFuncs import is_slow


class IsSlow_test(TestCase):
    # CallForElevator(time, src, dest, state, allocatedTo, id)
    # Elevator(id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime)
    c0 = CallForElevator.CallForElevator(12.0, 1, 2, 0, -1, 0)
    c1 = CallForElevator.CallForElevator(25.2, 0, -1, 0, -1, 1)
    c2 = CallForElevator.CallForElevator(30.83, -2, 8, 0, -1, 2)
    c3 = CallForElevator.CallForElevator(45.44, 7, 10, 0, -1, 3)
    c4 = CallForElevator.CallForElevator(51.53, 9, 4, 0, -1, 4)
    c5 = CallForElevator.CallForElevator(59.61, 5, 0, 0, -1, 5)
    listC1 = [c0]
    listC2 = [c0, c1, c2, c3, c4, c5]
    listC3 = [c0, c4, c5]
    e0 = Elevator.Elevator(0, 1, -2, 10, 3, 3, 2, 2)
    e1 = Elevator.Elevator(1, 1.5, -5, 50, 2, 2, 1, 1)
    e2 = Elevator.Elevator(2, 2.5, -10, 100, 2, 2, 1, 1)
    e3 = Elevator.Elevator(3, 1, -4, 20, 3, 3, 2, 2)
    listE1 = [e0]
    listE2 = [e0, e1, e2, e3]
    listE3 = [e1, e2]
    building1 = Building.Building(-2, 10, listE1, listC1)
    building2 = Building.Building(-2, 10, listE2, listC2)

    def test_is_slow(self):
        self.assertTrue(is_slow(self.building1, self.e0), "failed b1 e0")
        self.assertFalse(is_slow(self.building1, self.e1), "failed b1 e1")
        self.assertFalse(is_slow(self.building1, self.e2), "failed b1 e2")
        self.assertTrue(is_slow(self.building1, self.e3), "failed b1 e3")
        self.assertTrue(is_slow(self.building2, self.e0), "failed b2 e0")
        self.assertTrue(is_slow(self.building2, self.e1), "failed b2 e1")
        self.assertFalse(is_slow(self.building2, self.e2), "failed b2 e2")
        self.assertTrue(is_slow(self.building2, self.e3), "failed b2 e3")
