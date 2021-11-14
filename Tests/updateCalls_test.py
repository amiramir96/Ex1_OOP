from unittest import TestCase
from Ex1Objects import CallForElevator
from Ex1Objects import Elevator
from Brain import BrainTeamAlgo


class updateCalls_test(TestCase):
    # CallForElevator(time, src, dest, state, allocatedTo, id)
    # Elevator(id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime)
    c0 = CallForElevator.CallForElevator(12.0, 1, 2, 0, -1, 0)
    c1 = CallForElevator.CallForElevator(25.2, 0, -1, 0, -1, 1)
    c2 = CallForElevator.CallForElevator(30.83, -2, 10, 0, -1, 2)
    c3 = CallForElevator.CallForElevator(10.44, 7, 10, 0, -1, 3)
    c33 = CallForElevator.CallForElevator(10.44, 7, 10, 0, -1, 3)
    c4 = CallForElevator.CallForElevator(51.53, 9, 4, 0, -1, 4)
    c5 = CallForElevator.CallForElevator(59.61, 5, -1, 0, -1, 5)
    c6 = CallForElevator.CallForElevator(60.61, 5, 1, 0, -1, 5)
    c11 = CallForElevator.CallForElevator(63.2, 0, -1, 0, -1, 1)
    listC1 = [c2, c33]
    listC2 = [c2, c1, c0, c3, c4, c5]
    listC3 = [c5, c6, c11]
    e0 = Elevator.Elevator(0, 1, -2, 10, 3, 3, 2, 2)
    e1 = Elevator.Elevator(1, 1.5, -5, 50, 2, 2, 1, 1)
    e2 = Elevator.Elevator(2, 2.5, -10, 100, 2, 2, 1, 1)

    def test_update_calls(self):
        # reminder**: total_calls_time = time_end_call + elev.getTotalDelayTime() * stops_counter
        BrainTeamAlgo.updateCalls(self.listC2, self.e0, 64.83)
        self.assertEqual(self.e0.getPos(), 10, "fail update e0 position")
        self.assertAlmostEqual(self.e0.getCurrTime(), 144.83, None, "fail to calculate and/or update accurate updated time", 0.1)
        BrainTeamAlgo.updateCalls(self.listC2, self.e1, 52.16)
        self.assertEqual(self.e1.getPos(), 10, "fail update e0 position")
        self.assertAlmostEqual(self.e1.getCurrTime(), 100.16, None, "fail e1 to calculate and/or update accurate updated time", 0.1)
        BrainTeamAlgo.updateCalls(self.listC1, self.e2, 48.43)
        self.assertEqual(self.e2.getPos(), 10, "fail update e1 position")
        self.assertAlmostEqual(self.e2.getCurrTime(), 54.43, None, "fail e1 to calculate and/or update accurate updated time", 0.1)
        self.e2.setPos(0)
        self.e2.setCurrTime(0.0)
        BrainTeamAlgo.updateCalls(self.listC3, self.e2, 76.01)
        self.assertEqual(self.e2.getPos(), -1, "fail update e3 position")
        self.assertAlmostEqual(self.e2.getCurrTime(), 88.01, None, "fail e2 to calculate and/or update accurate updated time", 0.1)
