"""

        Problem set 6 test


"""

width = 15
height = 20
speed = 1.0


 ##creating room

from ps6 import *

room = RectangularRoom(width,height)


def checkPosition(rooms):
    for pos,cleaned in rooms.roomTiles.iteritems():
        print("Position: x=",str(pos.getX()),", y=",str(pos.getY()),", isCleaned = ",str(cleaned))

def getCleanedTileLocation(rooms):
    for pos,cleaned in rooms.roomTiles.iteritems():
        if cleaned:
            print("Position: x=",str(pos.getX()),", y=",str(pos.getY()),", isCleaned = ",str(cleaned))


##checkPosition(room)
robo  = Robot(room, speed)
pos = robo.getRobotPosition()
direction = robo.getRobotDirection()
print("Now Robo Position: x=",pos.getX(),', y=',pos.getY(),', direction= ',str(direction))
print(room.isPositionInRoom(pos))
robo.updatePositionAndClean()
getCleanedTileLocation(room)
