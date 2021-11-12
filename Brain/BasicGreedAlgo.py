import Ex1Objects.Building
import Ex1Objects.Elevator
import Ex1Objects.CallForElevator
import random
import Brain.genericHelpFuncs

"""
greed algorithm, always take the optimal mission(DEFINITION): which is gonna end as fast as possible by the curr elevator
there is 3 type of modes:
1- dont sort elevators, run from ID=0 till ID = building.numOfElevators()-1
2- sortElevators from slowest to fastest
3- sortElevators opositely to(2) - fastest to slowest

after algorithm is ending - engage randomally the calls that remained unengaged (in reserveSort mode is barely to not at all happens)
"""


class BasicGreedAlgo:
    def __init__(self, Building):
        self.building = Building
        Brain.genericHelpFuncs.sortElevator(self.building.getListOfElevator())
        # Brain.genericHelpFuncs.reserveSortElevator(self.building.getListOfElevator())

    def run(self):
        list_of_calls = self.building.getListOfCalls()
        """
        run every elevator with its turn, from idx 0 to last at list_of_elevators
        """
        for elev in self.building.getListOfElevator():
            """
            idx - very important index, always point to the curr call which we check
            loop - run on all the list_of_calls
            """
            idx = 0
            while idx < len(list_of_calls):
                """
                but only on unengaged calls
                """
                if list_of_calls[idx].getAllocatedTo() == -1:
                    """
                    logic of the algo:
                    choose the first task after which is not engaged from the list of calls that starts 
                    as soon as possible 
                    """
                    can_be_merged = []
                    # temp_call = list_of_calls[idx]
                    #
                    # idx_30s = Brain.genericHelpFuncs.gimmie30SecForward(self.building, elev, list_of_calls, idx)
                    # idx_opt = idx
#                    temp_call_start_time = temp_call.getStartTime()
                    # delta is only double parameter, we shall take into consideration
                    # the delay of time from further tasks
#                    delta = Brain.genericHelpFuncs.deltaTime(first_unengaged_call_time, temp_call_start_time)
#                     can_be_merged = Brain.genericHelpFuncs.isMergeAble(self.building, elev, list_of_calls, idx, idx_30s)
#                     if Brain.genericHelpFuncs.isSlow(self.building, elev) and len(can_be_merged) != 0:
#                         list_of_calls[idx].setAllocatedTo(elev.getID())
#                         elev.setPos(list_of_calls[idx].getDest())
#                         temp_time = Brain.genericHelpFuncs.timeToEndTask(elev, temp_call.getSrc(),
#                                                                              temp_call.getDest(), 0, 2)
#                         idx = Brain.genericHelpFuncs.gimmieIdxEndOfTask(list_of_calls, idx, temp_time)
#                         for x in can_be_merged:
#                             list_of_calls[x].setAllocatedTo(elev.getID())
#
#
#                     else:
                    list_of_calls[idx].setAllocatedTo(elev.getID())
                    elev.setPos(list_of_calls[idx].getDest())

                    temp_call = list_of_calls[idx]
                    time_curr_mission = Brain.genericHelpFuncs.timeToEndTask(elev, temp_call.getSrc(),
                                                                             temp_call.getDest(), 0, 2)
                    idx_next_new_task = Brain.genericHelpFuncs.gimmieIdxEndOfTask(list_of_calls, idx, time_curr_mission)
                    idx = idx_next_new_task
                    can_be_merged = []
                else:
                    idx = idx + 1

        # # # just a plaster of random algo
        # for y in range(0, len(list_of_calls)):
        #     c = list_of_calls[y]
        #     if c.getAllocatedTo() == -1:
        #         list_of_calls[y].setAllocatedTo(random.randint(0, self.building.getNumberOfElevetors() - 1))

        """
        shall engage the unchoosen calls somehow so...
        use the fixer! for more info, move to Fixer.py file
        """
        Brain.Fixer.FixerSkelton(list_of_calls, self.building)