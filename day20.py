# import our helpers
from utils import load, show, day, Map, TRACE
import numpy as np

####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__)).splitlines()

# parse the input
ALGO = DATA[0]
IMG = DATA[2:]
BLACK = 0
WHITE = 1
CONVERT = {".": BLACK, "#": WHITE}

def create_image_with_border(border_width):
    height = len(IMG)+border_width*2
    width = len(IMG[0])+border_width*2
    padded = ['.'*width]*border_width                                   # top border
    padded += [f"{'.'*border_width}{_}{'.'*border_width}" for _ in IMG] # side borders
    padded += ['.'*width]*border_width                                  # bottom border
    # convert to numpy array
    return np.array([[CONVERT[c] for c in row] for row in padded], dtype=int)

def enhance_image(arr):
    width, height = arr.shape
    new_arr = arr.copy()
    for x in range(width):
        for y in range(height):
            acc = 0
            for dy in range(-1,2):
                for dx in range(-1,2):
                    acc <<= 1
                    try:
                        if arr[y+dy,x+dx] == WHITE:
                            acc += 1
                    except:
                        pass
            new_arr[y,x] = CONVERT[ALGO[acc]]
    return new_arr

def zoom(repetitions, viz):
    maps = []
    arr = create_image_with_border(border_width=repetitions+1)
    if viz:
        maps.append(Map(arr))
    for _ in range(repetitions):
        arr = enhance_image(arr)
        if viz:
            maps.append(Map(arr))
    if viz:
        viz(maps)
    return arr

######## Part 1 ##########
def p1(expect=5432, viz=None):
    return sum(sum(zoom(2, viz)))

######## Part 2 ##########
def p2(expect=16016, viz=None):
    return sum(sum(zoom(50, viz)))

######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
    from visualizations import viz20a, viz20b
    p1(viz=viz20a)
    p2(viz=viz20b)
