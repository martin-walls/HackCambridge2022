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


