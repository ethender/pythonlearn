# Problem Set 6: Simulating robots
# Name:
# Collaborators:
# Time:

import math
import random

import ps6_visualize
import pylab

# === Provided classes

class Position(object):
    """
        A Position represents a location in a two-dimensional room.
        """
    def __init__(self, x, y):
        """
            Initializes a position with coordinates (x, y).
            """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self,x):
        self.x = x
    def setY(self, y):
        self.y = y
    def getNewPosition(self, angle, speed):
        """
            Computes and returns the new Position after a single clock-tick has
            passed, with this object as the current position, and with the
            specified angle and speed.
            
            Does NOT test whether the returned position fits inside the room.
            
            angle: float representing angle in degrees, 0 <= angle < 360
            speed: positive float representing speed
            
            Returns: a Position object representing the new position.
            """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = int(old_x + delta_x)
        new_y = int(old_y + delta_y)

        ##rounding off
##        new_x = int(math.ceil(new_x))
##        new_y = int(math.ceil(new_y))
        return Position(new_x, new_y)
    def __str__(self):
        ##print("X Axis: ",self.x," Y Axis: ",self.y)
        return "X Axis: ",self.x," Y Axis: ",self.y
    def __eq__(self, other):
        return self.getX() == other.getX() and self.getY() == other.getY()

# === Problems 1

class RectangularRoom(object):
    """
        A RectangularRoom represents a rectangular region containing clean or dirty
        tiles.
        
        A room has a width and a height and contains (width * height) tiles. At any
        particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
            Initializes a rectangular room with the specified width and height.
            
            Initially, no tiles in the room have been cleaned.
            
            width: an integer > 0
            height: an integer > 0
        """
        self.roomTiles = {}
        ##raise NotImplementedError
        for i in range(width):
            for j in range(height):
                temp = Position(i,j)
                self.roomTiles[temp]=False



    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        
        Assumes that POS represents a valid position inside this room.
        
        pos: a Position
        """
            #raise NotImplementedError
        if not self.isTileCleaned(pos.getX(),pos.getY()):
            self.roomTiles[pos] = True
        
        
    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.
        
        Assumes that (m, n) represents a valid tile inside the room.
        
        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        # raise NotImplementedError
        for pos,isCleaned in self.roomTiles.iteritems():
            if pos.getX() == m and pos.getY() == n:
                return isCleaned
        return False

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.
        
        returns: an integer
        """
        #raise NotImplementedError
        return len(self.roomTiles)
            
    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.
        
        returns: an integer
        """
        #raise NotImplementedError
        numTilesCleaned = 0
        for pos, cleaned in self.roomTiles.iteritems():
            if cleaned:
                numTilesCleaned += 1
        return numTilesCleaned

    def getRandomPosition(self):
        """
        Return a random position inside the room.
        
        returns: a Position object.
        """
        #raise NotImplementedError
        return random.choice(self.roomTiles.keys())

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.
        
        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        #raise NotImplementedError
        #return self.roomTiles.has_key(pos)
        for roomPos in self.roomTiles.keys():
            if roomPos == pos:
                return True
        return False


class Robot(object):
    """
        Represents a robot cleaning a particular room.
        
        At all times the robot has a particular position and direction in the room.
        The robot also has a fixed speed.
        
        Subclasses of Robot should provide movement strategies by implementing
        updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
            Initializes a Robot with the given speed in the specified room. The
            robot initially has a random direction and a random position in the
            room. The robot cleans the tile it is on.
            
            room:  a RectangularRoom object.
            speed: a float (speed > 0)
        """
        #raise NotImplementedError
        self.room = room
        self.speed = speed
        self.direction = random.choice(range(360))
        self.position = self.room.getRandomPosition()
    
    def getRobotPosition(self):
        """
            Return the position of the robot.
            
            returns: a Position object giving the robot's position.
        """
        #raise NotImplementedError
        return self.position
    
    def getRobotDirection(self):
        """
            Return the direction of the robot.
            
            returns: an integer d giving the direction of the robot as an angle in
            degrees, 0 <= d < 360.
        """
        #raise NotImplementedError
        return self.direction
    
    def setRobotPosition(self, position):
        """
            Set the position of the robot to POSITION.
            
            position: a Position object.
        """
        #raise NotImplementedError
        self.position = position
    
    def setRobotDirection(self, direction):
        """
            Set the direction of the robot to DIRECTION.
            
            direction: integer representing an angle in degrees
        """
        #raise NotImplementedError
        self.direction = direction
    
    def updatePositionAndClean(self):
        """
            Simulate the raise passage of a single time-step.
            
            Move the robot to a new position and mark the tile it is on as having
            been cleaned.
        """
        #raise NotImplementedError
        
        """
            1. first clean first position
            2. update the next position
                a. if next position available then update
                b. else search for next position
        """
        self.room.cleanTileAtPosition(self.position)
        pos = self.position.getNewPosition(self.direction,self.speed)
        print('Next position: x=',pos.getX(),' y=',pos.getY())
        if self.room.isPositionInRoom(pos):
            self.setRobotPosition(pos)
        else:
            print("position is not in room")
            



# === Problem 2
class StandardRobot(Robot):
    """
        A StandardRobot is a Robot with the standard movement strategy.
        
        At each time-step, a StandardRobot attempts to move in its current direction; when
        it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):
        """
            Simulate the passage of a single time-step.
            
            Move the robot to a new position and mark the tile it is on as having
            been cleaned.
        """
        ##raise NotImplementedError
        self.room.cleanTileAtPosition(self.position)
        nextXDirection = Position(self.position.getX()+1,self.position.getY())
        nextYDirection = Position(self.position.getX(),self.position.getY()+1)
        if self.room.isPositionInRoom(nextXDirection) :
            self.setRobotPosition(nextXDirection())
        elif self.room.isPositionInRoom(nextYDirection):
             self.setRobotPosition(nextYDirection())
        else:
            pos = self.position.getNewPosition(self.direction,self.speed)
        
            print('Next position: x=',pos.getX(),' y=',pos.getY())
            if self.room.isPositionInRoom(pos):
                self.setRobotPosition(pos)
            else:
                print("position is not in room")
            
        
        

# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
        Runs NUM_TRIALS trials of the simulation and returns the mean number of
        time-steps needed to clean the fraction MIN_COVERAGE of the room.
        
        The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
        speed SPEED, in a room of dimensions WIDTH x HEIGHT.
        
        num_robots: an int (num_robots > 0)
        speed: a float (speed > 0)
        width: an int (width > 0)
        height: an int (height > 0)
        min_coverage: a float (0 <= min_coverage <= 1.0)
        num_trials: an int (num_trials > 0)
        robot_type: class of robot to be instantiated (e.g. Robot or
        RandomWalkRobot)
    """
     #raise NotImplementedError
  
    
    

# === Problem 4
#
# 1) How long does it take to clean 80% of a 20×20 room with each of 1-10 robots?
#
# 2) How long does it take two robots to clean 80% of rooms with dimensions
#	 20×20, 25×16, 40×10, 50×8, 80×5, and 100×4?

def showPlot1():
    """
        Produces a plot showing dependence of cleaning time on number of robots.
        """ 
    raise NotImplementedError

def showPlot2():
    """
        Produces a plot showing dependence of cleaning time on room shape.
        """
    raise NotImplementedError

# === Problem 5

##class RandomWalkRobot(Robot):
##    """
##        A RandomWalkRobot is a robot with the "random walk" movement strategy: it
##        chooses a new direction at random after each time-step.
##        """
##    raise NotImplementedError


# === Problem 6

# For the parameters tested below (cleaning 80% of a 20x20 square room),
# RandomWalkRobots take approximately twice as long to clean the same room as
# StandardRobots do.
def showPlot3():
    """
        Produces a plot comparing the two robot strategies.
        """
    raise NotImplementedError



