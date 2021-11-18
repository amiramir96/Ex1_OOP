# Ex1_OOP
Object Oriented Programming exercise 1

in this assigment we were required to create an offline algorithm and code it in python for smart elevator system in a building, every mission for moving a given elevator from floor x to y will be named as call. <br>
in this assigment we are required to: get B.json, Calls.csv files which represents the building and all the calls for the given scenario, in return, the algo have to output a calls.csv file with elevator allocated to each call in the last column.

A literature overview about elevator's algorithms from Ex0 is attached.
we reccomend to upen the diagram.uml by pycharm program with the plugin "diagram" !

# Algorithm logic
the algorithm will combine several principles togheter:  
<o1>
  1. Greedy algorithm: given a call, the elevator which will end the call as fast as possible will be choosen.</li>  
  2. Consistency: when a call is allocated to an elevator - it won't be allocated again. furthermore, the call wont be checked again.</li>  
  3. Cost-Benefit tradeoff: when certain conditions apply - we will "merge" several calls, which means - the chosen elevator will complete multiple calls at once.</li>  
  however, we won't merge many calls together to avoid streching the original call for too long.</li>
</o1>
  
# Algorithm Overview
  
diagram of the algorithm and code:
![image](https://user-images.githubusercontent.com/89981387/142495871-60d6e0f5-3c26-4684-a4e8-e4da6cc18246.png)

the algorithm works consistenly by the following steps:
<o1>
  1. get input of building (json) file that holds building and elevator data and input of calls (csv) file then construct the algorithm object. 
  2. the algorithm will scan one by one the calls of the scenario, from the first to the last. 
  3. bid process - let alpha be a curr call that the algorithm checks which is NOT allocated to any elevator yet (if its already allocated, the algo will jump to next call on the list), the algo will use optimal_elevator function that will return the elevator that will end the call as soon as possible compared to the other elevators. 
  4. merge check proccess - the chosen elevator will be sent for the merge proccess check via the contained_calls function that will return a list of all the calls that are contained in the superior call - alpha. call beta is contained if: <br>
 
        <br>a. the potential future return list size is less than a certain parameter (depends on building height, elev spped, elev delay times) <br>
            b. beta startTime is lower from the time that will take to the elevator to complete alpha task  <br>
            c. time that takes the elevator to move from elev.pos -> alpha.srcFloor -> beta.srcFloor is higher than beta.startTime <br>
            d. alpha.type of task is same as beta.type (Up/Down) <br>
            e. alpha.src <= beta.src <= beta.dest <= alpha.dest. beta is fully contained in alpha`s path. <br>  <br>
  5. the calls that will be engaged along the same path via the returned list will be allocated to the chosen elevator (section 3) 
  6. the chosen elevator parameters of currect Floor and currect Time will be updated to: elevator.currFloor <- alpha.destFloor , elevator.currTime <- time_to_end_alpha_task + (amount_of_stops * elevator.delayTime) 
  7. continue to the next call in list_of_calls and return to section 2 (until we arrived at the end of the list)
  8. extract the allocated calls to a new csv file.
</o1>

# Structre of the project code
in this assigment we will create the following packages of files:

|   package name: |                                                     **Ex1Objects**                                                                                       |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **file name**   |      **description**                                                                                                                                     |   
| CallForElevator |      represents a call for an elevator, will hold all the parameters which we get as input from our school tester and some inner functions that helps to |    |                 |         orginize better the data of the call                                                                                                             | 
|    Elevator     |        represents an elevator, will hold all the parameters and data we will need to maintain and operate an elevator                                    |
|   Building      |        represents a building, will hold list of elevators, list of calls and the basic parameters of building (aka min and max floor)                    | 


|   package name:    |                                                  **Brain**                                                                                            |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **file name**      |      **description**                                                                                                                                  |   
| BrainTeamAlgo      |       the algorithm itself, holds the whole chain proccess                                                                                            |   
|MergeAndUpdateFuncs |         holds functions that supports the Merge and Updating(elevator and calls parms) functions                                                      |
|TimeAndPathFuncs    |          holds functions that calculate path and time period of tasks for elevators                                                                   |

The Ex1.py file is the file that activates our algorithm. (the main function is there)  

there is also Ex1_checker_V1.2_obf.jar  in 'jar score test' which simulates the elevator system moving along the building, and prints the results of the scenario for the processed csv output file.


# Testing
this project is tested by unitest libary, the tests can be run with an IDE workspace.  
the package named Tests holds all the test files, we tested every object and function that gonna be used along the project run (the main.py file).

# Running the simulation 
Run the Ex1.py file in a directory containing 'Brain', 'Ex1Objects', relevant Building json and csv with calls.  <br>
Use the following code template to run Ex1:  <br>
the simultor jar file is waiting at "[https://github.com/amiramir96/Ex1_OOP/tree/main/jar%20score%20test](url)"
```
python Ex1.py <Building json> <Calls csv> <output name>
```
The csv with the results (same calls but allocated to elevators) will be created in the directory.   <br>

Running the algorithm example:
```
python Ex1.py B1.json C2.csv out.csv
```
Running the test code example:
```
java -jar Ex1_checker_V1.2_obf.jar 1111,2222,3333 B2.json Ex1_Calls_case_2_b.csv out.log
```

# Results
this is the best results that we were able to gain:
|Case |Building|Uncompleted calls| average waiting time per call (seconds)|
|-----|--------|------------------|---------------------------------|
|a    |B1.json |       0          |       112                       |
|a    |B2.json |       0          |      40                         |
|a    |B3.json |        0         |            27                   |
|a    |B4.json |        0         |      18                         |
|a    |B5.json |        0         |         11                      |
|b    |B4.json |       2          |           160                   |
|b    |B5.json |       0          |               40                |  
|b    |B9.json |       0          |               67                |
|c    |B4.json |       2          |            158                  |
|c    |B5.json |       0          |               39                | 
|d    |B4.json |       0          |             155                 |
|d    |B5.json |       0          |               39                |
|d    |B9.json |       0          |               68                |
|g    |B7.json |       20         |               188               |

little nore - B9 is building of stage 9 from Ex0 (similiar to B5 but with some slower elevators), B7 is building of stage 7 from Ex0 and case g is same as stage 7 case of Ex0

# Assigment instructions

project files:  
https://github.com/amiramir96/Ex1_OOP  
reporting form:  
https://docs.google.com/forms/d/e/1FAIpQLSffojCP9ftLSlk58_opDf-OpcLXvmuYzoQ3N_EQGtfozXjfjA/viewform?usp=sf_link  
reported results by students:  
https://docs.google.com/spreadsheets/d/1fyFWvU_8d8UeaiUdyDujfgvt2dMs2mzzLd9QgUb33Wc/edit?usp=sharing  
link to our course teacher assigment github:  
https://github.com/benmoshe/OOP_2021/tree/main/Assignments/Ex1  

the project designed and created by Amir.S and Ori.D
