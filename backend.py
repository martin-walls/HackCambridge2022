import algorithms
import math

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

    def __init__(self):
        """ Creates drone object """
        self.x = 70
        self.y = 90
        self.searchRadius = 200
        self.moveSpeed = self.searchRadius

    def returnCoords(self):
        return (self.x, self.y)

    def getSearchRadius(self):
        return self.searchRadius

    def detectPerson(self, peopleList):
        found_people_list = []
        for person in peopleList:
            distance = math.sqrt((self.x - person.x) ** 2 + (self.y - person.y) ** 2)
            if distance <= self.searchRadius:
                print("Find a person")
                found_people_list.append(person)
        return found_people_list




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




retAttr = WorldStateInstance([Person()], [Drone()])
sa = algorithms.SearchAlgorithm(retAttr)

print(retAttr)
def update():
    retAttr = sa.returnNextWorldStateInstance()
    #retAttr.peopleList[0].movePerson(1, 1)
    return retAttr
