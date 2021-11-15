class Building:
    def __init__(self, bot_floor, top_floor, list_of_elev, list_of_calls):
        global min, max
        self.botFloor = bot_floor
        self.topFloor = top_floor
        self.list_of_elev = list_of_elev
        self.list_of_calls = list_of_calls
        total_speed = 0.00
        for x in list_of_elev:
            total_speed = total_speed + x.get_speed()
        # average elevator speed
        self.avgSpeed = total_speed / len(list_of_elev)
        real_min = 1000000
        real_max = -1000000
        total = 0
        for x in list_of_calls:
            mini = min(x.get_src(), x.get_dest())
            maxi = max(x.get_src(), x.get_dest())
            total = total + x.get_distance()
            # find the maximum height relevant for the scenario
            if mini < real_min:
                real_min = mini
            if maxi > real_max:
                real_max = maxi
        self.real_min = real_min
        self.real_max = real_max

    def get_min_floor(self):
        return self.real_min

    def get_max_floor(self):
        return self.real_max

    def get_number_of_elevetors(self):
        return len(self.list_of_elev)

    def get_list_of_elevator(self):
        return self.list_of_elev

    def get_elevator(self, id_elev):
        return self.list_of_elev[id_elev]

    def get_list_of_calls(self):
        return self.list_of_calls

    def get_call(self, idx):
        return self.list_of_calls[idx]

    def get_number_of_calls(self):
        return len(self.list_of_calls)

    def get_avg_speed(self):
        return self.avgSpeed

    def get_height(self):
        return self.get_max_floor() - self.get_min_floor()
