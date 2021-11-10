import Ex1Objects.Elevator
import Ex1Objects.Building
import Ex1Objects.CallForElevator
import Brain.randomAlgo
import json
import csv

#construct list of elevators from json file
def parseElev(json_name):
    elev_json = open(json_name)
    elev_dict = json.load(elev_json)
    myFirstElevList = list()
    for E in elev_dict['_elevators']:
        myFirstElevList.append(Ex1Objects.Elevator.Elevator(E['_id'], E['_speed'], E['_minFloor'],
                                                            E['_maxFloor'], E['_closeTime'], E['_openTime'], E['_startTime'], E['_stopTime']))
    return myFirstElevList

#construct list of Calls from csv file
def parseCalls(csv_name):
    myFirstCallList = list()
    with open(csv_name) as csv_file:
        calls_reader = csv.reader(csv_file)
        #j resemble the index along the list of the call, can be usefull as inner info in the future
        j = 0
        for line in calls_reader:
            myFirstCallList.append(
                Ex1Objects.CallForElevator.CallForElevator(line[1], line[2], line[3], line[4], line[5], j))
            j = j + 1
    return myFirstCallList

#extract ea CallForElevator as same format to new csv file, with updated allocated elev
def extractBackToCSV(list_of_calls):
    f = open("outputCalls.csv", "w")
    for y in range(0, len(list_of_calls) - 1):
        strC = str(list_of_calls[y])
        # print(strC, cList[y].getId())
        f.write(strC + "\n")
    strC = str(list_of_calls[len(list_of_calls) - 1])
    f.write(strC)
    f.close()

building_file_string = input("set json file name or/and directory for building and elevators: ")
Building_json = open(building_file_string)
Building_dict = json.load(Building_json)
# print(Building_dict)
list_of_elevators = parseElev(building_file_string)
list_of_calls = parseCalls(input("set csv file name or/and directory for calls: "))
#construct the building! ezpz now :-)
our_building = Ex1Objects.Building.Building(Building_dict['_minFloor'], Building_dict['_maxFloor'], list_of_elevators, list_of_calls)
#construct our algo and let it do our magic xD
first_run = Brain.randomAlgo.randomAlgo(our_building)
first_run.run()
#ea call in the list_of_calls is allocated to any elev now, we shall extract this data to new csv file!
extractBackToCSV(list_of_calls)