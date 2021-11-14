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
        relevant_curr_time = elev.getCurrTime()
    else:
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


def timeTravelNoDelay(start, stop, elev: Ex1Objects.Elevator.Elevator):
    """return time to for TRAVEL only by elevator e"""
    curr_pos = elev.getPos()
    no_of_floors = abs(curr_pos - start) + abs(start - stop)
    moving_time = no_of_floors / elev.getSpeed()
    return elev.getCurrTime() + moving_time


"""
return list_of_calls which contains into the first call (call input function)
this calls shall stand with the next terms:
1- being same type with the input call
2- their path shall be contained into the input call path
3- the checken call have to "show up" in the scenario time BEFORE the elev is getting to her src floor
"""


def containedCalls(building, list_of_calls: list, call: Ex1Objects.CallForElevator.CallForElevator,
                   elev: Ex1Objects.Elevator.Elevator, time_end_call: float):
    output_list = [call]
    # thats the last call on the list, proccess is uneedded
    if call.getId == len(list_of_calls) - 1:
        return output_list

    # start proccess
    idx = call.getId() + 1
    # terms is:
    while idx < len(list_of_calls) and list_of_calls[idx].getStartTime() <= time_end_call and len(output_list) <= building.getHeight()/(len(building.getListOfElevator())+building.getAvgSpeed()):
        if list_of_calls[idx].getAllocatedTo() == -1 and call.isContained(list_of_calls[idx]):
            # roof_time - higher/equal to that, couldnt stop to take mission
            roof_time = timeToEndPath(call.getStartTime(), call.getSrc(), list_of_calls[idx].getSrc(), elev) - 1
            if roof_time > list_of_calls[idx].getStartTime():
                output_list.append(list_of_calls[idx])
        idx = idx + 1

    return output_list


"""
True if check number is between two others
"""


def isBetween(start, stop, check):
    ans = False
    if stop <= check <= start:
        ans = True
    elif stop >= check >= start:
        ans = True
    return ans


"""
1 for UP, -1 for DOWN 
"""


def taskDirection(start, stop):
    if start <= stop:
        return 1
    else:
        return -1


"""
elev - curr elevator
start,stop - floor numbers of task
stop_amount - for cal delay time of open/close/start/stop
delay_from_prev_task - its possible that the curr task will be start after D time of delay since the last task which got ended
output_time is float type!!
"""


def timeToEndTask(elev: Ex1Objects.Elevator.Elevator, start, stop, delay_from_prev_task, stop_amount):
    floors_move_time = (abs(elev.getPos() - start) + abs(start - stop)) / elev.getSpeed()
    stops_delay_time = (
                               elev.getCloseTime() + elev.getStartTime() + elev.getStopTime() + elev.getOpenTime()) * stop_amount
    output_time = floors_move_time + stops_delay_time + delay_from_prev_task
    return output_time


# def howManyStops(elev: Ex1Objects.Elevator.Elevator, list_of_calls):
#     stops_counter = 0
#     curr_pos = elev.getPos()
#     for i in range(0, len(list_of_calls)):
#         j = i+1
#         while j < len(list_of_calls):
#


"""
just simple cal for delta
"""


def deltaTime(start, stop):
    return abs(stop - start)


"""
get list of CallForElevator and idx start which represent Call in the list (and her time start)
returns idx of last Call inside the 30sec range of task - inside the list of calls
"""


def gimmie30SecForward(building, elev: Ex1Objects.Elevator.Elevator, list_of_calls: list, idx_start: int):
    idx_stop = idx_start + 1
    if isSlow(building, elev):
        const = elev.getTotalDelayTime() * 2
    else:
        const = elev.getTotalDelayTime() * 1
    top_time = list_of_calls[idx_start].getStartTime() + const
    while idx_stop < len(list_of_calls) - 1:
        temp = list_of_calls[idx_stop].getStartTime()
        if temp < top_time:
            idx_stop = idx_stop + 1
        else:
            break
    if idx_stop != len(list_of_calls) - 1:
        idx_stop = idx_stop - 1
    return idx_stop


"""
get list of CallForElevator and idx start which represent Call in the list (and her time start) and time_curr_mission
returns idx of first Call after the end of the curr task
"""


def gimmieIdxEndOfTask(list_of_calls: list, idx_start: int, time_curr_mission: float):
    idx_stop = idx_start + 1
    top_time = list_of_calls[idx_start].getStartTime() + time_curr_mission
    while idx_stop < len(list_of_calls) - 1:
        temp = list_of_calls[idx_stop].getStartTime()
        if temp < top_time:
            idx_stop = idx_stop + 1
        else:
            break
    return idx_stop


