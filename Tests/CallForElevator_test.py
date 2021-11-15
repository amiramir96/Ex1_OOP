from unittest import TestCase
from Ex1Objects import CallForElevator
from Ex1Objects import Elevator


class CallForElevator_test(TestCase):
    # CallForElevator(time, src, dest, state, allocatedTo, id)
    c0 = CallForElevator.CallForElevator(12.0, 1, 2, 0, -1, 0)
    c1 = CallForElevator.CallForElevator(25.2, 0, -1, 0, -1, 1)
    c2 = CallForElevator.CallForElevator(30.83, -2, 8, 0, -1, 2)
    c3 = CallForElevator.CallForElevator(45.44, 7, 10, 0, -1, 3)
    e0 = Elevator.Elevator(0, 1, -2, 10, 3, 3, 2, 2)
    e1 = Elevator.Elevator(1, 1.5, -5, 50, 2, 2, 1, 1)

    def test_get_start_time(self):
        self.assertEqual(self.c0.getStartTime(), 12.0, "fail getStartTime0")
        self.assertEqual(self.c1.getStartTime(), 25.2, "fail getStartTime1")
        self.assertEqual(self.c2.getStartTime(), 30.83, "fail getStartTime2")
        self.assertEqual(self.c3.getStartTime(), 45.44, "fail getStartTime3")

    def test_set_state(self):
        self.assertEqual(self.c0.getState(), 0, "fail setState0")
        self.c0.setState(1)
        self.assertEqual(self.c0.getState(), 1, "fail setState0.1")
        self.c0.setState(2)
        self.assertEqual(self.c0.getState(), 2, "fail setState0.2")
        self.c0.setState(3)
        self.assertEqual(self.c0.getState(), 3, "fail setState0.3")
        self.c1.setState(5)
        self.assertEqual(self.c1.getState(), 0, "fail setState1.1")
        self.c0.setState(0)
        self.c1.setState(0)

    def test_get_state(self):
        self.assertEqual(self.c0.getState(), 0, "fail getState0")
        self.c1.setState(1)
        self.assertEqual(self.c1.getState(), 1, "fail getState1")
        self.c2.setState(2)
        self.assertEqual(self.c2.getState(), 2, "fail getState2")
        self.c2.setState(3)
        self.assertEqual(self.c2.getState(), 3, "fail getState2.1")
        self.c1.setState(0)
        self.c2.setState(0)

    def test_get_src(self):
        self.assertEqual(self.c0.getSrc(), 1, "fail getSrc0")
        self.assertEqual(self.c1.getSrc(), 0, "fail getSrc1")
        self.assertEqual(self.c2.getSrc(), -2, "fail getSrc2")
        self.assertEqual(self.c3.getSrc(), 7, "fail getSrc3")

    def test_get_dest(self):
        self.assertEqual(self.c0.getDest(), 2, "fail getDest0")
        self.assertEqual(self.c1.getDest(), -1, "fail getDest1")
        self.assertEqual(self.c2.getDest(), 8, "fail getDest2")
        self.assertEqual(self.c3.getDest(), 10, "fail getDest3")

    def test_get_type(self):
        self.assertEqual(self.c0.getType(), 1, "fail getType0")
        self.assertEqual(self.c1.getType(), -1, "fail getType1")
        self.assertEqual(self.c2.getType(), 1, "fail getType2")
        self.assertEqual(self.c3.getType(), 1, "fail getType3")

    def test_get_allocated_to(self):
        self.assertEqual(self.c0.getAllocatedTo(), -1, "fail getAllocated0")
        self.assertEqual(self.c1.getAllocatedTo(), -1, "fail getAllocated1")
        self.c1.setAllocatedTo(0)
        self.assertEqual(self.c1.getAllocatedTo(), 0, "fail getAllocated1.1")
        self.c1.setAllocatedTo(1)
        self.assertEqual(self.c1.getAllocatedTo(), 1, "fail getAllocated2")

    def test_set_allocated_to(self):
        self.c0.setAllocatedTo(1)
        self.assertEqual(self.c0.getAllocatedTo(), 1, "fail setAllocated0")
        self.c1.setAllocatedTo(-1)
        self.assertEqual(self.c1.getAllocatedTo(), -1, "fail setAllocated1")
        self.c1.setAllocatedTo(1)
        self.assertEqual(self.c1.getAllocatedTo(), 1, "fail setAllocated1.1")
        self.c1.setAllocatedTo(0)
        self.assertEqual(self.c1.getAllocatedTo(), 0, "fail setAllocated1.2")

    def test_get_id(self):
        self.assertEqual(self.c0.getId(), 0, "fail getId0")
        self.assertEqual(self.c1.getId(), 1, "fail getId1")
        self.assertEqual(self.c2.getId(), 2, "fail getId2")
        self.assertEqual(self.c3.getId(), 3, "fail getId3")

    def test_get_distance(self):
        self.assertEqual(self.c0.getDistance(), 1, "fail getDistance0")
        self.assertEqual(self.c1.getDistance(), 1, "fail getDistance1")
        self.assertEqual(self.c2.getDistance(), 10, "fail getDistance2")
        self.assertEqual(self.c3.getDistance(), 3, "fail getDistance3")

    def test_is_contained(self):
        self.assertFalse(self.c0.isContained(self.c1), "fail isContained c1 in c0")
        self.assertFalse(self.c3.isContained(self.c2), "fail isContained c2 in c3")
        self.assertFalse(self.c2.isContained(self.c1), "fail isContained c1 in c2")
        self.assertTrue(self.c2.isContained(self.c0), "fail isContained c0 in c2")
