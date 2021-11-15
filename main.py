import Ex1Objects.Elevator
import Ex1Objects.Building
import Ex1Objects.CallForElevator
import Brain.BrainTeamAlgo
import json
import csv


def parse_elev(json_name):
    """ construct list of elevators from json file """
    elev_json = open(json_name)
    elev_dict = json.load(elev_json)
    my_first_elev_list = list()
    for E in elev_dict['_elevators']:
        my_first_elev_list.append(Ex1Objects.Elevator.Elevator(E['_id'], E['_speed'], E['_minFloor'],
                                                               E['_maxFloor'], E['_closeTime'], E['_openTime'],
                                                               E['_startTime'], E['_stopTime']))
    return my_first_elev_list


def parse_calls(csv_name):
    """ construct list of Calls from csv file """
    my_first_call_list = list()
    with open(csv_name) as csv_file:
        calls_reader = csv.reader(csv_file)
        # j resemble the index along the list of the call, useful as inner info in the future
        j = 0
        for line in calls_reader:
            my_first_call_list.append(
                Ex1Objects.CallForElevator.CallForElevator(line[1], line[2], line[3], line[4], line[5], j))
            j = j + 1
    return my_first_call_list


def extract_back_to_csv(calls_list,name):
    """ extract CallForElevator list as new csv file, with updated allocated elev column """
    f = open(name, "w")  # name of assigned calls csv

    for y in range(0, len(calls_list) - 1):
        str_c = str(calls_list[y])
        f.write(str_c + "\n")
    str_c = str(calls_list[len(calls_list) - 1])  # last line without \n
    f.write(str_c)
    f.close()


# scenario settings
while True:
    try:
        building_file_string = input("json path for building and elevators: ")
        Building_json = open(building_file_string)
        break
    except:
        print("Wrong file type/path!  Try again.\n")
        continue

Building_dict = json.load(Building_json)
list_of_elevators = parse_elev(building_file_string)
while True:
    try:
        list_of_calls = parse_calls(input("csv path for calls: "))
        break
    except:
        print("Wrong file type/path!  Try again.\n")
        continue
# construct the building! ezpz now :-)
our_building = Ex1Objects.Building.Building(Building_dict['_minFloor'], Building_dict['_maxFloor'], list_of_elevators,
                                            list_of_calls)

# construct our algo and let it do our magic xD (our algorithm is based on greedy algorithm)
greedy_run = Brain.BrainTeamAlgo.BrainTeamAlgo(our_building)
greedy_run.run()
# each call in the list_of_calls is allocated to an elev now, extract this data to a new csv file!
new_file_name="outputCalls1.csv"
extract_back_to_csv(list_of_calls, new_file_name)
print(new_file_name, "created, run completed successfully.")