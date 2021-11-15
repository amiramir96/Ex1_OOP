import Ex1Objects.Elevator
import Ex1Objects.Building


def time_to_end_call(call: Ex1Objects.CallForElevator.CallForElevator, elev: Ex1Objects.Elevator.Elevator):
    """return time to end call c by elev"""
    start = call.get_src()
    stop = call.get_dest()
    curr_pos = elev.get_pos()
    no_of_floors = abs(curr_pos - start) + abs(start - stop)
    moving_time = no_of_floors / elev.get_speed()
    stopping_time = elev.get_total_delay_time() * 2
    if call.get_start_time() < elev.get_curr_time():
        # mission starts right after last call
        relevant_curr_time = elev.get_curr_time()
    else:
        # mission starts when the call comes
        relevant_curr_time = call.get_start_time()
    return relevant_curr_time + moving_time + stopping_time


def time_to_end_path(time, start, stop, elev: Ex1Objects.Elevator.Elevator):
    """ return time to end path from e.position -> start floor -> stop floor by elev"""
    curr_pos = elev.get_pos()
    no_of_floors = abs(curr_pos - start) + abs(start - stop)
    moving_time = no_of_floors / elev.get_speed()
    stopping_time = elev.get_total_delay_time() * 2
    if time < elev.get_curr_time():
        relevant_curr_time = elev.get_curr_time()
    else:
        relevant_curr_time = time
    return relevant_curr_time + moving_time + stopping_time


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
    while idx < len(list_of_calls) and list_of_calls[idx].getStartTime() <= time_end_call and \
            len(output_list) <= building.get_height()/(len(building.get_list_of_elevator()) + building.get_avg_speed()):
        # there are still more calls in the scenario,
        # we are before the expected finish time of the original mission
        # and there are less than (Building height/(no. of elevators + average elevator speed))
        # calls already in our contained calls list.
        if list_of_calls[idx].getAllocatedTo() == -1 and call.is_contained(list_of_calls[idx]):
            # call is contained and no elevator is assigned to it
            roof_time = time_to_end_path(call.get_start_time(), call.get_src(), list_of_calls[idx].getSrc(), elev) - 1
            # roof_time - only merge calls that come before elevator leaves original src
            if roof_time > list_of_calls[idx].getStartTime():
                output_list.append(list_of_calls[idx])
        idx = idx + 1

    return output_list
