from datetime import datetime

class Event:
    def __init__(self, name, start, end):
        assert start < end

        self.name = name
        self.start = start
        self.end = end

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.start, self.end)

    def __repr__(self):
        return self.__str__()