"""
sort from slowest to fastest
use bubble sort since there is small amount of elevators
"""


def sortElevator(list_of_elevators: list):
    for i in list_of_elevators:
        for j in range(0, len(list_of_elevators) - 1):
            if list_of_elevators[j].getSpeed() > list_of_elevators[j + 1].getSpeed():
                temp = list_of_elevators[j]
                list_of_elevators[j] = list_of_elevators[j + 1]
                list_of_elevators[j + 1] = temp


"""
sort from fastest to slowest
use bubble sort since there is small amount of elevators
"""


def reserveSortElevator(list_of_elevators: list):
    for i in list_of_elevators:
        for j in range(0, len(list_of_elevators) - 1):
            if list_of_elevators[j].getSpeed() < list_of_elevators[j + 1].getSpeed():
                temp = list_of_elevators[j]
                list_of_elevators[j] = list_of_elevators[j + 1]
                list_of_elevators[j + 1] = temp


"""
sort first the "isSlow" elev from fast to slow
then the "!isSlow" elev from fast to slow
"""


def specialSortElevator(building, list_of_elevators: list):
    for i in list_of_elevators:
        for j in range(0, len(list_of_elevators) - 1):
            if list_of_elevators[j].getSpeed() > list_of_elevators[j + 1].getSpeed():
                temp = list_of_elevators[j]
                list_of_elevators[j] = list_of_elevators[j + 1]
                list_of_elevators[j + 1] = temp
    counter = 0
    for x in list_of_elevators:
        if isSlow(building, x):
            counter = counter + 1

    for i in range(counter - 1, int((counter) / 2), -1):
        swap(list_of_elevators, i, counter - 1 - i)
    k = 1
    for j in range(counter, math.ceil(len(list_of_elevators) - counter / 2)):
        swap(list_of_elevators, j, len(list_of_elevators) - k)
        k = k + 1


def swap(list_of_elevators, one, two):
    temp = list_of_elevators[one]
    list_of_elevators[one] = list_of_elevators[two]
    list_of_elevators[two] = temp


"""
early_call - call that gonna show first in the scenario
further_call - call that gonna show after in the scenario time line
check two tasks is being able to merge:
~~~~~~~
NOTmergeAble = -1
~~~~~~~
for any value which is NOT 0 - both calls TYPE is SAME!
further_call.getSrc() is between early_call src-dest road = 1
further_call src And dest is between early_call src-dest road = 2
further_call src is equal to early_call src or dest = 3
further_call dest is equal to early_call dest AND src is along the road = 4
further_call src and dest is equal to early_call src and dest = 5
"""


def isMergeAble(building, elev: Ex1Objects.Elevator.Elevator, list_of_calls: list, idx_start, idx_stop):
    output_list = []
    early_call = list_of_calls[idx_start]
    temp_idx = idx_start + 1

    if isSlow(building, elev):

        while temp_idx < len(list_of_calls) and temp_idx <= idx_stop:
            further_call = list_of_calls[temp_idx]

            if further_call.getAllocatedTo() == -1 and \
                    early_call.getType() == further_call.getType() and further_call.getDistance() < building.getHeight() * 0.5:

                if (isBetween(early_call.getSrc(), early_call.getDest(),
                              further_call.getSrc()) and early_call.getDest() == further_call.getDest()) \
                        or (early_call.getSrc() == further_call.getSrc() and isBetween(early_call.getSrc(),
                                                                                       early_call.getDest(),
                                                                                       further_call.getDest())):
                    output_list.append(temp_idx)
            temp_idx = temp_idx + 1

    else:

        while temp_idx < len(list_of_calls) and temp_idx <= idx_stop:
            further_call = list_of_calls[temp_idx]

            if further_call.getAllocatedTo() == -1 and \
                    early_call.getType() == further_call.getType() and further_call.getDistance() > building.getHeight() * 0.25:

                if (isBetween(early_call.getSrc(), early_call.getDest(),
                              further_call.getSrc()) and early_call.getDest() == further_call.getDest()) \
                        or (early_call.getSrc() == further_call.getSrc() and isBetween(early_call.getSrc(),
                                                                                       early_call.getDest(),
                                                                                       further_call.getDest())):
                    output_list.append(temp_idx)
            temp_idx = temp_idx + 1
    return output_list


def isSlow(building, elev: Ex1Objects.Elevator.Elevator):
    if elev.getSpeed() <= building.getAvgSpeed():
        return True
    return False
