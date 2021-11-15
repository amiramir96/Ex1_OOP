from unittest import TestCase
from Ex1Objects import Building
from Ex1Objects import CallForElevator
from Ex1Objects import Elevator
from Brain import BrainTeamAlgo


class howManyStops_test(TestCase):
    # CallForElevator(time, src, dest, state, allocatedTo, id)
    # Elevator(id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime)
    c0 = CallForElevator.CallForElevator(12.0, 1, 2, 0, -1, 0)
    c1 = CallForElevator.CallForElevator(25.2, 0, -1, 0, -1, 1)
    c2 = CallForElevator.CallForElevator(30.83, -2, 8, 0, -1, 2)
    c3 = CallForElevator.CallForElevator(45.44, 7, 10, 0, -1, 3)
    c4 = CallForElevator.CallForElevator(51.53, 9, 4, 0, -1, 4)
    c5 = CallForElevator.CallForElevator(59.61, 5, 0, 0, -1, 5)
    c6 = CallForElevator.CallForElevator(60.61, 5, 1, 0, -1, 5)
    listC1 = [c0]
    listC2 = [c0, c1, c2, c3, c4, c5]
    listC3 = [c0, c4, c5]
    listC4 = [c2, c5, c6, c0]
    e0 = Elevator.Elevator(0, 1, -2, 10, 3, 3, 2, 2)
    e1 = Elevator.Elevator(1, 1.5, -5, 50, 2, 2, 1, 1)
    e2 = Elevator.Elevator(2, 2.5, -10, 100, 2, 2, 1, 1)
    e3 = Elevator.Elevator(3, 1, -4, 20, 3, 3, 2, 2)
    listE1 = [e0]
    listE2 = [e0, e1, e2, e3]
    listE3 = [e1, e2]
    building1 = Building.Building(-2, 10, listE1, listC1)
    building2 = Building.Building(-2, 10, listE2, listC2)
    building3 = Building.Building(-2, 10, listE3, listC3)

    def test_how_many_stops(self):
        self.assertEqual(BrainTeamAlgo.howManyStops(self.listC1), 0, "bad1")
        self.assertEqual(BrainTeamAlgo.howManyStops(self.listC2), 9, "bad2")
        self.assertEqual(BrainTeamAlgo.howManyStops(self.listC3), 4, "bad3")
        self.assertEqual(BrainTeamAlgo.howManyStops(self.listC4), 4, "bad4")


