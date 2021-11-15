from unittest import TestCase
from Ex1Objects import Building
from Ex1Objects import CallForElevator
from Ex1Objects import Elevator
from Brain import BrainTeamAlgo


class BrainTeamAlgoObject_test(TestCase):
    # CallForElevator(time, src, dest, state, allocatedTo, id)
    # Elevator(id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime)
    c0 = CallForElevator.CallForElevator(10.83, -2, 10, 0, -1, 0)
    c00 = CallForElevator.CallForElevator(10.83, -2, 10, 0, -1, 0)
    c1 = CallForElevator.CallForElevator(11.2, 0, -1, 0, -1, 1)
    c2 = CallForElevator.CallForElevator(15.0, 1, 2, 0, -1, 2)
    c3 = CallForElevator.CallForElevator(18.44, 7, 10, 0, -1, 3)

    c4 = CallForElevator.CallForElevator(51.53, 6, -2, 0, -1, 4)
    c5 = CallForElevator.CallForElevator(59.61, 5, -1, 0, -1, 5)
    c6 = CallForElevator.CallForElevator(60.61, 5, 1, 0, -1, 6)
    c11 = CallForElevator.CallForElevator(63.2, 0, -1, 0, -1, 11)
    listC1 = [c0]
    listC2 = [c00, c1, c2, c3, c4, c5, c6, c11]
    e0 = Elevator.Elevator(0, 1, -2, 10, 3, 3, 2, 2)
    e1 = Elevator.Elevator(1, 1.5, -5, 50, 2, 2, 1, 1)
    e2 = Elevator.Elevator(2, 1, -2, 10, 3, 3, 2, 2)
    listE1 = [e0]
    listE2 = [e1, e2]
    building1 = Building.Building(-2, 10, listE1, listC1)
    building2 = Building.Building(-2, 10, listE2, listC2)

    def test_run(self):
        smart_run_shfiut = BrainTeamAlgo.BrainTeamAlgo(self.building1)
        smart_run_shfiut.run()
        self.assertEqual(self.c0.get_allocated_to(), 0, "failed with BDIKAT SHFIUT, please dont sign this algo")
        smart_run_serious = BrainTeamAlgo.BrainTeamAlgo(self.building2)
        smart_run_serious.run()
        self.assertEqual(self.c00.get_allocated_to(), 1, "failed allocatine c00 in real scenario, please go back to work")
        self.assertEqual(self.c1.get_allocated_to(), 2, "failed allocatine c1 in real scenario, please go back to work")
        self.assertEqual(self.c2.get_allocated_to(), 1, "failed allocatine c2 in real scenario, please go back to work")
        self.assertEqual(self.c3.get_allocated_to(), 1, "failed allocatine c3 in real scenario, please go back to work")
        self.assertEqual(self.c4.get_allocated_to(), 1, "failed real allocatine c4 in realscenario, please go back to work")
        self.assertEqual(self.c5.get_allocated_to(), 1, "failed real allocatine c5 in realscenario, please go back to work")
        self.assertEqual(self.c6.get_allocated_to(), 1, "failed real allocatine c6 in realscenario, please go back to work")
        self.assertEqual(self.c11.get_allocated_to(), 1, "failed real allocatine c11 in realscenario, please go back to work")
