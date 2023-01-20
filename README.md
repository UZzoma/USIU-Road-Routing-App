# USIU-Road-Routing-App
 An application that acts as a USIU map to help visitors find routes between buildings.


 ## Problem Statement
- To design an application that acts as a USIU map to help visitors find routes between buildings.
Objectives
- To design a USIU map with the use of Python that solve the problem stated above
- To ensure the system meet the goals specified in the problem statement
- To explicitly state the assumption made during the system development process.
- To avail evidence of project implementation

## Procedure 
The system was implemented using the termcolor, operator,  and random libraries. The location mapping was implemented using graphs and the dictionaries as data structures. The cost of traversing a certain location was implemented in second and the data was stored in a dictionary. Heuristics were calculated and stored in a dictionary. The A* algorithm was the informed search algorithm chosen to implement the solution which uses both the cost and the heuristics to calculate the optimal route. 
State: The starting location. It could be any location in USIU
Action: The steps required to reach the goal.
Goal Test: Has the route to the requested destination been found.
Path Cost: Sum of distance and heuristics to the required location.

## Assumptions 
Heuristics: The nodes, School of Communication and Cinematic Art,  was the centre point on the map. It has the most neighbours; thus, it was used to calculate heuristics using the Manhattan distance from the goal( It is admissible and consistent). Cost was implemented in seconds(During peak hours). 


