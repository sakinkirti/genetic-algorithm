import random

from mouse import Mouse

'''
@author Sakin Kirti
@date 6/27/2022

class to define a set of Mice
structured as an array holding multiple mouse objects
'''

class Population:
    '''
    initialize the population
    '''
    def __init__(self, window, top_mice, lifespan, population_size=10):
        self.mice = []
        self.population_size = population_size
        self.mating_pool = []

        # at first, initialize the mice randomly
        if len(top_mice) == 0:
            for i in range(self.population_size):
                self.mice.append(Mouse(lifespan, pos_x=window.getWidth()/2, pos_y=window.getHeight()*0.90))
        # per generation, initialize the mice with top_mice DNA
        else:
            for i in range(self.population_size):
                partners = [top_mice[random.randint(0, len(top_mice)-1)], top_mice[random.randint(0, len(top_mice)-1)]]
                self.mice.append(Mouse(lifespan, pos_x=window.getWidth()/2, pos_y=window.getHeight()*0.90, top_mice=partners))

    '''
    show the mice to the display
    '''
    def display(self, window):
        flag = ''
        top_mice = []

        # iterate and update weights
        for mouse in self.mice:
            mouse.update_weights()
            flag = mouse.show(window)

        # if the flag is raised, isolate the top 25% of mice
        if flag == 'raised':
            # sort mice based on distance to cheese
            for i in range(self.population_size-1):
                min_index = i
                for j in range(i+1, self.population_size-1):
                    if self.mice[j].cheese_to_pos < self.mice[min_index].cheese_to_pos:
                        min_index = j
                self.mice[i], self.mice[min_index] = self.mice[min_index], self.mice[i]

            # isolate top 10% of mice
            top_mice = self.mice[0:int(0.1*self.population_size)]

        return top_mice

    '''
    draw the mice for the first time
    '''
    def start(self, window):
        # iterate and show the mice
        for mouse in self.mice:
            mouse.start(window)

    '''
    test fitness of the mice
    '''
    def evaluate_mice(self, cheese_position):
        # fitness calculation
        max_fit = 0
        for mouse in self.mice:
            mouse.calc_fitness(cheese_position)
            max_fit = mouse.fitness if mouse.fitness > max_fit else max_fit

        # normalize
        for mouse in self.mice:
            mouse.fitness /= max_fit

        # add to mating pool based on fitness
        for mouse in self.mice:
            n = mouse.fitness * 100
            for i in range(n):
                self.mating_pool.append(mouse)

    '''
    select parents
    '''
    def select_parents(self):
        parent_a = self.mating_pool[random.randint(0, len(self.mating_pool))].DNA
        parent_b = self.mating_pool[random.randint(0, len(self.mating_pool))].DNA
        child = parent_a.crossover(parent_b)