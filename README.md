# Ex1_OOP
Object Oriented Programming exercise 1

in this assigment we were required to create an offline algorithm and code it in python for elevator system in a building, every mission for moving a given elevator from floor x to y will be named as call.

# algorithm logic:
this algorithm will combine several principles togheter:
1- Greed system: given a call, the elevator which will end the call as fast as possible will be choosen.
2- Consitency: since a call as been allocated to an elevator - this decision wont change furthermore, the call wont be checked again.
3- Cost-Benefit tradeoff: given terms is taking place - there will be more efficient to "merge" calls which means - the choosen elevator will stop meanwhile a call is on, for finishing togheter one or more another calls.

in this assigment we will create the following packages of files:

|                                                   package name:      Ex1Objects                                                                                            |
| file name       |      description                                                                                                                                         |     
| CallForElevator |       represent a call for an elevator, will hold all the parameters which we get as input from our school tester and some inner functions that helps to |     |                 |         orginize better the data of the call                                                                                                             | 
|    Elevator     |          represent a elevator, will hold all the parameters and data we shall need to maintain and operating an elevator                                 |
|   Building      |         represent a building, will hold list of elevators and list of calls either the basic parameters of building (aka min and max floor)              | 
