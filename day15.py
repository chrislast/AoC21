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
def find_lowest_risk_path(target, get_risk_fn):
    queue = []
    visited = set((0,0))
    queue.append(RiskPoint(risk=0, pos=(0,0), route=[]))
    while queue:
        node = queue.pop(0) # process least risky queue node
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
                # insert the new node into the queue before any riskier nodes
                inserted = False
                for idx, qnode in enumerate(queue):
                    if qnode.risk > newnode.risk:
                        queue.insert(idx, newnode)
                        inserted = True
                        break
                if not inserted:
                    queue.append(newnode)
        # queue = sorted(queue) saved 50% of total execution time by replacing with insertion method above
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
