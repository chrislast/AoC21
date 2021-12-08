# import our helpers
from utils import load, show, day, TRACE, Map, Path
from collections import Counter
from PIL import Image
from matplotlib import pyplot as plt

####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__))

# parse the input
PARSED = DATA.split(',')

######## Part 1 ##########
def p1(expect=349812, viz=None):
    data = dict(Counter(map(int, PARSED)))
    fuel = 0
    while len(data) > 1:
        imax = max(data)
        imin = min(data)
        if data[imax] > data[imin]:
            n = data.pop(imin)
            data[imin+1] = data.get(imin+1,0) + n
            fuel += n
        else:
            n = data.pop(imax)
            data[imax-1] = data.get(imax-1,0) + n
            fuel += n
    return fuel


######## Part 2 ##########
def fuelcalc(crabs, pos):
    acc = 0
    for cpos, n in crabs.items():
        acc += sum(range(abs(cpos-pos)+1)) * n
    return acc

def p2(expect=99763899, viz=None):
    scatter = []
    ints = list(map(int, PARSED))
    data = dict(Counter(ints))
    imax = max(data)
    imin = min(data)
    iguess = (imax + imin) // 2
    iguess = sorted(ints)[len(ints)//2]
    newval = 999999999999
    while True:
        oldval = newval
        newval = fuelcalc(data, iguess)
        scatter.append((iguess, newval))
        if newval > oldval:
            break
        iguess += 1
    while True:
        oldval = newval
        newval = fuelcalc(data, iguess)
        scatter.append((iguess, newval))
        if newval > oldval:
            break
        iguess -= 1
    if viz:
        viz(scatter)
    return oldval

######### Main ###########
def main():
    show(p1, p2)

def viz2(scatter):
    fig, ax = plt.subplots()
    xdata = [_[0] for _ in scatter]
    ydata = [_[1] for _ in scatter]
    ax.plot(xdata, ydata)
    ax.set_xlabel("crab submarine position")
    ax.set_ylabel("fuel used")
    fig.set_tight_layout(True)
    full = Path(__file__).parent / 'output' / 'day7b.png'
    fig.savefig(full)
    img = Image.open(full)
    img.resize((100,100)).save(Path(__file__).parent / 'output' / 'day7bthumb.png')

if __name__ == "__main__":
    main()
    #p1(viz=viz1)
    p2(viz=viz2)
