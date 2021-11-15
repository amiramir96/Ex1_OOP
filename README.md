# Ex1_OOP
Object Oriented Programming exercise 1

in this assigment we were required to create an offline algorithm and code it in python for smart elevator system in a building, every mission for moving a given elevator from floor x to y will be named as call. 
in this assigment we are required to: get B.json, Calls.csv files which represents the building and all the calls for the given scenario, in return, the algo have to output a calls.csv file with elevator allocated to each call in the last column.

# algorithm logic
the algorithm will combine several principles togheter:  
  1. Greedy algorithm: given a call, the elevator which will end the call as fast as possible will be choosen.  
  2. Consistency: when a call is allocated to an elevator - it won't be allocated again. furthermore, the call wont be checked again.  
  3. Cost-Benefit tradeoff: when certain conditions apply - we will "merge" several calls, which means - the chosen elevator will complete multiple calls at once.  
  however, we won't merge many calls together to avoid streching the original call for too long.

# structre of the project code
in this assigment we will create the following packages of files:

|   package name: |                                                     **Ex1Objects**                                                                                       |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **file name**   |      **description**                                                                                                                                     |     
| CallForElevator |      represents a call for an elevator, will hold all the parameters which we get as input from our school tester and some inner functions that helps to |    |                 |         orginize better the data of the call                                                                                                             | 
|    Elevator     |        represents an elevator, will hold all the parameters and data we will need to maintain and operate an elevator                                 |
|   Building      |        represents a building, will hold list of elevators, list of calls and the basic parameters of building (aka min and max floor)              | 


|   package name: |                                                     **Brain**                                                                                            |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **file name**   |      **description**                                                                                                                                     |   
| BrainTeamAlgo   |       the algorithm itself, holds the whole chain proccess                                                                                               |   
|generalHelpFuncs |          holds all the generic functions that help to the algorithm proccess                                                                             |

The main.py file is the file that activates our algorithm.  
this file will build the building and allocate elevators to every call in a given csv file, outputing an updated file.
Running the algorithm example:
```
python Ex1.py B1.json C2.csv out.csv
```

there is also Ex1_checker_V1.2_obf.jar which simulates the elevator system moving along the building, and prints the results of the scenario for the processed csv output file.
Running the test code template:
```
java -jar Ex1_checker_V1.2_obf.jar 1111,2222,3333 B2.json Ex1_Calls_case_2_b.csv out.log
```

# Testing
this project is tested by unitest libary, the tests can be run with an IDE workspace.  
the package named Tests holds all the test files, we tested every object and function that gonna be used along the project run (the main.py file).

# Running the simulation 
Run the Main.py file in a directory containing 'Brain', 'Ex1Objects', relevant Building json and csv with calls.  
You will be asked to provide the paths of the relevant json and csv files.  
The csv with the results (same calls but allocated to elevators) will be created in the directory.  
Default name for output is "outputCalls1.csv", custom names can be created inside main.py.  

# Results
this is the best results that we were able to gain:
|Case |Building|Uncompleted calls| average waiting time per call (seconds)|
|-----|--------|------------------|---------------------------------|
|a    |B1.json |       0          |       112                       |
|a    |B2.json |       0          |      43                         |
|a    |B3.json |        0         |            27                   |
|a    |B4.json |        0         |      18                         |
|a    |B5.json |        0         |         11                      |
|b    |B4.json |       8          |           185                   |
|b    |B5.json |       0          |               44                |  
|b    |B9.json |       0          |               67                |
|c    |B4.json |       2          |            176                  |
|c    |B5.json |       0          |               41                | 
|c    |B9.json |       0          |               72                |
|d    |B4.json |       8          |             185                 |
|d    |B5.json |       0          |               44                |
|d    |B9.json |       0          |               67                |
|g    |B7.json |       19         |               202               |

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
