import algorithms
import math
import random

WIDTH = 1000
HEIGHT = 700

class WorldStateInstance:
    peopleList = []
    numPeople = 0
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
        self.numPeople = peopleNum
        self.width = WIDTH
        self.height = HEIGHT

        print(self.droneList)


class Drone:
    x = 0
    y = 0
    searchRadius = 0
    moveSpeed = 0

    def __init__(self, x=70, y=90):
        """ Creates drone object """
        self.x = x
        self.y = y
        self.searchRadius = 100
        self.moveSpeed = int(self.searchRadius / 10)
        self.location_history = []

    def setCoords(self, x, y):
        self.x = x
        self.y = y
        self.add_current_coords_to_history()

    def addToX(self, dx):
        self.x += dx
        self.add_current_coords_to_history()

    def addToY(self, dy):
        self.y += dy
        self.add_current_coords_to_history()

    def returnCoords(self):
        return (int(self.x), int(self.y))

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
        self.x += delta_x
        self.y += delta_y
        self.add_current_coords_to_history()

    def move_absolute(self, dx, dy):
        dist = math.sqrt(dx**2 + dy**2)
        if dist > self.moveSpeed:
            dx = dx / dist * self.moveSpeed
            dy = dy / dist * self.moveSpeed

        self.x += dx
        self.y += dy
        self.add_current_coords_to_history()


    def moveTowardsLocation(self, x_toLocation, y_toLocation):
        x_proposedMove = x_toLocation - self.x
        y_proposedMove = y_toLocation - self.y
        proposedDistance = math.sqrt(x_proposedMove ** 2 + y_proposedMove ** 2)
        if proposedDistance <= self.moveSpeed:
            self.x += x_proposedMove
            self.y += y_proposedMove
        else:
            self.x += x_proposedMove * self.moveSpeed / proposedDistance
            self.y += y_proposedMove * self.moveSpeed / proposedDistance
        self.add_current_coords_to_history()

    def add_current_coords_to_history(self):
        self.location_history.append((int(self.x), int(self.y)))

    def get_location_history(self):
        return self.location_history



class Person:
    x = 0
    y = 0

    def __init__(self):
        """ Creates person object """
        self.x = 100
        self.y = 240

    def returnCoords(self):
        return (int(self.x), int(self.y))

    def movePerson(self, x_change, y_change):
        self.x = self.x + x_change
        self.y = self.y + y_change

    def moveRandomly(self):
        dx = random.randint(-1, 2)
        dy = random.randint(-1, 2)
        self.movePerson(dx, dy)




class Backend:
    def __init__(self, alg_to_use="basic", num_drones=3, num_people=1):
        """ create a backend instance with the given config """
        self.world_state = WorldStateInstance(num_drones, num_people)
        if alg_to_use == "basic":
            self.search_alg = algorithms.BasicSearchAlgorithm(self.world_state)
        elif alg_to_use == "zshape":
            self.search_alg = algorithms.ZShapeAlgorithm(self.world_state)
        elif alg_to_use == "spiral":
            self.search_alg = algorithms.SpiralSearchAlgorithm(self.world_state)
        else:
            print("Invalid algorithm option: {}. Using basic algorithm instead.".format(alg_to_use))
            self.search_alg = algorithms.BasicSearchAlgorithm(self.world_state)


    def update(self):
        self.world_state = self.search_alg.returnNextWorldStateInstance()
        # move people
        # for person in self.world_state.peopleList:
        #     person.moveRandomly()
        return self.world_state

