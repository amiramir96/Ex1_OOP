import Ex1Objects.Building
import Ex1Objects.Elevator
import Ex1Objects.CallForElevator
import random
import Brain.genericHelpFuncs
import Brain.Fixer
import Brain.randomAlgo

"""
check who is the best elevator for currect call within time to end mission
return its id and its approximated time
"""


def optimalElevator(list_elevators, call: Ex1Objects.CallForElevator.CallForElevator):
    opt_time = 2147483647
    opt_elev = list_elevators[0]
    for x in list_elevators:
        temp_time = Brain.genericHelpFuncs.timeToEndCall(call, x)
        if opt_time > temp_time:
            opt_time = temp_time
            opt_elev = x
    return [opt_elev, opt_time]


"""
will check amount of stops that required to finish the whole list
list_calls - hold all the CALLFORELEVATORS tasks that we would like to do
"""


def howManyStops(list_calls: list):
    stops_list = []
    for x in list_calls:
        stops_list.append(int(x.getSrc()))
        stops_list.append(int(x.getDest()))
    stops_list.sort()
    # value is -2 since we already calculated 2 stops in the parent_call_time var of UPDATECALLS func
    # we only gonna check for extra stops (more than 2)
    stops_counter = -1
    for i in range(0, len(stops_list) - 1):
        if stops_list[i] != stops_list[i + 1]:
            stops_counter = stops_counter + 1
    return stops_counter


"""
the func will edit all calls in the list to be allocated to the input elev
the func will check the time which will take the elev to accomplish the whole list calls
the func will edit the curr elev time and pos to be upadted fo next iterate in the algo RUN()
input:
list_calls - all the calls which we would like to engage togheter to the same elevator
e - relevant elevator
output:
none, this func is "VOID", shall only complete her task

"""


def updateCalls(list_calls: list, elev: Ex1Objects.Elevator.Elevator, time_end_call: float):
    for x in list_calls:
        x.setAllocatedTo(elev.getId())
    stops_counter = howManyStops(list_calls)
    total_calls_time = time_end_call + elev.getTotalDelayTime() * stops_counter
    elev.setPos(list_calls[0].getDest())
    elev.setCurrTime(total_calls_time)


"""
logic of algorithm:
run on all calls 
    check if curr call is UNENGAGED (else, just move to next call)
        get the optimal elev for the task (via time to end mission)
        check if possible to merge into this task more tasks via "containedTime" terms (check that func for more details)
        updateCalls - updated all calls to be allocated, update new time and pos for the choosen elev
"""


class BrainTeamAlgo:
    def __init__(self, building):
        self.building = building

    def run(self):
        for call in self.building.getListOfCalls():
            if call.getAllocatedTo() == -1:
                # opt_elev is LIST! of pair!!! idx 0 = elev opt obj, idx 1 = elev opt time to end Call
                opt_elev = optimalElevator(self.building.getListOfElevator(), call)
                tasks_list = Brain.genericHelpFuncs.containedCalls(self.building, self.building.getListOfCalls(), call,
                                                                   opt_elev[0], opt_elev[1])
                updateCalls(tasks_list, opt_elev[0], opt_elev[1])
