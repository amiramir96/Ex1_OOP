import Ex1Objects.Building
import Ex1Objects.Elevator
import Ex1Objects.CallForElevator
import random
import Brain.genericHelpFuncs
import Brain.Fixer
import Brain.randomAlgo

"""
greed algorithm, always take the optimal mission(DEFINITION): which is gonna end as fast as possible by the curr elevator
there is 3 type of modes:
1- dont sort elevators, run from ID=0 till ID = building.numOfElevators()-1
2- sortElevators from slowest to fastest
3- sortElevators opositely to(2) - fastest to slowest
after algorithm is ending - engage randomally the calls that remained unengaged (in reserveSort mode is barely to not at all happens)

also use Fixer!
"""


class DistanceSplitAlgo:
    def __init__(self, Building):
        self.building = Building
        # Brain.genericHelpFuncs.sortElevator(self.building.getListOfElevator())
        Brain.genericHelpFuncs.reserveSortElevator(self.building.getListOfElevator())
        Brain.genericHelpFuncs.specialSortElevator(self.building, self.building.getListOfElevator())

        for x in self.building.list_of_elev:
            print(x)

    def run(self):
        list_of_calls = self.building.getListOfCalls()
        """
        run every elevator with its turn, from idx 0 to last at list_of_elevators
        """
        print("avg speed for this scenario is: ", self.building.getAvgSpeed())
        for elev in self.building.getListOfElevator():
            if Brain.genericHelpFuncs.isSlow(self.building, elev):
                slowElevProccess(self.building, elev, list_of_calls)
            else:
                fastElevProccess(self.building, elev, list_of_calls)

        """
        shall engage the unchoosen calls somehow so...
        use the fixer! for more info, move to Fixer.py file
        """
        Brain.Fixer.FixerSkelton(list_of_calls, self.building)

        # Brain.randomAlgo.randomFixer(self.building)


def slowElevProccess(building: Ex1Objects.Building.Building, elev: Ex1Objects.Elevator.Elevator, list_of_calls: list):
    idx = 0
    while idx < len(list_of_calls):

        if list_of_calls[idx].getAllocatedTo() == -1 and list_of_calls[idx].getDistance() < building.getHeight() * 0.5:
            idx_origin = idx
            idx_30s = Brain.genericHelpFuncs.gimmie30SecForward(building, elev, list_of_calls, idx)
            merged_list = []
            while idx <= idx_30s < len(list_of_calls):

                merged_list = Brain.genericHelpFuncs.isMergeAble(building, elev, list_of_calls, idx, idx_30s)
                if list_of_calls[idx].getDistance() < building.getHeight() * 0.5 and len(merged_list) > 0:

                    for x in merged_list:
                        list_of_calls[x].setAllocatedTo(elev.getID())
                    list_of_calls[idx].setAllocatedTo(elev.getID())
                    delta = Brain.genericHelpFuncs.deltaTime(list_of_calls[idx_origin].getStartTime(),
                                                             list_of_calls[idx].getStartTime())
                    time_end = Brain.genericHelpFuncs.timeToEndTask(elev, list_of_calls[idx].getSrc(),
                                                                    list_of_calls[idx].getDest(), delta,
                                                                    2 + len(merged_list))
                    elev.setPos(list_of_calls[idx].getDest())
                    idx = Brain.genericHelpFuncs.gimmieIdxEndOfTask(list_of_calls, idx, time_end)
                    break
                idx = idx + 1

            if len(merged_list) == 0:
                idx = idx_origin
                first_unengaged_call_time = list_of_calls[idx].getStartTime()
                temp_opt_time = 10000
                while len(list_of_calls) > idx_30s >= idx:
                    if list_of_calls[idx].getAllocatedTo() == -1 and list_of_calls[
                        idx].getDistance() < building.getHeight() * 0.5:

                        temp_call = list_of_calls[idx]
                        temp_call_start_time = temp_call.getStartTime()
                        delta = Brain.genericHelpFuncs.deltaTime(first_unengaged_call_time, temp_call_start_time)
                        temp_task_time = Brain.genericHelpFuncs.timeToEndTask(elev, temp_call.getSrc(),
                                                                              temp_call.getDest(), delta, 2)
                        if list_of_calls[
                            idx].getDistance() < building.getHeight() * 0.5 and temp_opt_time > temp_task_time:
                            temp_opt_time = temp_task_time
                            idx_opt = idx
                    idx = idx + 1
                    # best mission found, edit it on list_of_calls, also edit elevator currPos for next iterate

                list_of_calls[idx_opt].setAllocatedTo(elev.getID())
                elev.setPos(list_of_calls[idx_opt].getDest())
                idx = Brain.genericHelpFuncs.gimmieIdxEndOfTask(list_of_calls, idx_opt, temp_opt_time)

        else:
            idx = idx + 1


