import random; random.seed(random.randint(-1000, 1000))
import math

from cheese import Cheese
from DNA import DNA
from graphics import *

'''
@author Sakin Kirti
@date 6/27/2022

class to define a mouse which is trying to find the cheese
'''

# global vars - variables to help with indexing
x = 0
y = 1

class Mouse:
    '''
    initialize the Mouse, with position, velocity, acceleration
    '''
    def __init__(self, lifespan, pos_x=0, pos_y=0, top_mice=None):
        # physics variables
        self.position = [pos_x, pos_y] # (x, y) coordinates
        self.velocity = [0, 0] # (x, y) velocity
        self.acceleration = [0, 0] # (x, y) acceleration

        # genetics
        self.DNA = DNA(top_mice, length=lifespan)
        self.counter = 0
        self.lifespan = lifespan
        self.fitness = 0

        # distance to cheese (to optimize)
        self.cheese_to_pos = math.inf

        # display variables
        self.mouse_display = Circle(Point(self.position[x], self.position[y]), 3)
        self.mouse_display.setFill(color='aquamarine')
        self.mouse_display.setOutline(color='aquamarine')

    '''
    apply a force to the acceleration value
    '''
    def add_force(self, force=[0, 0]):
        # set the acceleration
        self.acceleration[x] += force[x]
        self.acceleration[y] += force[y]

    '''
    update the mouse based on the new acceleration value
    '''
    def update_weights(self):
        self.add_force(self.DNA.genes[self.counter])
        self.counter += 1

        self.velocity[x] += self.acceleration[x]
        self.velocity[y] += self.acceleration[y]

        self.position[x] += self.velocity[x]
        self.position[y] += self.velocity[y]

        self.acceleration = [0, 0] # reset acceleration

    '''
    show the mouse to the screen
    '''
    def show(self, window):
        self.mouse_display.move(self.velocity[x], self.velocity[y])

        self.velocity[x] *= 0 # reset velocity after moving
        self.velocity[y] *= 0

        if self.lifespan == self.counter:
            self.mouse_display.undraw()

            self.cheese_to_pos = self.cheese_distance([window.getWidth()/2, window.getHeight()*0.1])
            return 'raised'

        return '' # return something to flag so that the population can be updated

    '''
    start up the mouse
    '''
    def start(self, window):
        self.mouse_display.draw(window)

    '''
    calculate distance from mice
    '''
    def cheese_distance(self, cheese_position):
        # euclidean distance
        return math.sqrt( ((cheese_position[x] - self.position[x])**2) + ((cheese_position[y] - self.position[y])**2) )

    def calc_fitness(self, cheese_position):
        # distance
        distance = math.dist(self.position, cheese_position)
        self.fitness = 1/distance

    '''
    compare two mouse objects by distance to the cheese goal
    @return -1 if other_mouse.cheese_to_pos is greater
    @return 0 if they are equal
    @return 1 if self.cheese_to_pos is greater
    '''
    def compare_to(self, other_mouse):
        return self.cheese_to_pos - other_mouse.cheese_to_pos