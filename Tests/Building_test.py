from unittest import TestCase
from Ex1Objects import Building
from Ex1Objects import CallForElevator
from Ex1Objects import Elevator


class Building_test(TestCase):
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
    building3 = Building.Building(-2, 10, listE3, listC3)

    def test_get_min_floor(self):
        self.assertEqual(self.building1.getMinFloor(), 1, "fail min1")
        self.assertEqual(self.building2.getMinFloor(), -2, "fail min2")
        self.assertEqual(self.building3.getMinFloor(), 0, "fail min3")

    def test_get_max_floor(self):
        self.assertEqual(self.building1.getMaxFloor(), 2, "fail max1")
        self.assertEqual(self.building2.getMaxFloor(), 10, "fail max2")
        self.assertEqual(self.building3.getMaxFloor(), 9, "fail max3")

    def test_get_number_of_elevetors(self):
        self.assertEqual(self.building1.getNumberOfElevetors(), 1, "fail numE1")
        self.assertEqual(self.building2.getNumberOfElevetors(), 4, "fail numE2")
        self.assertEqual(self.building3.getNumberOfElevetors(), 2, "fail numE3")

    def test_get_list_of_elevator(self):
        self.assertEqual(self.building1.getListOfElevator(), self.listE1, "fail listE1")
        self.assertEqual(self.building2.getListOfElevator(), self.listE2, "fail listE2")
        self.assertEqual(self.building3.getListOfElevator(), self.listE3, "fail listE3")

    def test_get_elevator(self):
        self.assertEqual(self.building1.getElevator(0), self.e0, "fail getE0")
        self.assertEqual(self.building2.getElevator(3), self.e3, "fail getE1")
        self.assertEqual(self.building3.getElevator(1), self.e2, "fail getE2")

    def test_get_list_of_calls(self):
        self.assertEqual(self.building1.getListOfCalls(), self.listC1, "fail ListC1")
        self.assertEqual(self.building2.getListOfCalls(), self.listC2, "fail ListC2")
        self.assertEqual(self.building3.getListOfCalls(), self.listC3, "fail ListC3")

    def test_get_call(self):
        self.assertEqual(self.building1.getCall(0), self.c0, "fail getC0")
        self.assertEqual(self.building2.getCall(2), self.c2, "fail getC3")
        self.assertEqual(self.building3.getCall(1), self.c4, "fail getC2")

    def test_get_number_of_calls(self):
        self.assertEqual(self.building1.getNumberOfCalls(), 1, "fail length LC1")
        self.assertEqual(self.building2.getNumberOfCalls(), 6, "fail length LC2")
        self.assertEqual(self.building3.getNumberOfCalls(), 3, "fail length LC3")

    def test_get_avg_speed(self):
        self.assertEqual(self.building1.getAvgSpeed(), 1, "fail AvgS1")
        self.assertEqual(self.building2.getAvgSpeed(), 1.5, "fail AvgS2")
        self.assertEqual(self.building3.getAvgSpeed(), 2, "fail AvgS3")

    def test_get_height(self):
        self.assertEqual(self.building1.getHeight(), 1, "fail Height1")
        self.assertEqual(self.building2.getHeight(), 12, "fail Height2")
        self.assertEqual(self.building3.getHeight(), 9, "fail Height3")
