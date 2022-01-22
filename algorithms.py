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
