import algorithms
import math
import random

WIDTH = 1000
HEIGHT = 700

class WorldStateInstance:
    peopleList = []
    droneList = []
    numDrones = 0
    width = 0
    height = 0

    def __init__(self, droneNum, peopleNum):
        """ Create a new point at the origin """
        self.droneList = []
        for i in range(droneNum):
            self.droneList.append(Drone())

        self.peopleList = []
        for i in range(peopleNum):
            self.peopleList.append(Person())

        self.numDrones = droneNum
        self.width = WIDTH
        self.height = HEIGHT


class Drone:
    x = 0
    y = 0
    searchRadius = 0
    moveSpeed = 0

    def __init__(self, x=70, y=90):
        """ Creates drone object """
        self.x = x
        self.y = y
        self.searchRadius = 200
        self.moveSpeed = 10

    def setCoords(self, x, y):
        self.x = x
        self.y = y

    def returnCoords(self):
        return (self.x, self.y)

    def getSearchRadius(self):
        return self.searchRadius

    def detectPerson(self, peopleList):
        found_people_list = []
        for person in peopleList:
            # can use object detection algorithm in the future to determine whether a person has been detected
            distance = math.sqrt((self.x - person.x) ** 2 + (self.y - person.y) ** 2)
            if distance <= self.searchRadius:
                print("Find a person")
                found_people_list.append(person)
        return found_people_list

    def move_by_angle(self, angle, speed):
        """ angle measured clockwise from north, in degrees """
        if speed > self.moveSpeed:
            speed = self.moveSpeed

        radians = math.radians(angle)
        delta_x = speed * math.sin(radians)
        delta_y = speed * math.cos(radians)
        self.x += int(delta_x)
        self.y += int(delta_y)

    def move_absolute(self, dx, dy):
        dist = math.sqrt(dx**2 + dy**2)
        if dist > self.moveSpeed:
            dx = int(dx / dist * self.moveSpeed)
            dy = int(dy / dist * self.moveSpeed)

        self.x += dx
        self.y += dy

    def moveInDirection(self, dx, dy):
        actual_dis = math.sqrt(dx ** 2 + dy ** 2)
        dx = int(dx / actual_dis * self.moveSpeed)
        dy = int(dy / actual_dis * self.moveSpeed)

        self.x += dx
        self.y += dy

        # print(self.x, " ", self.y)

    def moveTowardsLocation(self, x_toLocation, y_toLocation):
        x_proposedMove = x_toLocation - self.x
        y_proposedMove = y_toLocation - self.y
        proposedDistance = math.sqrt((x_proposedMove)**2 + (y_proposedMove)**2)
        if (proposedDistance <= self.moveSpeed):
            self.x += x_proposedMove
            self.y += y_proposedMove
        else:
            self.x += int(x_proposedMove * self.moveSpeed / proposedDistance)
            self.y += int(y_proposedMove * self.moveSpeed / proposedDistance)



class Person:
    x = 0
    y = 0

    def __init__(self):
        """ Creates person object """
        self.x = 100
        self.y = 240

    def returnCoords(self):
        return (self.x, self.y)

    def movePerson(self, x_change, y_change):
        self.x = self.x + x_change
        self.y = self.y + y_change

    def moveRandomly(self):
        dx = random.randint(-1, 2)
        dy = random.randint(-1, 2)
        self.movePerson(dx, dy)





retAttr = WorldStateInstance(3, 1)
# sa = algorithms.SearchAlgorithm(retAttr)
sa = algorithms.BasicSearchAlgorithm(retAttr)


# print(retAttr)
def update():
    retAttr = sa.returnNextWorldStateInstance()
    retAttr.peopleList[0].moveRandomly()
    return retAttr
