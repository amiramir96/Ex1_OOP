# Ex1_OOP
Object Oriented Programming exercise 1

in this assigment we were required to create an offline algorithm and code it in python for elevator system in a building, every mission for moving a given elevator from floor x to y will be named as call.
in this assigment we required to: get B.json, Calls.csv files which represents the building and all the calls for the given scenario, in return, the algo have to output a calls.csv file that the column which represent the elevator that engage the call is edited.

# algorithm logic
this algorithm will combine several principles togheter:
1- Greed system: given a call, the elevator which will end the call as fast as possible will be choosen.
2- Consitency: since a call as been allocated to an elevator - this decision wont change furthermore, the call wont be checked again.
3- Cost-Benefit tradeoff: given terms is taking place - there will be more efficient to "merge" calls which means - the choosen elevator will stop meanwhile a call is on, for finishing togheter one or more another calls.

# structre of the project code
in this assigment we will create the following packages of files:

|   package name: |                                                     **Ex1Objects**                                                                                       |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **file name**   |      **description**                                                                                                                                     |     
| CallForElevator |       represent a call for an elevator, will hold all the parameters which we get as input from our school tester and some inner functions that helps to |    |                 |         orginize better the data of the call                                                                                                             | 
|    Elevator     |          represent a elevator, will hold all the parameters and data we shall need to maintain and operating an elevator                                 |
|   Building      |         represent a building, will hold list of elevators and list of calls either the basic parameters of building (aka min and max floor)              | 


|   package name: |                                                     **Brain**                                                                                            |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **file name**   |      **description**                                                                                                                                     |   
| BrainTeamAlgo   |       the algorithm itself, hold the whole chain proccess                                                                                                |   
|generalHelpFuncs |          holds all the generic functions that help to the algorithm proccess                                                                             |


there is also Ex1_checker_V1.2_obf.jar which simulates the elevator system moving along the building, and represent the results of the scenario for the return csv output file.

# Testing
this project is tested by unitest libary, the tests can be run by IDE workspace. 
the package name Tests hold all the tests files, which tests ea every object and function that gonna be used along the algorithm project run (the main of them mentioned above).

# Running the simulation 
Run the Main.py file in a directory containing 'Brain', 'Ex1Objects', relevant Building json and csv with calls.  
You will be asked to provide the names of the relevant json and csv files.  
The csv with the results (same calls but allocated to elevators) will be created in the directory.  
Default name for output is "outputCalls1.csv", custom names can be created inside main.py.  

# Results
this is the best results that we were able to gain:
|Case |Building|Uncompleted calls| average waiting time per call|
|a    |B1.json |                 |                              |
|a    |B2.json |                 |                              |
|a    |B3.json |                 |                              |
|a    |B4.json |                 |                              |
|a    |B5.json |                 |                              |
|b    |B2.json |                 |                              |
|b    |B3.json |                 |                              |
|b    |B4.json |                 |                              |
|b    |B5.json |                 |                              |  
|c    |B2.json |                 |                              |
|c    |B3.json |                 |                              |
|c    |B4.json |                 |                              |
|c    |B5.json |                 |                              | 
|d    |B2.json |                 |                              |
|d    |B3.json |                 |                              |
|d    |B4.json |                 |                              |
|d    |B5.json |                 |                              |

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
