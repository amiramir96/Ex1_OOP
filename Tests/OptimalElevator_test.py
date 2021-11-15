from unittest import TestCase
from Ex1Objects import CallForElevator
from Ex1Objects import Elevator
from Brain import BrainTeamAlgo


class OptimalElevator_test(TestCase):
    # CallForElevator(time, src, dest, state, allocatedTo, id)
    # Elevator(id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime)
    c0 = CallForElevator.CallForElevator(12.0, 1, 2, 0, -1, 0)
    c1 = CallForElevator.CallForElevator(25.2, 0, -1, 0, -1, 1)
    c2 = CallForElevator.CallForElevator(30.83, -2, 8, 0, -1, 2)
    c3 = CallForElevator.CallForElevator(45.44, 7, 10, 0, -1, 3)
    c4 = CallForElevator.CallForElevator(51.53, 9, 4, 0, -1, 4)
    c5 = CallForElevator.CallForElevator(59.61, 5, 0, 0, -1, 5)
    e0 = Elevator.Elevator(0, 1, -2, 10, 3, 3, 2, 2)
    e1 = Elevator.Elevator(1, 1.5, -5, 50, 2, 2, 1, 1)
    e2 = Elevator.Elevator(2, 2.5, -10, 100, 2, 2, 1, 1)
    e3 = Elevator.Elevator(3, 1, -4, 20, 3, 3, 2, 2)
    listE1 = [e0]
    listE2 = [e0, e1, e2, e3]
    listE3 = [e1, e2]

    def test_optimal_elevator(self):
        self.assertEqual(BrainTeamAlgo.optimal_elevator(self.listE1, self.c0), [self.e0, 34.0], "bad0")
        self.assertEqual(BrainTeamAlgo.optimal_elevator(self.listE2, self.c0), [self.e2, 24.8], "bad0.1")
        self.assertAlmostEqual(BrainTeamAlgo.optimal_elevator(self.listE2, self.c1), [self.e2, 37.599999999999994], None, "bad1", 0.1)
        self.assertAlmostEqual(BrainTeamAlgo.optimal_elevator(self.listE2, self.c2), [self.e2, 47.629999999999995], None, "bad2", 0.1)
        self.assertEqual(BrainTeamAlgo.optimal_elevator(self.listE3, self.c3), [self.e2, 61.44], "bad3")
        self.assertEqual(BrainTeamAlgo.optimal_elevator(self.listE3, self.c4), [self.e2, 69.13], "bad4")
        self.assertEqual(BrainTeamAlgo.optimal_elevator(self.listE3, self.c5), [self.e2, 75.61], "bad5")
