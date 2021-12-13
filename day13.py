# import our helpers
from utils import load, show, day, TRACE, Map, decode4x6font

####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__)).splitlines()
# Parse input
FOLDS = [_ for _ in DATA if "f" in _] # fold along x=655
DOTS = {tuple(map(int,_.split(','))) for _ in DATA if ',' in _} # 1277,347

######## Part 1 ##########
def fold(axis, fold_at, points):
    folded = set()
    for point in points:
        x, y = point
        if axis == "x" and x>fold_at:
            x = fold_at-(x-fold_at)
        if axis == "y" and y>fold_at:
            y = fold_at-(y-fold_at)
        folded.add((x,y))
    return folded

def p1(expect=720, viz=None):
    axis = FOLDS[0][11]
    val = int(FOLDS[0][13:])
    return len(fold(axis,val,DOTS))

######## Part 2 ##########
def p2(expect="AHPRPAUZ", viz=None):
    dots = DOTS
    for instruction in FOLDS:
        axis = instruction[11]
        val = int(instruction[13:])
        dots = fold(axis,val,dots)
    if viz:
        viz(dots)
    return decode4x6font(dots)


######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
    from visualizations import viz13b
    p2(viz=viz13b)
