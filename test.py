from graphics import *

window = GraphWin('test', width=500, height=500, autoflush=True)

#window.yUp()

head = Circle(Point(40,100), 25)
head.setFill("yellow")
head.draw(window)

message = Text(Point(window.getWidth()/2, 20), 'Click anywhere to quit.')
message.draw(window)
window.getMouse()
window.close()