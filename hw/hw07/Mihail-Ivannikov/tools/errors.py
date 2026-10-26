class LessThenZeroError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data

class TriangleSidesError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data

