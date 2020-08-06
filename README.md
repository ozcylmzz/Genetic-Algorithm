# Genetic Algorithm
 
Matrix: Created square world. Matrise food assignments are made.
In this matrix;
with the position of the person (-1),
with food (1),
other frames are denoted by (0).

The itsDone variable is initialized as 0. The program enters a loop that will continue as long as this variable is 0.
The initial matrix is formed with path = creatPath ().
As much as the determined number of iterations, the following operations are repeated.
For each person in the continuing cycle until the number of paths
Fitness () function is calculated by calling the suitability.
The selection () function selects persons who are eligible to create the next generation.
crossover () function is cross-crossed between selected persons.
Persons are mutated according to the determined rate.
If among persons eating all food, itsDone variable 1 is initially set to 0. Thanks to this, it comes out of the outer loop.
Before the end of the program, the information of the generation where the result is found and the path followed by the person who finds the result is printed.
This ensures that the program works until you find a result.

Hyperparameter Review:

Mutation Rate: Mutation rate 0.01 * number of roads * Number of meals with the number of meals to achieve success on the matrix of the same size without changing places, Mutation rate When 0.1 * the number of paths * the number of meals, it drops up to 50 generations. When mutation rate is 0.5 * road number * number of meals, too much chromozone is mustated, good persons also fail or die. Therefore, the success rate of persons decreases when the mutation rate is too low or too high compared to the problem.

Distribution of food: The location of the food is important, as well as the number of meals. Speaking about the same number of meals, the number of routes and the number of moves, the food being far apart increases the number of generations. The problem at this moment can reach the solution by increasing the number of moves. 
As the matrix grew and the number of meals increased and the distances increased, the success of persons was very low. Speaking for this example, when the number of routes and moves is increased, it becomes difficult to reach the solution. In this case, changing the number of iterations may bring it closer to the solution.

https://www.youtube.com/watch?v=RTbcsWFLUNc
