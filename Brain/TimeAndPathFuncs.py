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


def optimal_elevator(list_elevators, call: Ex1Objects.CallForElevator.CallForElevator):
    """
    check what elevator is best for given call by  expected time to end mission.

    return best elevator id and its approximated finish time
    """
    opt_time = 2147483647
    opt_elev = list_elevators[0]
    for x in list_elevators:
        temp_time = time_to_end_call(call, x)
        if opt_time > temp_time:
            opt_time = temp_time
            opt_elev = x
    return [opt_elev, opt_time]
