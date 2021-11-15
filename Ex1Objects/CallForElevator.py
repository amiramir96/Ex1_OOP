class CallForElevator:
    #    state INIT=0, GOING2SRC=1, GOING2DEST=2, DONE=3;
    #    type UP=1, DOWN=-1;
    #    id is index of Call at the cList (list_of_calls)
    def __init__(self, time, src, dest, state, allocated_to, id):
        self.time = float(time)
        self.src = int(src)
        self.dest = int(dest)
        self.state = int(state)
        self.allocatedTo = int(allocated_to)
        if self.dest - self.src > 0:
            self.type = 1
        else:
            self.type = -1
        self.id = id

    def get_start_time(self):
        return self.time

    def get_state(self):
        return self.state

    # only 0 to 3 numbers is valid!!
    def set_state(self, new_status):
        if 0 <= new_status <= 3:
            self.state = new_status

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest

    def get_type(self):
        return self.type

    def get_allocated_to(self):
        return self.allocatedTo

    def set_allocated_to(self, elev_id):
        self.allocatedTo = elev_id

    def get_id(self):
        return int(self.id)

    def get_distance(self):
        return abs(self.dest - self.src)

    def is_contained(self, call_check):
        """ True if check number is between two others """
        if self.get_type() == call_check.get_type() \
                and is_between(self.get_src(), self.get_dest(), call_check.get_src()) \
                and is_between(self.get_src(), self.get_dest(), call_check.get_dest()):
            return True
        return False

    def __str__(self):
        return "Elevator call" + "," + str(self.get_start_time()) + "," + str(self.get_src()) \
               + "," + str(self.get_dest()) + "," + str(self.state) + "," + str(self.allocatedTo)


def is_between(start, stop, check):
    """is number "check" between start and stop"""
    ans = False
    if stop <= check <= start:
        ans = True
    elif stop >= check >= start:
        ans = True
    return ans
