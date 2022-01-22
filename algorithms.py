import numpy as np

class SearchAlgorithm:
    worldState = 0
    def __init__(self, WSI):
        """ Creates general algorithm class """
        self.worldState = WSI

    def returnNextWorldStateInstance(self):
        return self.worldState

# class BasicSearchAlgorithm(SearchAlgorithm):
#     dfaState = ""
#     startingWidthLocations = []
#     def __init__(self, WSI):
#         " Creates a basic \"snake like\" algorithm "
#         self.worldState = WSI
#         self.dfaState = "setup"
#         for i in range(len(WSI.listOfDroneObjects)):
#             self.startingWidthLocations.append((WSI.width/len(WSI.listOfDroneObjects))*i)
#
#
#     def returnNextWorldStateInstance(self):
#         if (dfaState == "setup"):
#             # establish starting locations for the drones and move them there
#             movespeed = listOfDroneObjects[0].moveSpeed
#             for i in range(len(worldState.listOfDroneObjects)):
#                 x_loc = listOfDroneObjects[i].x
#                 if (x_loc != startingWidthLocations[i]):
#                     # do movemenet of drones towards starting location
#                     WSI.listOfDroneObjects[i].x += min(startingWidthLocations - x_loc, moveSpeed)
#
#         return worldState


class ZShapeAlgorithm(SearchAlgorithm):
    def __init__(self, WSI):
        self.worldState = WSI

        self.dx = self.worldState.width / self.worldState.numDrones
        self.dy = WSI.droneList[0].searchRadius

        self.moveToRight = 1

        self.worldState.numDrones = 1
        for i in range(self.worldState.numDrones):
            self.worldState.droneList[i].setCoords(int(self.dx * (i + 0.5)), 0)

    def returnNextWorldStateInstance(self):
        for drone in self.worldState.droneList:
            drone.moveInDirection(self.dx * self.moveToRight, self.dy)

        if self.worldState.droneList[0].x >= self.dx or self.worldState.droneList[0].x <= 0:
            self.moveToRight *= -1

        return self.worldState


class SpiralSearchAlgorithm(SearchAlgorithm):
    _drone_dirs = []
    _angle_change = 10
    _speed = 1
    _move_forward_counter = 1
    _move_forward_max = 1

    def __init__(self, WSI):
        super().__init__(WSI)
        self._drone_dirs = np.linspace(0, 360, self.worldState.numDrones, endpoint=False)

        for drone in self.worldState.droneList:
            drone.x = self.worldState.width / 2
            drone.y = self.worldState.height / 2

        print(self._drone_dirs)

    def returnNextWorldStateInstance(self):
        for i in range(len(self.worldState.droneList)):
            drone = self.worldState.droneList[i]
            angle = self._drone_dirs[i]
            drone.move_by_angle(angle, self._speed)
        self._next_state()
        return self.worldState

    def _next_state(self):
        if (self._move_forward_counter > 0):
            self._move_forward_counter -= 1
        else:
            self._move_forward_max += 1
            self._move_forward_counter = self._move_forward_max

            for i in range(self.worldState.numDrones):
                self._drone_dirs[i] += self._angle_change
