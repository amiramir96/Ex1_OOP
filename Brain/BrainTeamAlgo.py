import Ex1Objects.Elevator
import Ex1Objects.CallForElevator
import Brain.genericHelpFuncs


def optimal_elevator(list_elevators, call: Ex1Objects.CallForElevator.CallForElevator):
    """
    check what elevator is best for given call by  expected time to end mission.

    return best elevator id and its approximated finish time
    """
    opt_time = 2147483647
    opt_elev = list_elevators[0]
    for x in list_elevators:
        temp_time = Brain.genericHelpFuncs.time_to_end_call(call, x)
        if opt_time > temp_time:
            opt_time = temp_time
            opt_elev = x
    return [opt_elev, opt_time]


def how_many_stops(list_calls: list):
    """
    will check amount of stops that required to finish the whole list.\n
    list_calls - CallForElevator tasks that we want to do.
    """
    stops_list = []
    for x in list_calls:
        stops_list.append(int(x.get_src()))
        stops_list.append(int(x.get_dest()))
    stops_list.sort()
    # value is -2 since we already calculated 2 stops in the parent_call_time var of UPDATE_CALLS func
    # we only gonna check for extra stops (more than 2)
    stops_counter = -1
    for i in range(0, len(stops_list) - 1):
        if stops_list[i] != stops_list[i + 1]:
            stops_counter = stops_counter + 1
    return stops_counter


def update_calls(list_calls: list, elev: Ex1Objects.Elevator.Elevator, time_end_call: float):
    """
    the func will edit all calls in the list to be allocated to the input elev.\n
    the func will check the time which will take the elev to complete the whole list calls.\n
    the func will edit the curr elev time and pos to be updated
    for the next iteration in the algo RUN().\n
    input:\n
    list_calls - all the calls which we would like to assign together to the same elevator.\n
    e - relevant elevator.\n
    output:\n
    none, this func is "VOID", shall only complete her task
    """
    for x in list_calls:
        x.set_allocated_to(elev.get_id())
    stops_counter = how_many_stops(list_calls)
    total_calls_time = time_end_call + elev.get_total_delay_time() * stops_counter
    elev.set_pos(list_calls[0].get_dest())
    elev.set_curr_time(total_calls_time)


class BrainTeamAlgo:
    def __init__(self, building):
        self.building = building

    def run(self):
        """
        run on all calls
            check if curr call is NOT assigned to an elevator (otherwise, just move to next call)
                get the optimal elev for the task (best time to end mission)\n
                check if possible to merge into this task more tasks with "contained_calls"
                (check that func for more details)\n
                update_calls - update all relevant calls to be allocated, update new time and pos for the chosen elev
        """
        for call in self.building.get_list_of_calls():
            if call.get_allocated_to() == -1:
                # opt_elev is a pair!!! idx 0 = optimal elevator obj, idx 1 = time to end Call by optimal elevator
                opt_elev = optimal_elevator(self.building.get_list_of_elevator(), call)

                tasks_list = Brain.genericHelpFuncs.contained_calls(self.building, self.building.get_list_of_calls(),
                                                                    call, opt_elev[0], opt_elev[1])
                update_calls(tasks_list, opt_elev[0], opt_elev[1])
