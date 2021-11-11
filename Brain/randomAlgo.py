import random
import Ex1Objects.Building
import Ex1Objects.Elevator
import Ex1Objects.CallForElevator

"""
as it sounds, engage randomally between elevator to calls
"""


class randomAlgo:
    def __init__(self, Building):
        self.building = Building

    def run(self):
        i = 0
        for x in self.building.getListOfCalls():
            x.setAllocatedTo(random.randint(0, self.building.getNumberOfElevetors() - 1))
            i = i + 1
