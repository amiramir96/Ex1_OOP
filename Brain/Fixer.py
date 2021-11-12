import Ex1Objects.Building
import Ex1Objects.Elevator
import Ex1Objects.CallForElevator
import Brain.genericHelpFuncs

"""
the Fixer file purpose is to clean after the mess of the greedy algo!
in the end of the "pure greed" run, we will remain with tasks which is not choosen for any elevator
so before we finish our offline engages, the Fixer will find the most "UNDAMAGED" elevator for ea task

DEFINITION - "undamaged" elevator - the elevator which will suffer the lowest delay from gets the curr checken call

this way we shall minimize our loose from greed algo const
"""

"""
look for all unAllocated (yet) calls and start the fixer proccess
"""


def FixerSkelton(list_of_calls: list, building):
    for y in range(0, len(list_of_calls)):
        c = list_of_calls[y]

        # found unAllocated call
        if c.getAllocatedTo() == -1:
            # big enough number to start work with the variable
            min_delay = 1000000
            for elev in building.getListOfElevator():
                # check every elevator
                # take calls before and after
                a = gimmieCallIdxBefore(elev, y, list_of_calls)
                b = gimmieCallIdxAfter(elev, y, list_of_calls)
                # main cal func, look below for more details
                delay = delayTime(elev, a, b, y, list_of_calls)
                if min_delay > delay:
                    min_delay = delay
                    fixer_elev_id = elev.getID()
            # set the best from the worst xD
            c.setAllocatedTo(fixer_elev_id)


"""
let "curr_idx" be the i CALLFORELEVATOR which is unchoosed
the two functions below will find the most close calls by time to i
this way, we can calculate the delay time that will pop up from pushing 1 more task between them
"""


def gimmieCallIdxBefore(elev: Ex1Objects.Elevator.Elevator, curr_idx, cList: list):
    a = curr_idx - 1
    while 0 <= a < curr_idx:
        if cList[a].getAllocatedTo() != elev.getID():
            a = a - 1
        else:
            break
    if a < 0:
        a = 0
    return a


# same as above
def gimmieCallIdxAfter(elev: Ex1Objects.Elevator.Elevator, curr_idx, cList: list):
    b = curr_idx + 1
    while curr_idx < b < len(cList):
        if cList[b].getAllocatedTo() != elev.getID():
            b = b + 1
        else:
            break
    if b >= len(cList):
        b = len(cList) - 1
    return b


"""
helper to the delayTime func
will change to zero any negative number
"""


def negativeGoZero(num):
    if num < 0:
        num = 0
    return num


"""
will calculate the delay time for a given elev if the pot_call will be pushed 
halfWay_delay - gonna suffer from half of the stopping penality times
fullWay_delay - gonna suffer from whole proccess of stopping penality times
cList - list_of_calls

"""


def delayTime(elev: Ex1Objects.Elevator.Elevator, prev_call_idx, next_call_idx, pot_call_idx, cList: list):
    halfWay_delay = elev.getCloseTime() + elev.getStartTime()
    fullWay_delay = elev.getOpenTime() + elev.getStopTime() + elev.getCloseTime() + elev.getStartTime()
    prev_call = cList[prev_call_idx]
    next_call = cList[next_call_idx]
    pot_call = cList[pot_call_idx]

    delay_time = 0
    """
    its a magic! credit to kiriloid of Travian.ru
    for more details on kiriloid for being a better Travian Player, check this site: https://travian.kirilloid.ru/
    or contact with Mr.B xD
    """
    new_src_prev = prev_call.getSrc() + \
                   int(negativeGoZero(
                       pot_call.getStartTime() - prev_call.getStartTime() - halfWay_delay) * elev.getSpeed())

    """
    let pot_call be the unchoosen task, prev_call - the closest call before it of same elevator, next_call - same as after call
    lets look on the currect path this way (like a ezpz graph):
    prev.Src[in reality - new_src_prev, thanks kiril :-P]  -> prev.Dest -> next.Src -> next.Dest
    and we have in hand the pot.Src && pot.Dest which we shall push somwhere there
    now the options (terms is):
    1- push pot.Src between prev.src and prev.dest then we shall check pot.dest in the next stations
    2- push pot.Src between prev.Dest and next.Src (reminder! next.Src wont happen till we already on the way to pot.Src thats why the last road isnt relevant)
    for each option we check where to push pot.Dest as well in the same thinking root
    and at every step update the delay_time as required
    """
    if Brain.genericHelpFuncs.isBetween(new_src_prev, prev_call.getDest(), pot_call.getSrc()):
        if prev_call.getDest() != pot_call.getSrc():
            delay_time = delay_time + fullWay_delay
        if Brain.genericHelpFuncs.isBetween(pot_call.getSrc(), prev_call.getDest(), pot_call.getDest()):
            if prev_call.getDest() != pot_call.getDest():
                delay_time = delay_time + fullWay_delay
        else:
            delay_time = delay_time + fullWay_delay + abs(prev_call.getDest() - pot_call.getDest()) / elev.getSpeed()
    else:
        if not Brain.genericHelpFuncs.isBetween(prev_call.getDest(), next_call.getSrc(), pot_call.getSrc()):
            delay_time = delay_time + fullWay_delay + abs(prev_call.getDest() - pot_call.getSrc()) / elev.getSpeed()
        else:
            delay_time = delay_time + halfWay_delay
        if not (Brain.genericHelpFuncs.isBetween(pot_call.getSrc(), next_call.getSrc(), pot_call.getDest()) or
                Brain.genericHelpFuncs.isBetween(next_call.getSrc(), next_call.getDest(), pot_call.getDest())):
            delay_time = delay_time + fullWay_delay + abs(pot_call.getSrc() - pot_call.getDest()) / elev.getSpeed()
        else:
            delay_time = delay_time + halfWay_delay + abs(prev_call.getDest() - pot_call.getSrc()) / elev.getSpeed()

    return delay_time


"""
unused funcs for now
"""
# def isContainCall(elev: Ex1Objects.Elevator.Elevator, curr_idx, pot_idx, cList: list):
#     curr_call = cList[curr_idx]
#     pot_call = cList[pot_idx]
#     halfWay_delay = elev.getCloseTime() + elev.getStartTime()
#     delta_move_time = abs(pot_call.getSrc() - curr_call.getSrC()) / elev.getSpeed()
#     return curr_call.getType() == pot_call.getType() and \
#            halfWay_delay + delta_move_time + curr_call.getStartTime() <= pot_call.getStartTime() and \
#            Brain.genericHelpFuncs.isBetween(curr_call.getSrc(), curr_call.getDest(), pot_call.getSrc()) and \
#            Brain.genericHelpFuncs.isBetween(curr_call.getSrc(), curr_call.getDest(), pot_call.getDest())


# def stopSaverCounter(elev: Ex1Objects.Elevator.Elevator, prev_call, next_call, pot_call, cList: list):
#     saver_counter = 0
#     if prev_call.getDest() == pot_call.getSrc():
#         saver_counter = saver_counter + 1
#     if next_call.getSrc() == pot_call.getDest():
#         saver_counter = saver_counter + 1
#     return saver_counter
