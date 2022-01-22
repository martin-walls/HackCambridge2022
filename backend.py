class UpdateAttrs:
    peopleList = []
    droneList = []

    def __init__(self, listOfPersonObjects, listOfDroneObjects):
        """ Create a new point at the origin """
        self.peopleList = listOfPersonObjects
        self.droneList = listOfDroneObjects


class Drone:
    x = 0
    y = 0

    def __init__(self):
        """ Creates drone object """
        self.x = 70
        self.y = 90

    def returnCoords(self):
        return (self.x, self.y)


class Person:
    x = 0
    y = 0

    def __init__(self):
        """ Creates person object """
        self.x = 100
        self.y = 240

    def returnCoords(self):
        return (self.x, self.y)


def update():
    retAttr = UpdateAttrs([Person()], [Drone()])
    return (retAttr.peopleList, retAttr.droneList)


print(update())
