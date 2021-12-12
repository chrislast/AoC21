# import our helpers
from utils import load, show, day, TRACE

####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__)).splitlines()

######## Part 1 ##########
def pathfinder(node, connections, route=[], visited=set(), small_cave_visited_twice_already=True):
    route.append(node) # tracked for interest only - not required for problem

    if node == "end":
        return 1 # we found a valid path

    if node in visited and small_cave_visited_twice_already:
        return 0 # we failed to find a valid path

    # Otherwise, form a new network search list and update visited list
    search = connections.copy()
    if node == "start":
        search = [_ for _ in search if "start" not in _]
    elif node > "ZZ": # small cave test
        if node in visited: # this will be our one repeated small cave
            small_cave_visited_twice_already = True
        visited.add(node) # remember we were here
        if small_cave_visited_twice_already:
            # we can start removing routes back to small caves
            search = [_ for _ in search if node not in _]

    # recursively add the number of valid solutions with this base
    retval = 0
    for cave in [_.replace("-","").replace(node,"") for _ in connections if node in _]:
        retval += pathfinder(cave, search, route.copy(), visited.copy(), small_cave_visited_twice_already)
    return retval

def p1(expect=5157, viz=None):
    return pathfinder("start", DATA.copy())

######## Part 2 ##########
def p2(expect=144309, viz=None):
    return pathfinder("start", DATA.copy(), small_cave_visited_twice_already=False)

######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
