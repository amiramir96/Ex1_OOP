from Ex1Objects import Elevator
from Ex1Objects import CallForElevator


class Building:
    def __init__(self, botFloor, topFloor, list_of_elev, list_of_calls):
        global min, max
        self.botFloor = botFloor
        self.topFloor = topFloor
        self.list_of_elev = list_of_elev
        self.list_of_calls = list_of_calls
        total_speed = 0.00
        for x in list_of_elev:
            total_speed = total_speed + x.getSpeed()
        self.avgSpeed = total_speed / len(list_of_elev)
        real_min = 1000000
        real_max = -1000000
        for x in list_of_calls:
            mini = min(x.getSrc(), x.getDest())
            maxi = max(x.getSrc(), x.getDest())
            if mini < real_min:
                real_min = mini
            if maxi > real_max:
                real_max = maxi
        self.real_min = real_min
        self.real_max = real_max

    def getMinFloor(self):
        return self.real_min

    def getMaxFloor(self):
        return self.real_max

    def getNumberOfElevetors(self):
        return len(self.list_of_elev)

    def getListOfElevator(self):
        return self.list_of_elev

    def getElevator(self, id_elev):
        return self.list_of_elev[id_elev]

    def getListOfCalls(self):
        return self.list_of_calls

    def getCall(self, idx):
        return self.list_of_calls[idx]

    def getNumberOfCalls(self):
        return len(self.list_of_calls)

    def getAvgSpeed(self):
        return self.avgSpeed

    def getHeight(self):
        return self.getMaxFloor() - self.getMinFloor()
