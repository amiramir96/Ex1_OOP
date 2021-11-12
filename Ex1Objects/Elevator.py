class Elevator:
#   state: UP=1 DOWN=-1 idle(LEVER)=0
    def __init__(self, id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime):
        self.id = id
        self.speed = speed
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.closeTime = closeTime
        self.openTime = openTime
        self.startTime = startTime
        self.stopTime = stopTime
        self.currPos = 0
        self.state = 0
        self.currTime = 0.0

    def getID(self):
        return self.id

    def getSpeed(self):
        return self.speed

    def getMinFloor(self):
        return self.minFloor

    def getMaxFloor(self):
        return self.maxFloor

    def getCloseTime(self):
        return self.closeTime

    def getOpenTime(self):
        return self.openTime

    def getStopTime(self):
        return self.stopTime

    def getStartTime(self):
        return self.startTime

    def getPos(self):
        return self.currPos

    def setPos(self, floor):
        self.currPos = floor

    def getState(self):
        return self.state

    def getTotalDelayTime(self):
        return self.startTime+self.stopTime+self.openTime+self.closeTime

    def getCurrTime(self):
        return self.currTime

    def setCurrTime(self, time):
        self.currTime = time

    def __str__(self):
        return ""+str(self.id)+","+str(self.speed)+","+str(self.minFloor)+","+str(self.maxFloor)+","+str(self.closeTime)\
               +","+str(self.openTime)+","+str(self.startTime)+","+str(self.stopTime)+","+str(self.getPos())\
               +","+str(self.state)