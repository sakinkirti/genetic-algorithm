import random

'''
@author Sakin Kirti
@date 6/27/2022

class to define the DNA that the mouse has
'''

# global
x = 0
y = 1

class DNA:

    '''
    initialize the DNA, carrying the genetic information for the mouse
    '''
    def __init__(self, top_mice=None, length=200):
        self.genes = []
        self.length = length

        # set the genes
        if top_mice is None:
            for i in range(self.length):
                rand_x_dir = random.random() * 20 - 10 # should result in random number between (5, 5)
                rand_y_dir = random.random() * 20 - 10
                self.genes.append([rand_x_dir, rand_y_dir])
        else:
            self.reproduce(top_mice)

    '''
    mutate the top_mouse genese
    '''
    def reproduce(self, top_mice):
        # unpack
        male, female = top_mice

        # iterate through top_mouse and set self.genes to something similar
        gamete = self.generate_gamete(male, female)
        # gamete = self.mutate(gamete)
        self.genes = gamete

    '''
    simulate crossover event and choose one set of genes to send back
    '''
    def generate_gamete(self, male, female):
        # generate a number of crossover events
        num_events = random.randint(0, 5)

        # find the places to switch genes at
        locs = [random.randint(0, self.length) for i in range(num_events)]
        locs.sort()

        # splice genes
        for i in range(num_events):
            temp = male[locs[i]:]
            male = male[:locs[i]] + female[locs[i]:]
            female = female[:locs[i]] + temp

        # return one of the gametes
        if num_events % 2 == 0:
            return male
        else:
            return female

    '''
    some slight mutations
    '''
    def mutate(self, gamete):
        # iterate through the genes and introduce some slight variation
        for nucleotide in gamete:
            nucleotide[x] += random.random() * 10 - 5
            nucleotide[y] += random.random() * 10 - 5

        return gamete