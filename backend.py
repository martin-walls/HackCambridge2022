class worldStateInstance:
    peopleList = []
    droneList = []

    def __init__(self, listOfPersonObjects, listOfDroneObjects):
        """ Create a new point at the origin """
        self.peopleList = listOfPersonObjects
        self.droneList = listOfDroneObjects


class Drone:
    x = 0
    y = 0
    searchRadius = 0

    def __init__(self):
        """ Creates drone object """
        self.x = 70
        self.y = 90
        self.searchRadius = 50

    def returnCoords(self):
        return (self.x, self.y)

    def getSearchRadius(self):
        return self.searchRadius


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


class SearchAlgorithm:
    worldState = 0
    def __init__(self):
        """ Creates general algorithm class """
        self.worldState = worldStateInstance()





retAttr = worldStateInstance([Person()], [Drone()])


print(retAttr)
def update():
    retAttr.peopleList[0].movePerson(4, 4)
    return retAttr
