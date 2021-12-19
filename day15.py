# import our helpers
from utils import load, show, day, TRACE, Map
from dataclasses import dataclass
from collections import deque
import numpy as np
####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__)).splitlines()

# Parse input
LENY = len(DATA)
LENX = len(DATA[0])
ARR = np.array([[int(c) for c in row] for row in DATA])

@dataclass
class RiskPoint:
    risk: int   # 0-9
    pos: tuple  # (x,y)
    route: list # [ (x,y), (x,y), ... ]

    def __lt__(self, obj):
        return self.risk < obj.risk

######## Part 1 ##########
class DictQueue:
    """Lowest priority first queue implemented as a dictionary of subqueues
    keyed by cumulative priority.  Significantly quicker than sorting a single
    list reqepatedly or even finding where to insert a node in a sorted list"""
    def __init__(self):
        self._queue = {}

    def popleft(self):
        lowest_risk = min(self._queue)
        siblings = self._queue[lowest_risk]
        point = siblings.pop(0)
        if not siblings:
            self._queue.pop(lowest_risk)
        return point

    def append(self, point):
        risk = point.risk
        riskqueue = self._queue.get(risk, [])
        riskqueue.append(point)
        self._queue[risk] = riskqueue

    def __len__(self):
        return len(self._queue)

def find_lowest_risk_path(target, get_risk_fn):
    queue = DictQueue()
    queue.append(RiskPoint(risk=0, pos=(0,0), route=[]))
    visited = set((0,0))
    while len(queue):
        node = queue.popleft() # process least risky node first
        if node.pos == target:
            break # path found
        xnode, ynode = node.pos
        for xoff, yoff in ((-1,0), (0,-1), (1,0), (0,1)): # foreach neighbour
            pos = (xnode+xoff, ynode+yoff)
            if 0<=pos[0]<=target[0] and 0<=pos[1]<=target[1] and pos not in visited:
                # we reached a new location for the first time
                visited.add(pos)
                newnode = RiskPoint(
                    risk=node.risk + get_risk_fn(pos),
                    pos=pos,
                    route=node.route.copy() + [pos])
                queue.append(newnode)
    return node

def p1risk(pos):
    return ARR[pos[1],pos[0]]

def p1(expect=456, viz=None):
    targetnode = find_lowest_risk_path((LENX-1, LENY-1), p1risk)
    if viz:
        viz(targetnode.route)
    return targetnode.risk

######## Part 2 ##########
def p2risk(pos):
    divx, modx = divmod(pos[0], LENX)
    divy, mody = divmod(pos[1], LENY)
    risk = ARR[mody,modx]
    risk += divx + divy
    if risk > 9:
        risk -= 9
    return risk

def p2(expect=2831, viz=None):
    targetnode = find_lowest_risk_path((5*LENX-1, 5*LENY-1), p2risk)
    if viz:
        viz(targetnode.route)
    return targetnode.risk

######### Main ###########
def main():
    show(p1,p2)

if __name__ == "__main__":
    main()
    from visualizations import viz15a, viz15b
    p1(viz=viz15a)
    p2(viz=viz15b)
