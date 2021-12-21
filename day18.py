# import our helpers
from utils import load, show, day, Map, TRACE
from dataclasses import dataclass

####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__)).splitlines()
xDATA = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""".splitlines()
xDATA = ["[[[[4,3],4],4],[7,[[8,4],9]]]","[1,1]"]
DIGITS = "0123456789"

@dataclass
class ValueInfo:
    depth: int
    value: int
    route: list

def write_to_tree(value, tree, index):
    """recursive method to write to arbitrarily nested index
    represented by a list of indexes"""
    i = index.pop(0)
    if index: # more indices to descend
        write_to_tree(value, tree[i], index)
    else: # reached final tree node
        tree[i] = value

class ExplodeRestart(Exception):
    """Used to restart reduce function"""

def explode(tree, depth=1, history=None, values=None):
    if history is None:
        history = []
    if values is None:
        values = []
    # parse the tree for all depths and values
    for i in 0, 1:
        # descend the lists
        if isinstance(tree[i], list):
            explode(tree[i], depth+1, [*history, i], values)
        # add a value to the shared values list
        # values = [depth, value, [indices from base]]
        else:
            values.append(ValueInfo(depth, tree[i], [*history, i]))
        # end of recursive section

    # if this is the base call check for any explode required
    if depth == 1:
        # search for depth 5 integers
        # we will always find left node first
        for value_index, left in enumerate(values):
            if left.depth == 5:

                # explode left node number to number before this (if any)
                if value_index > 0:
                    before = values[value_index-1]
                    write_to_tree(before.value+left.value, tree, before.route[:])

                # explode right node number to number after this (if any)
                if value_index < len(values)-2:
                    right = values[value_index+1]
                    # this index should always be the second part of the 2-list that needs exploding
                    assert right.depth == 5
                    after = values[value_index+2]
                    write_to_tree(after.value+right.value, tree, after.route[:])

                # swap the exploded 2-list for a 0
                write_to_tree(0, tree, left.route[:-1])

                # and restart the number processing
                raise ExplodeRestart

class SplitRestart(Exception):
    """Used to restart reduce function"""

def split(tree):
    for i in 0, 1:
        if isinstance(tree[i], int):
            val = tree[i]
            if val > 9:
                tree[i]=[val//2, (val+1)//2]
                raise SplitRestart
        else:
            split(tree[i])

# parse the input
def reduce(tree):
    while True:
        try:
            explode(tree)
            split(tree)
        except ExplodeRestart:
            pass # print(f"after explode:  {tree}")
        except SplitRestart:
            pass # print(f"after split:    {tree}")
        else:
            break
    return tree

def magnitude(tree):
    # get left-side magnitude
    if isinstance(tree[0], int):
        left = tree[0]
    else:
        left = magnitude(tree[0])
    # get right-side magnitude
    if isinstance(tree[1], int):
        right = tree[1]
    else:
        right = magnitude(tree[1])
    # return total magnitude
    return 3*left + 2*right

######## Part 1 ##########
def p1(expect=3756):
    tree = eval(DATA[0])
    for i, newtxt in enumerate(DATA[1:]):
        tree = [tree, eval(newtxt)]
        # print(f"after addition: {tree}")
        tree = reduce(tree)
    return magnitude(tree)


######## Part 2 ##########
def p2(expect=4585):
    maximum = 0
    for num1 in DATA:
        for num2 in DATA:
            if num1 is num2:
                continue
            mag = magnitude(reduce([eval(num1), eval(num2)]))
            if mag > maximum:
                maximum = mag
    return maximum

######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
    # from visualizations import viz1
    # viz1(depths)
