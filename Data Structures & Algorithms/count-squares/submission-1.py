class CountSquares:

    def __init__(self):
        self.freq = {}
        self.points = []
    def add(self, point: List[int]) -> None:
        self.freq[tuple(point)] = self.freq.get(tuple(point), 0) + 1
        self.points.append(point)
    def count(self, point: List[int]) -> int:
        px,py = point 
        count = 0
        for x, y in self.points:
            if abs(x - px) != abs(y - py) or x == px or y == py: 
                continue
            
            if (px,y) in self.freq and (x, py) in self.freq:
                count += self.freq[(px,y)] * self.freq[(x,py)]

        return count