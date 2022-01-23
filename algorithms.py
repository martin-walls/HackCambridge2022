import numpy as np


class SearchAlgorithm:
    worldState = 0

    def __init__(self, WSI):
        """ Creates general algorithm class """
        self.worldState = WSI

    def returnNextWorldStateInstance(self):
        return self.worldState

    def movePeople(self):
        for person in self.worldState.peopleList:
            person.moveRandomly()


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

            # check if going right, down, left
            listOfDrones = self.worldState.droneList
            if (self.descending):
                for i in range(len(listOfDrones)):
                    drone = listOfDrones[i]
                    drone.moveTowardsLocation(drone.x, self.y_level)
                    if (drone.y == self.y_level):
                        self.descending = False
            elif (self.leftToRight):
                for i in range(len(listOfDrones)):
                    drone = listOfDrones[i]
                    drone.moveTowardsLocation(self.startingWidthLocations[i] + widthDistance, drone.y)
                    if (drone.x == self.startingWidthLocations[i] + widthDistance):
                        self.leftToRight = False
                        self.descending = True
                        self.y_level += (drone.searchRadius)
            else:
                for i in range(len(listOfDrones)):
                    drone = listOfDrones[i]
                    drone.moveTowardsLocation(self.startingWidthLocations[i], drone.y)
                    if (drone.x == self.startingWidthLocations[i]):
                        self.leftToRight = True
                        self.descending = True
                        self.y_level += (drone.searchRadius)

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
            for drone in self.worldState.droneList:
                drone.move_absolute(self.dx * self.moveToRight, self.dy)

            if self.worldState.droneList[0].x >= self.dx or self.worldState.droneList[0].x <= 0:
                self.moveToRight *= -1

        # self.movePeople()
        return self.worldState


class SpiralSearchAlgorithm(SearchAlgorithm):
    _drone_dirs = []
    _angle_change = 15
    _speed = 2
    _move_forward_counter = 1
    _move_forward_max = 1
    _drift = (0.5, 0.5)

    def __init__(self, WSI):
        super().__init__(WSI)
        self._drone_dirs = np.linspace(0, 360, self.worldState.numDrones, endpoint=False)

        for drone in self.worldState.droneList:
            # drone.x = self.worldState.width / 2
            # drone.y = self.worldState.height / 2
            drone.x = 100
            drone.y = 100

    def returnNextWorldStateInstance(self):
        for i in range(self.worldState.numDrones):
            drone = self.worldState.droneList[i]
            angle = self._drone_dirs[i]
            drone.move_by_angle(angle, self._speed)
            drone.move_absolute(*self._drift)
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
