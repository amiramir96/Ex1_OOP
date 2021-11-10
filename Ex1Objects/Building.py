from Ex1Objects import Elevator
from Ex1Objects import CallForElevator
class Building:
    def __init__(self, botFloor, topFloor, list_of_elev, list_of_calls):
        self.botFloor = botFloor
        self.topFloor = topFloor
        self.list_of_elev = list_of_elev
        self.list_of_calls = list_of_calls

    def getMinFloor(self):
        return self.botFloor

    def getMaxFloor(self):
        return self.topFloor

    def getNumberOfElevetors(self):
        return len(self.list_of_elev)

    def getElevator(self, id_elev):
        return self.list_of_elev[id_elev]

    def getListOfCalls(self):
        return self.list_of_calls

    def getCall(self, idx):
        return self.list_of_calls[idx]

    def getNumberOfCalls(self):
        return len(self.list_of_calls)