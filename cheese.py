from graphics import *

'''
@author Sakin Kirti
@date 6/28/2022

class to define the goal object that the mice are trying to find
'''

class Cheese:
    '''
    initialize the object
    '''
    def __init__(self, window):
        self.position = [window.getWidth()/2, window.getHeight()*0.1]

        # display cheese
        self.cheese_display = Rectangle(Point(self.position[0]-10, self.position[1]+10), Point(self.position[0]+10, self.position[1]-10))
        self.cheese_display.setFill(color='yellow')
        self.cheese_display.setOutline(color='yellow')

    '''
    get the cheese position
    '''
    def get_position(self):
        return [self.position[0], self.position[1]]

    '''
    display the cheese
    '''
    def start(self, window):
        self.cheese_display.draw(window)
