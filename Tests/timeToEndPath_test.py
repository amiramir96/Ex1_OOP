from unittest import TestCase
from Ex1Objects import CallForElevator
from Ex1Objects import Elevator
from Brain import genericHelpFuncs


class timeToEndPath_test(TestCase):
    # CallForElevator(time, src, dest, state, allocatedTo, id)
    # Elevator(id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime)
    c0 = CallForElevator.CallForElevator(12.0, 1, 2, 0, -1, 0)
    c1 = CallForElevator.CallForElevator(25.2, 0, -1, 0, -1, 1)
    c2 = CallForElevator.CallForElevator(30.83, -2, 8, 0, -1, 2)
    c3 = CallForElevator.CallForElevator(45.44, 7, 10, 0, -1, 3)
    c4 = CallForElevator.CallForElevator(51.53, 9, 4, 0, -1, 4)
    c5 = CallForElevator.CallForElevator(59.61, 5, 0, 0, -1, 5)
    e0 = Elevator.Elevator(0, 1, -2, 10, 3, 3, 2, 2)
    e2 = Elevator.Elevator(2, 2.5, -10, 100, 2, 2, 1, 1)

    def test_time_to_end_path(self):
        self.assertEqual(genericHelpFuncs.timeToEndPath(12.0, self.c0.getSrc(), self.c0.getDest(), self.e0), 34.0, "bad0")
        self.assertEqual(genericHelpFuncs.timeToEndPath(12.0, self.c0.getSrc(), self.c0.getDest(), self.e2), 24.8, "bad0.1")
        self.assertAlmostEqual(genericHelpFuncs.timeToEndPath(25.2, self.c1.getSrc(), self.c1.getDest(), self.e2), 37.6, None, "bad1", 0.1)
        self.assertAlmostEqual(genericHelpFuncs.timeToEndPath(30.83, self.c2.getSrc(), self.c2.getDest(), self.e2), 47.62, None, "bad2", 0.1)
        self.assertEqual(genericHelpFuncs.timeToEndPath(45.44, self.c3.getSrc(), self.c3.getDest(), self.e2), 61.44, "bad3")
        self.assertEqual(genericHelpFuncs.timeToEndPath(51.53, self.c4.getSrc(), self.c4.getDest(), self.e2), 69.13, "bad4")
        self.assertEqual(genericHelpFuncs.timeToEndPath(59.61, self.c5.getSrc(), self.c5.getDest(), self.e2), 75.61, "bad5")
