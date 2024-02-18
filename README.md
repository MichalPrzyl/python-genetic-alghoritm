# Genetic Algorithm for Finding the Closest Number to a Target

This Python script implements a genetic algorithm to find the number closest to a predefined target number from a list of random numbers.

## Algorithm Overview

The genetic algorithm works as follows:

1. **Initialization**: A population of random numbers is generated.
2. **Evaluation**: Each number in the population is evaluated to determine its fitness, i.e., how close it is to the target number.
3. **Selection**: Individuals from the population are selected for reproduction based on their fitness. Individuals that are closer to the target number have a higher chance of being selected.
4. **Mutation**: Offspring undergo mutation, introducing small random changes to their genetic material. This step helps maintain diversity in the population.
5. **Replacement**: The offspring population replaces the parent population.
6. **Termination**: The algorithm terminates when a stopping criterion is met (e.g., reaching a maximum number of generations or finding a solution with satisfactory fitness).

## Usage


1. **Run the Script**: Execute the `script.py` script using Python. You can't adjust parameters such as population size, mutation rate, and the target number within the script itself but maybe in the future.
