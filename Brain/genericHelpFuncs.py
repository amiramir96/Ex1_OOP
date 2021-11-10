import Ex1Objects.Elevator
import Ex1Objects.CallForElevator
import Ex1Objects.Building
import math

"""
True if check number is between two others
"""


def isBetween(start, stop, check):
    ans = False
    if stop <= check and check <= start:
        return not ans
    elif stop >= check and check >= start:
        return not ans
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
    output_time = (abs(start - stop) + abs(elev.getPos() - start)) / elev.getSpeed() + \
                  (elev.getStartTime() + elev.getStopTime() + elev.getOpenTime() + elev.getOpenTime()) * stop_amount \
                  + delay_from_prev_task
    return output_time


"""
just simple cal for delta
"""


def deltaTime(start, stop):
    return abs(stop - start)/12


"""
get list of CallForElevator and idx start which represent Call in the list (and her time start)
returns idx of last Call inside the 30sec range of task - inside the list of calls
"""


def gimmie30SecForward(list_of_calls: list, idx_start: int):
    idx_stop = idx_start + 1
    top_time = list_of_calls[idx_start].getStartTime() + 30
    while idx_stop < len(list_of_calls) - 1:
        temp = list_of_calls[idx_stop].getStartTime()
        if temp < top_time:
            idx_stop = idx_stop + 1
        else:
            break
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
            if (list_of_elevators[j].getSpeed() > list_of_elevators[j + 1].getSpeed()):
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
