class CallForElevator:
#    state INIT=0, GOING2SRC=1, GOIND2DEST=2, DONE=3;
#    type UP=1, DOWN=-1;
#    id is index of Call at the cList (list_of_calls)
    def __init__(self, time, src, dest, state, allocatedTo, id):
        self.time = float(time)
        self.src = int(src)
        self.dest = int(dest)
        self.state = int(state)
        self.allocatedTo = int(allocatedTo)
        if (self.dest - self.src > 0):
            self.type = 1
        else:
            self.type = -1
        self.id = id

    def getStartTime(self):
        return self.time

    def getState(self):
        return self.state

    #only 0 to 3 numbers is valid!!
    def setState(self, new_status):
        if(0 <= new_status and new_status <= 3):
            self.state = new_status

    def getStatus(self):
        return self.status

    def getSrc(self):
        return self.src

    def getDest(self):
        return self.dest

    def getType(self):
        return self.type

    def getAllocatedTo(self):
        return self.allocatedTo

    def setAllocatedTo(self, elev_id):
        self.allocatedTo = elev_id

    def getId(self):
        return int(self.id)

    def __str__(self):
        return "Elevator call"+","+str(self.getStartTime())+","+str(self.getSrc())\
               +","+str(self.getDest())+","+str(self.state)+","+str(self.allocatedTo)