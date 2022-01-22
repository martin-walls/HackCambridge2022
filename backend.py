
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
        self.x = 0
        self.y = 0

    def returnCoords(self):
        return (self.x, self.y)

class Person:
    x = 0
    y = 0
    def __init__(self):
        """ Creates person object """
        self.x = 0
        self.y = 0

    def returnCoords(self):
        return (self.x, self.y)

    def movePerson(self, x_change, y_change):
        self.x = self.x + x_change
        self.y = self.y + y_change





retAttr = UpdateAttrs([Person()], [Drone()])
def update():
    retAttr.listOfDroneObjects[0].movePerson(4, 4))
    return retAttr
