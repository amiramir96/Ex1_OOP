import Ex1Objects.Elevator
import Ex1Objects.CallForElevator
import Brain.TimeAndPathFuncs
import Brain.MergeAndUpdateFuncs


class BrainTeamAlgo:
    def __init__(self, building):
        self.building = building

    def run(self):
        """
        run on all calls
            check if curr call is NOT assigned to an elevator (otherwise, just move to next call)
                get the optimal elev for the task (best time to end mission)\n
                check if possible to merge into this task more tasks with "contained_calls"
                (check that func for more details)\n
                update_calls - update all relevant calls to be allocated, update new time and pos for the chosen elev
        """
        for call in self.building.get_list_of_calls():
            if call.get_allocated_to() == -1:
                # opt_elev is a pair!!! idx 0 = optimal elevator obj, idx 1 = time to end Call by optimal elevator
                opt_elev = Brain.TimeAndPathFuncs.optimal_elevator(self.building.get_list_of_elevator(), call)

                tasks_list = Brain.MergeAndUpdateFuncs.contained_calls(self.building, self.building.get_list_of_calls(),
                                                                       call, opt_elev[0], opt_elev[1])
                Brain.MergeAndUpdateFuncs.update_calls(tasks_list, opt_elev[0], opt_elev[1])
