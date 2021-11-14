from unittest import TestCase
from Ex1Objects import Building
from Ex1Objects import CallForElevator
from Ex1Objects import Elevator
from Brain import genericHelpFuncs


class containedCalls_test(TestCase):
    # CallForElevator(time, src, dest, state, allocatedTo, id)
    # Elevator(id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime)
    c0 = CallForElevator.CallForElevator(10.83, -2, 10, 0, -1, 0)
    c1 = CallForElevator.CallForElevator(11.2, 0, -1, 0, -1, 1)
    c2 = CallForElevator.CallForElevator(15.0, 1, 2, 0, -1, 2)
    c3 = CallForElevator.CallForElevator(18.44, 7, 10, 0, -1, 3)

    c4 = CallForElevator.CallForElevator(51.53, 6, -2, 0, -1, 4)
    c5 = CallForElevator.CallForElevator(59.61, 5, -1, 0, -1, 5)
    c6 = CallForElevator.CallForElevator(60.61, 5, 1, 0, -1, 6)
    c11 = CallForElevator.CallForElevator(63.2, 0, -1, 0, -1, 11)
    listC1 = [c0]
    listC2 = [c0, c1, c2, c3, c4, c5, c6, c11]
    listC3 = [c4, c5, c6, c11]
    e0 = Elevator.Elevator(0, 1, -2, 10, 3, 3, 2, 2)
    e1 = Elevator.Elevator(1, 1.5, -5, 50, 2, 2, 1, 1)
    listE1 = [e0, e1]
    building1 = Building.Building(-2, 10, listE1, listC1)

    def test_contained_calls(self):
        self.assertEqual(genericHelpFuncs.containedCalls(self.building1, self.listC1, self.c0, self.e0, 44.83),
                         [self.c0],"second check is failed, something goes wrong with bdikat Shfiut")
        self.assertEqual(genericHelpFuncs.containedCalls(self.building1, self.listC2, self.c0, self.e0, 44.83),
                         [self.c0, self.c2, self.c3],"second check is failed, something goes wrong with upper path")
        self.assertEqual(genericHelpFuncs.containedCalls(self.building1, self.listC2, self.c4, self.e0, 72.86),
                         [self.c4, self.c5, self.c6, self.c11],"third check is failed, something goes wrong with down path")
