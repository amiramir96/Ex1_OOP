from unittest import TestCase
from Ex1Objects import Elevator


class Elevator_test(TestCase):
    # Elevator(id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime)
    e0 = Elevator.Elevator(0, 1, -2, 10, 3, 3, 2, 2)
    e1 = Elevator.Elevator(1, 1.5, -5, 50, 2, 2, 1, 1)
    e2 = Elevator.Elevator(2, 2.5, -10, 100, 2, 2, 1, 1)
    e3 = Elevator.Elevator(3, 1, -4, 20, 3, 3, 2, 2)

    def test_get_id(self):
        self.assertEqual(self.e0.getId(), 0, "fail Id0")
        self.assertEqual(self.e1.getId(), 1, "fail Id1")
        self.assertEqual(self.e2.getId(), 2, "fail Id2")
        self.assertEqual(self.e3.getId(), 3, "fail Id3")

    def test_get_speed(self):
        self.assertEqual(self.e0.getSpeed(), 1, "fail speed0")
        self.assertEqual(self.e1.getSpeed(), 1.5, "fail speed1")
        self.assertEqual(self.e2.getSpeed(), 2.5, "fail speed2")
        self.assertEqual(self.e3.getSpeed(), 1, "fail speed3")

    def test_get_min_floor(self):
        self.assertEqual(self.e0.getMinFloor(), -2, "fail minFloor0")
        self.assertEqual(self.e1.getMinFloor(), -5, "fail minFloor1")
        self.assertEqual(self.e2.getMinFloor(), -10, "fail minFloor2")
        self.assertEqual(self.e3.getMinFloor(), -4, "fail minFloor3")

    def test_get_max_floor(self):
        self.assertEqual(self.e0.getMaxFloor(), 10, "fail Maxfloor0")
        self.assertEqual(self.e1.getMaxFloor(), 50, "fail Maxfloor1")
        self.assertEqual(self.e2.getMaxFloor(), 100, "fail Maxfloor2")
        self.assertEqual(self.e3.getMaxFloor(), 20, "fail Maxfloor3")

    def test_get_close_time(self):
        self.assertEqual(self.e0.getCloseTime(), 3.0, "fail closeTime0")
        self.assertEqual(self.e1.getCloseTime(), 2.0, "fail closeTime1")
        self.assertEqual(self.e2.getCloseTime(), 2.0, "fail closeTime2")
        self.assertEqual(self.e3.getCloseTime(), 3.0, "fail closeTime3")

    def test_get_open_time(self):
        self.assertEqual(self.e0.getOpenTime(), 3.0, "fail openTime0")
        self.assertEqual(self.e1.getOpenTime(), 2.0, "fail openTime1")
        self.assertEqual(self.e2.getOpenTime(), 2.0, "fail openTime2")
        self.assertEqual(self.e3.getOpenTime(), 3.0, "fail openTime3")

    def test_get_stop_time(self):
        self.assertEqual(self.e0.getStopTime(), 2.0, "fail stopTime0")
        self.assertEqual(self.e1.getStopTime(), 1.0, "fail stopTime1")
        self.assertEqual(self.e2.getStopTime(), 1.0, "fail stopTime2")
        self.assertEqual(self.e3.getStopTime(), 2.0, "fail stopTime3")

    def test_get_start_time(self):
        self.assertEqual(self.e0.getStartTime(), 2.0, "fail startTime0")
        self.assertEqual(self.e1.getStartTime(), 1.0, "fail startTime1")
        self.assertEqual(self.e2.getStartTime(), 1.0, "fail startTime2")
        self.assertEqual(self.e3.getStartTime(), 2.0, "fail startTime3")

    def test_get_pos(self):
        self.assertEqual(self.e0.getPos(), 0, "fail pos0")
        self.assertEqual(self.e1.getPos(), 0, "fail pos0")
        self.assertEqual(self.e2.getPos(), 0, "fail pos0")
        self.assertEqual(self.e3.getPos(), 0, "fail pos0")
        self.e1.setPos(15)
        self.assertEqual(self.e1.getPos(), 15, "fail pos1afterset")
        self.e2.setPos(78)
        self.assertEqual(self.e2.getPos(), 78, "fail pos2afterset")

    def test_set_pos(self):
        self.e0.setPos(3)
        self.assertEqual(self.e0.getPos(), 3, "fail setpos0")
        self.e1.setPos(15)
        self.assertEqual(self.e1.getPos(), 15, "fail setpos1")
        self.e2.setPos(55)
        self.assertEqual(self.e2.getPos(), 55, "fail setpos2")
        self.e3.setPos(-4)
        self.assertEqual(self.e3.getPos(), -4, "fail setpos3")

    def test_get_state(self):
        self.assertEqual(self.e0.getState(), 0, "fail state0")
        self.assertEqual(self.e1.getState(), 0, "fail state1")
        self.assertEqual(self.e2.getState(), 0, "fail state2")
        self.assertEqual(self.e3.getState(), 0, "fail state3")

    def test_get_total_delay_time(self):
        self.assertEqual(self.e0.getTotalDelayTime(), 10.0, "fail totalDelayTime0")
        self.assertEqual(self.e1.getTotalDelayTime(), 6.0, "fail totalDelayTime1")
        self.assertEqual(self.e2.getTotalDelayTime(), 6.0, "fail totalDelayTime2")
        self.assertEqual(self.e3.getTotalDelayTime(), 10.0, "fail totalDelayTime3")

    def test_set_curr_time(self):
        self.e1.setCurrTime(18.5123)
        self.e2.setCurrTime(421.931)
        self.e3.setCurrTime(3.14)
        self.assertEqual(self.e1.getCurrTime(), 18.5123, "fail setCurrTime1")
        self.assertEqual(self.e2.getCurrTime(), 421.931, "fail setCurrTime2")
        self.assertEqual(self.e3.getCurrTime(), 3.14, "fail setCurrTime3")

    def test_get_curr_time(self):
        self.e2.setCurrTime(421.931)
        self.e3.setCurrTime(3.14)
        self.assertEqual(self.e0.getCurrTime(), 0.0, "fail getCurrTime0")
        self.assertEqual(self.e2.getCurrTime(), 421.931, "fail getCurrTime2")
        self.assertEqual(self.e3.getCurrTime(), 3.14, "fail getCurrTime3")
