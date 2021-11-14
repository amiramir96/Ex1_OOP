import Ex1Objects.Elevator
import Ex1Objects.CallForElevator
import Ex1Objects.Building
import math


def timeToEndCall(call: Ex1Objects.CallForElevator.CallForElevator, elev: Ex1Objects.Elevator.Elevator):
    """return time to end call c by elev"""
    start = call.getSrc()
    stop = call.getDest()
    curr_pos = elev.getPos()
    no_of_floors = abs(curr_pos - start) + abs(start - stop)
    moving_time = no_of_floors / elev.getSpeed()
    stopping_time = elev.getTotalDelayTime() * 2
    if call.getStartTime() < elev.getCurrTime():
        # mission starts right after last call
        relevant_curr_time = elev.getCurrTime()
    else:
        # mission starts when the call comes
        relevant_curr_time = call.getStartTime()
    return relevant_curr_time + moving_time + stopping_time


def timeToEndPath(time, start, stop, elev: Ex1Objects.Elevator.Elevator):
    """ return time to end path from e.position -> start floor -> stop floor by elev"""
    curr_pos = elev.getPos()
    no_of_floors = abs(curr_pos - start) + abs(start - stop)
    moving_time = no_of_floors / elev.getSpeed()
    stopping_time = elev.getTotalDelayTime() * 2
    if time < elev.getCurrTime():
        relevant_curr_time = elev.getCurrTime()
    else:
        relevant_curr_time = time
    return relevant_curr_time + moving_time + stopping_time


def containedCalls(building, list_of_calls: list, call: Ex1Objects.CallForElevator.CallForElevator,
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
    if call.getId == len(list_of_calls) - 1:
        return output_list

    idx = call.getId() + 1
    # terms are:
    while idx < len(list_of_calls) and list_of_calls[idx].getStartTime() <= time_end_call and \
            len(output_list) <= building.getHeight()/(len(building.getListOfElevator())+building.getAvgSpeed()):
        # there are still more calls in the scenario,
        # we are before the expected finish time of the original mission
        # and there are less than (Building height/(no. of elevators + average elevator speed))
        # calls already in our contained calls list.
        if list_of_calls[idx].getAllocatedTo() == -1 and call.isContained(list_of_calls[idx]):
            # call is contained and no elevator is assigned to it
            roof_time = timeToEndPath(call.getStartTime(), call.getSrc(), list_of_calls[idx].getSrc(), elev) - 1
            # roof_time - only merge calls that come before elevator leaves original src
            if roof_time > list_of_calls[idx].getStartTime():
                output_list.append(list_of_calls[idx])
        idx = idx + 1

    return output_list
