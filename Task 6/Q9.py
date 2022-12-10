from collections import defaultdict
from typing import List

# The code is not mine
# I tried very hard but could not solve it
# I find copying code to be a heavy burden on me

class DetectSquares:
    def __init__(self):
        self.ptsC = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]):
        self.ptsC[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]):
        res = 0
        px, py = point
        for x, y in self.pts:
            if(abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.ptsC[(x, py)] * self.ptsC[(y, px)]
        return res