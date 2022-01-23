import numpy as np


class SearchAlgorithm:
    worldState = 0

    def __init__(self, WSI):
        """ Creates general algorithm class """
        self.worldState = WSI

    def nextWorldStateInstance(self):
        self.returnNextWorldStateInstance()
        if self.isAPersonFound():
            self.personFoundLine()
        return self.worldState

    def returnNextWorldStateInstance(self):
        return self.worldState

    def movePeople(self):
        for person in self.worldState.peopleList:
            person.moveRandomly()

    def isAPersonFound(self):
        if len(self.worldState.peopleList) > 1:
            return False
        for person in self.worldState.peopleList:
            if person.followed:
                return True
        return False

    def personFoundLine(self):
        person_loc = ()
        for person in self.worldState.peopleList:
            if person.followed:
                person_loc = person.returnCoords()
        drones_not_following = []
        for i in range(self.worldState.numDrones):
            drone = self.worldState.droneList[i]
            if drone.following:
                continue
            drones_not_following.append(i)
        dx = person_loc[0] / (i+1)
        dy = person_loc[1] / (i+1)
        for i in range(len(drones_not_following)):
            drone = self.worldState.droneList[drones_not_following[i]]
            drone.moveTowardsLocation(dx * (i+1), dy * (i+1))





class BasicSearchAlgorithm(SearchAlgorithm):
    dfaState = ""
    leftToRight = True
    descending = False
    y_level = 0
    startingWidthLocations = []

    def __init__(self, WSI):
        self.worldState = WSI
        self.dfaState = "setup"
        self.leftToRight = True
        self.descending = False
        self.y_level = 0
        for i in range(len(WSI.droneList)):
            self.startingWidthLocations.append(int((WSI.width / len(WSI.droneList)) * i))

    def returnNextWorldStateInstance(self):
        if (self.dfaState == "setup"):
            # establish starting locations for the drones and move them there
            moveSpeed = self.worldState.droneList[0].moveSpeed
            correctLocation = True
            for i in range(len(self.worldState.droneList)):
                x_loc = self.worldState.droneList[i].x
                if (x_loc != self.startingWidthLocations[i]):
                    correctLocation = False
                    # do movemenet of drones towards starting location
                    self.worldState.droneList[i].addToX(min(self.startingWidthLocations[i] - x_loc, moveSpeed))
            if (correctLocation):
                self.dfaState = "scan"
        elif (self.dfaState == "scan"):
            moveSpeed = self.worldState.droneList[0].moveSpeed
            widthDistance = self.startingWidthLocations[1]
            listOfDrones = self.worldState.droneList

            # check if you can spot the person
            #for i in range(len(listOfDrones)):
            #    drone = listOfDrones[i]
            #    drone.detectPerson(self.worldState.peopleList)
            # check if going right, down, left
            if (self.descending):
                for i in range(len(listOfDrones)):
                    drone = listOfDrones[i]
                    if drone.following == None:
                        drone.moveTowardsLocation(drone.x, self.y_level)
                    else:
                        drone.moveTowardsLocation(drone.following.x, drone.following.y)
                    if (drone.y == self.y_level):
                        self.descending = False
            elif (self.leftToRight):
                for i in range(len(listOfDrones)):
                    drone = listOfDrones[i]
                    if drone.following == None:
                        drone.moveTowardsLocation(self.startingWidthLocations[i] + widthDistance, drone.y)
                    else:
                        drone.moveTowardsLocation(drone.following.x, drone.following.y)
                if (listOfDrones[0].x == self.startingWidthLocations[0] + widthDistance):
                        self.leftToRight = False
                        self.descending = True
                        self.y_level += (drone.searchRadius*2)
            else:
                for i in range(len(listOfDrones)):
                    drone = listOfDrones[i]
                    if drone.following == None:
                        drone.moveTowardsLocation(self.startingWidthLocations[i], drone.y)
                    else:
                        drone.moveTowardsLocation(drone.following.x, drone.following.y)
                if (listOfDrones[0].x == self.startingWidthLocations[0]):
                        self.leftToRight = True
                        self.descending = True
                        self.y_level += (drone.searchRadius*2)


        self.movePeople()
        return self.worldState


class ZShapeAlgorithm(SearchAlgorithm):
    def __init__(self, WSI):
        self.worldState = WSI
        self.dfaState = "setup"

        self.dx = self.worldState.width / self.worldState.numDrones
        self.dy = WSI.droneList[0].searchRadius

        self.moveToRight = 1

        # for i in range(self.worldState.numDrones):
        #     self.worldState.droneList[i].setCoords(self.dx * (i + 0.5), 0)

    def returnNextWorldStateInstance(self):
        if self.dfaState == "setup":
            allFinished = True
            for i in range(self.worldState.numDrones):
                drone = self.worldState.droneList[i]
                drone.moveTowardsLocation(self.dx * (i + 0.5), 0)
                if drone.returnCoords() != (int(self.dx * (i + 0.5)), 0):
                    allFinished = False
            if allFinished:
                self.dfaState = "scan"
        else:
            toTurn = False
            for i in range(self.worldState.numDrones):
                drone = self.worldState.droneList[i]
                if drone.following == None:
                    drone.move_absolute(self.dx * self.moveToRight, self.dy)
                    if drone.x >= self.dx * (i + 1) or drone.x <= self.dx * i:
                        toTurn = True
                else:
                    drone.moveTowardsLocation(drone.following.x, drone.following.y)

            if toTurn:
                self.moveToRight *= -1

        self.movePeople()
        return self.worldState


class SpiralSearchAlgorithm(SearchAlgorithm):
    _drone_dirs = []
    _angle_change = 15
    _speed = 3
    _move_forward_counter = 1
    _move_forward_max = 1
    _drift = (1, 1.5)

    def __init__(self, WSI):
        super().__init__(WSI)
        self._drone_dirs = np.linspace(0, 360, self.worldState.numDrones, endpoint=False)

        for drone in self.worldState.droneList:
            # drone.x = self.worldState.width / 2
            # drone.y = self.worldState.height / 2
            drone.x = 100
            drone.y = 100

        _drift = (self.worldState.width / 1000, self.worldState.height / 1000)

    def returnNextWorldStateInstance(self):
        for i in range(self.worldState.numDrones):
            drone = self.worldState.droneList[i]
            angle = self._drone_dirs[i]
            if drone.following == None:
                drone.move_by_angle(angle, self._speed)
                drone.move_absolute(*self._drift)
            else:
                drone.moveTowardsLocation(drone.following.x, drone.following.y)
        self._next_state()
        self.movePeople()
        return self.worldState

    def _next_state(self):
        if (self._move_forward_counter > 0):
            self._move_forward_counter -= 1
        else:
            self._move_forward_max += 1
            self._move_forward_counter = self._move_forward_max

            for i in range(self.worldState.numDrones):
                self._drone_dirs[i] += self._angle_change
