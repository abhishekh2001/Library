import numpy as np
import random
from misc import *
"""Defines all the available selection methods"""
import sys
import numpy as np

def proportional_roulette_wheel(population):
    """ Performs roulette wheel selection:
    every individual can become a parent with a 
    probability which is proportional to its fitness.
    Selects one parent.

    Args:
        population(list): List containing fitness values of individuals
    
    Returns:
        int: Index of parent chosen
    """

    # Compute the total fitness of population
    sum_fitness = sum([entity_fitness for entity_fitness in population])

    # Each entity in population is given a probability
    # to become a parent proportional to the fitness of the
    # individual
    selection_probabilities = [entity_fitness/sum_fitness for entity_fitness in population]

    # Select the index of the parent chosen using the
    # probabilities computed for each individual in the population
    parent_ind = np.random.choice(len(population), p=selection_probabilities)
    return parent_ind

def stochastic_universal_sampling(population, N):
    """SUS uses a single random value to sample all of the solutions by 
    choosing them at evenly spaced intervals, giving
    weaker members of the population (according to their fitness) 
    chance to be chosen.
    Produces a parent pool of size N

    Args:
        population (List): List containing fitness values of individuals
        N (int): Number of parents
    
    Returns:
        list: The indices of parents
    """

    # https://stackoverflow.com/questions/22749132/stochastic-universal-sampling-ga-in-python
    # https://en.wikipedia.org/wiki/Stochastic_universal_sampling
    wheel = makeWheel(population)
    stepSize = 1.0/N
    answer = []
    r = random.random()

    answer.append(binSearch(wheel, r))

    # step through
    while len(answer) < N:
        r += stepSize
        if r>1:
            r %= 1
        answer.append(binSearch(wheel, r))
    return answer


def classic_linear_rank(population_fitness):
    """ RWS will have problems when the finesses differs very much. 
    Outstanding individuals will introduce a bias in the beginning 
    of the search that may cause a premature convergence and a loss 
    of diversity.

    http://www.ijmlc.org/papers/146-C00572-005.pdf

    Args:
        population_fitness(list): List containing fitness values of individuals
    
    Returns:
        int: Index of parent chosen
    """
    
    # Get the number of individuals in the population.
    n = len(population_fitness)

    # (sum of integers 1 to N).
    rank_sum = n * (n + 1) / 2

    # Create ranks
    array = np.array(population_fitness)
    order = array.argsort()
    ranks = order.argsort()

    return proportional_roulette_wheel(ranks)

def tournament_selection(pop,fitness,k):
    '''
    Input: population,fitness and a number k.
    Output: the function conducts tournaments between k individuals randomly and selects the best
    ''' 
    N = np.size(pop)
    best = -1
    fit  = -sys.maxsize-1
    for _ in range(1,k):
        ind = pop[np.random.randint(0, N)]
        if (fit == -1) or fitness[ind] > fitness[best]:
            best = ind
            fit = fitness[ind]
    return best

def boltzmann_selection(temp_gene , fitness , pop):
    #TODO: Fill function
    pass

