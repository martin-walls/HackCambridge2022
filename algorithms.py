import numpy as np

class SearchAlgorithm:
    worldState = 0
    def __init__(self, WSI):
        """ Creates general algorithm class """
        self.worldState = WSI

    def returnNextWorldStateInstance(self):
        return self.worldState

class BasicSearchAlgorithm(SearchAlgorithm):
    state = ""
    def __init__(self):
        " Creates a basic \"snake like\" algorithm "
        self.state = "setup"

    #def returnNextWorldStateInstance(self, )




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


