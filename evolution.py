import time

from population import Population
from cheese import Cheese
from mouse import Mouse

from graphics import *

'''
@author Sakin Kirti
@date 6/27/2022

script to bring all of the components of the genetic algorithm together
'''

def main():
    print('STARTING UP GENETIC ALGORITHM')

    # create graphics
    window = GraphWin(title='Genetic Algorithm Demo', width=1000, height=800, autoflush=True)
    window.setBackground(color='black')
    bounding_box = Rectangle(Point(window.getWidth()*0.05, window.getHeight()*0.05), Point(window.getWidth()*0.95, window.getHeight()*0.95))
    bounding_box.setOutline(color='white')
    bounding_box.draw(window)

    # create objects
    cheese = Cheese(window); cheese.start(window)
    lifespan = 100
    top_mice = []

    for i in range(10000):
        if i % lifespan == 0:
            population = Population(window, top_mice, lifespan, population_size=20)
            population.start(window)

        top_mice = population.display(window)

    window.getMouse()
    window.close()

if __name__ == '__main__':
    main()
