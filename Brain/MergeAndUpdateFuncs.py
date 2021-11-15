import Ex1Objects
from Brain.TimeAndPathFuncs import time_to_end_path


def contained_calls(building, list_of_calls: list, call: Ex1Objects.CallForElevator.CallForElevator,
                    elev: Ex1Objects.Elevator.Elevator, time_end_call: float):
    """
    return list of calls which are contained in the first (given) call (including original call)
    A call is contained in the original call if:
        1- The call has same type as the original call (up/down)
        2- their path is contained in the original call path (original src <= curr src <= curr dest = original dest)
        3- the call time in the scenario time BEFORE the elev is getting to her src floor
    """
    output_list = [call]
    # original call is the last call, terminate.
    if call.get_id == len(list_of_calls) - 1:
        return output_list

    idx = call.get_id() + 1
    # terms are:
    while idx < len(list_of_calls) and list_of_calls[idx].get_start_time() <= time_end_call and \
            len(output_list) <= building.get_height() / (
            len(building.get_list_of_elevator()) + building.get_avg_speed()):
        # there are still more calls in the scenario,
        # we are before the expected finish time of the original mission
        # and there are less than (Building height/(no. of elevators + average elevator speed))
        # calls already in our contained calls list.
        if list_of_calls[idx].get_allocated_to() == -1 and call.is_contained(list_of_calls[idx]):
            # call is contained and no elevator is assigned to it
            roof_time = time_to_end_path(call.get_start_time(), call.get_src(), list_of_calls[idx].get_src(), elev) - 1
            # roof_time - only merge calls that come before elevator leaves original src
            if roof_time > list_of_calls[idx].get_start_time():
                output_list.append(list_of_calls[idx])
        idx = idx + 1

    return output_list


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
