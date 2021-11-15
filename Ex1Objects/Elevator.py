class Elevator:
    def __init__(self, id, speed, min_floor, max_floor, close_time, open_time, start_time, stop_time):
        self.id = id
        self.speed = speed
        self.minFloor = min_floor
        self.maxFloor = max_floor
        self.closeTime = close_time
        self.openTime = open_time
        self.startTime = start_time
        self.stopTime = stop_time
        self.currPos = 0
        #   state: UP=1 DOWN=-1 LEVEL(idle)=0
        self.state = 0
        self.currTime = 0.0

    def get_id(self):
        return self.id

    def get_speed(self):
        return self.speed

    def get_min_floor(self):
        return self.minFloor

    def get_max_floor(self):
        return self.maxFloor

    def get_close_time(self):
        return self.closeTime

    def get_open_time(self):
        return self.openTime

    def get_stop_time(self):
        return self.stopTime

    def get_start_time(self):
        return self.startTime

    def get_pos(self):
        return self.currPos

    def set_pos(self, floor):
        self.currPos = floor

    def get_state(self):
        return self.state

    def get_total_delay_time(self):
        return self.startTime+self.stopTime+self.openTime+self.closeTime

    def get_curr_time(self):
        return self.currTime

    def set_curr_time(self, time):
        self.currTime = time

    def __str__(self):
        return "" + str(self.id) + "," + str(self.speed) + "," + str(self.minFloor) + ","\
               + str(self.maxFloor) + "," + str(self.closeTime) + "," + str(self.openTime)\
               + "," + str(self.startTime) + "," + str(self.stopTime) + "," + str(self.get_pos())\
               + "," + str(self.state)
