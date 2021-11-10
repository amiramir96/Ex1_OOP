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


class FlexGreedAlgo:
    def __init__(self, Building):
        self.building = Building
        # Brain.genericHelpFuncs.sortElevator(self.building.getListOfElevator())
        Brain.genericHelpFuncs.reserveSortElevator(self.building.getListOfElevator())

    def run(self):
        list_of_calls = self.building.getListOfCalls()
        """
        run every elevator with its turn, from idx 0 to last at list_of_elevators
        """
        for x in range(0, self.building.getNumberOfElevetors()):
            elev = self.building.getElevator(x)
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
                    each iterate of the first while loop represents a bulk of t seconds between first unegaged call time to that time+t secs
                    in this gap of time and calls, the second while loop checks who is the optimal task(look for DEFINITION upstairs)
                    the choosen task getting eddited to be allocated to the curr elevator
                    """
                    first_unengaged_call_time = list_of_calls[idx].getStartTime()

                    idx_30s = Brain.genericHelpFuncs.gimmie30SecForward(list_of_calls, idx)
                    idx_opt = idx

                    temp_call = list_of_calls[idx_opt]
                    temp_opt_time = Brain.genericHelpFuncs.timeToEndTask(elev, temp_call.getSrc(), temp_call.getDest(), 0, 0)
                    idx = idx+1

                    while idx != len(list_of_calls) and idx <= idx_30s:
                        temp_call = list_of_calls[idx]

                        if temp_call.getAllocatedTo() == -1:
                            temp_call_start_time = temp_call.getStartTime()
                            # delta is only double parameter, we shall take into consideration
                            # the delay of time from further tasks
                            delta = Brain.genericHelpFuncs.deltaTime(first_unengaged_call_time, temp_call_start_time)
                            temp_task_time = Brain.genericHelpFuncs.timeToEndTask(elev, temp_call.getSrc(),
                                                                                  temp_call.getDest(), delta, 0)
                            if temp_opt_time > temp_task_time:
                                temp_opt_time = temp_task_time
                                idx_opt = idx

                        idx = idx + 1
                    # best mission found, edit it on list_of_calls, also edit elevator currPos for next iterate
                    list_of_calls[idx_opt].setAllocatedTo(elev.getID())
                    elev.setPos(list_of_calls[idx_opt].getDest())
                    idx = Brain.genericHelpFuncs.gimmieIdxEndOfTask(list_of_calls, idx_opt, temp_opt_time)

                else:
                    idx = idx + 1

        #just a plaster
        for y in range(0, len(list_of_calls)):
            c = list_of_calls[y]
            if c.getAllocatedTo() == -1:
                list_of_calls[y].setAllocatedTo(random.randint(0, self.building.getNumberOfElevetors()-1))
