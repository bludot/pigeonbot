import random


class Pigeon:
    def __init__(self, type: str, points: int, success: int):
        self._type = type
        self._points = points
        self._success = success

    def type(self):
        return self._type
    
    def points(self):
        return self._points
    
    def success(self):
        return self._success
    

pigeons = [
    Pigeon("cartel member", 10, 85),
    Pigeon("boss", 100, 25),
    Pigeon("white", 50, 50),
]
 