def fastElevProccess(building, elev: Ex1Objects.Elevator.Elevator, list_of_calls: list):
    idx = 0
    # while idx < len(list_of_calls):
    #
    #     if list_of_calls[idx].getAllocatedTo() == -1 and list_of_calls[idx].getDistance() > building.getHeight() * 0.25:
    #         idx_origin = idx
    #         idx_30s = Brain.genericHelpFuncs.gimmie30SecForward(building, elev, list_of_calls, idx)
    #         merged_list = []
    #         while idx <= idx_30s < len(list_of_calls):
    #
    #             merged_list = Brain.genericHelpFuncs.isMergeAble(building, elev, list_of_calls, idx, idx_30s)
    #             if list_of_calls[idx].getDistance() > building.getHeight() * 0.25 and len(merged_list) > 0:
    #
    #                 for x in merged_list:
    #                     list_of_calls[x].setAllocatedTo(elev.getID())
    #                 list_of_calls[idx].setAllocatedTo(elev.getID())
    #                 delta = Brain.genericHelpFuncs.deltaTime(list_of_calls[idx_origin].getStartTime(),
    #                                                          list_of_calls[idx].getStartTime())
    #                 time_end = Brain.genericHelpFuncs.timeToEndTask(elev, list_of_calls[idx].getSrc(),
    #                                                                 list_of_calls[idx].getDest(), delta,
    #                                                                 2 + len(merged_list))
    #                 elev.setPos(list_of_calls[idx].getDest())
    #                 idx = Brain.genericHelpFuncs.gimmieIdxEndOfTask(list_of_calls, idx, time_end)
    #                 break
    #             idx = idx + 1
    #
    #         if len(merged_list) == 0:
    #             idx = idx_origin
    #             first_unengaged_call_time = list_of_calls[idx].getStartTime()
    #             temp_opt_time = 10000
    #             while len(list_of_calls) > idx_30s >= idx:
    #                 if list_of_calls[idx].getAllocatedTo() == -1 and list_of_calls[
    #                     idx].getDistance() > building.getHeight() * 0.25:
    #
    #                     temp_call = list_of_calls[idx]
    #                     temp_call_start_time = temp_call.getStartTime()
    #                     delta = Brain.genericHelpFuncs.deltaTime(first_unengaged_call_time, temp_call_start_time)
    #                     temp_task_time = Brain.genericHelpFuncs.timeToEndTask(elev, temp_call.getSrc(),
    #                                                                           temp_call.getDest(), delta, 2)
    #                     if list_of_calls[
    #                         idx].getDistance() > building.getHeight() * 0.25 and temp_opt_time > temp_task_time:
    #                         temp_opt_time = temp_task_time
    #                         idx_opt = idx
    #                 idx = idx + 1
    #                 # best mission found, edit it on list_of_calls, also edit elevator currPos for next iterate
    #
    #             list_of_calls[idx_opt].setAllocatedTo(elev.getID())
    #             elev.setPos(list_of_calls[idx_opt].getDest())
    #             idx = Brain.genericHelpFuncs.gimmieIdxEndOfTask(list_of_calls, idx_opt, temp_opt_time)
    #
    #     else:
    #         idx = idx + 1



    while idx < len(list_of_calls):
        """
        but only on unengaged calls
        """
        if list_of_calls[idx].getAllocatedTo() == -1 and list_of_calls[idx].getDistance() > building.getHeight() * 0.25:
            first_unengaged_call_time = list_of_calls[idx].getStartTime()

            idx_30s = Brain.genericHelpFuncs.gimmie30SecForward(building, elev, list_of_calls, idx)
            idx_opt = idx

            temp_call = list_of_calls[idx_opt]
            temp_opt_time = Brain.genericHelpFuncs.timeToEndTask(elev, temp_call.getSrc(), temp_call.getDest(), 0, 2)
            idx = idx + 1
            while idx != len(list_of_calls) and idx <= idx_30s:
                temp_call = list_of_calls[idx]
                temp_call_start_time = temp_call.getStartTime()
                delta = Brain.genericHelpFuncs.deltaTime(first_unengaged_call_time, temp_call_start_time)
                temp_task_time = Brain.genericHelpFuncs.timeToEndTask(elev, temp_call.getSrc(),
                                                                      temp_call.getDest(), delta, 2)
                if list_of_calls[idx].getAllocatedTo() == -1 and list_of_calls[
                    idx].getDistance() > building.getHeight() * 0.25 \
                        and temp_opt_time > temp_task_time:
                    temp_opt_time = temp_task_time
                    idx_opt = idx
                idx = idx + 1
            # best mission found, edit it on list_of_calls, also edit elevator currPos for next iterate
            list_of_calls[idx_opt].setAllocatedTo(elev.getID())
            elev.setPos(list_of_calls[idx_opt].getDest())
            idx = Brain.genericHelpFuncs.gimmieIdxEndOfTask(list_of_calls, idx_opt, temp_opt_time)

        else:
            idx = idx + 1
