import algorithms
import math
import random

WIDTH = 500
HEIGHT = 700

class WorldStateInstance:
    peopleList = []
    droneList = []
    numDrones = 0
    width = 0
    height = 0

    def __init__(self, listOfPersonObjects, listOfDroneObjects):
        """ Create a new point at the origin """
        self.peopleList = listOfPersonObjects
        self.droneList = listOfDroneObjects
        self.numDrones = len(listOfDroneObjects)
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

    def moveInDirection(self, dx, dy):
        actual_dis = math.sqrt(dx ** 2 + dy ** 2)
        dx = dx / actual_dis * self.moveSpeed
        dy = dy / actual_dis * self.moveSpeed

        self.x += dx
        self.y += dy




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





retAttr = WorldStateInstance([Person()], [Drone()])
# sa = algorithms.SearchAlgorithm(retAttr)
sa = algorithms.ZShapeAlgorithm(retAttr)


# print(retAttr)
def update():
    retAttr = sa.returnNextWorldStateInstance()
    retAttr.peopleList[0].moveRandomly()
    return retAttr
