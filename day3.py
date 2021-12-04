# import our helpers
from utils import load, show, day, TRACE, Map, Path
from collections import Counter
from PIL import Image
from matplotlib import pyplot as plt

####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__))

# parse the input
PARSED = DATA.splitlines()
BITS = len(PARSED[0])

######## Part 1 ##########
def p1(expect=3633500, viz=None):
    gamma = ''
    epsilon = ''
    counters = [] # save for viz
    for idx in range(BITS):
        counter = Counter([txt[idx] for txt in PARSED])
        counters.append(counter)
        gamma += counter.most_common()[0][0]
        epsilon += counter.most_common()[1][0]
    if viz:
        viz(counters)
    return int(gamma,2) * int(epsilon,2)

######## Part 2 ##########
def p2(expect=4550283, viz=None):
# Next, you should verify the life support rating, which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.
    counters=[]
    def get_diagnostic(defaultval, diagidx):
        valid = set(range(len(PARSED)))
        bit = 0
        while len(valid) > 1:
            counter = Counter([PARSED[i][bit] for i in valid])
            if viz:
                counters.append(counter)
            # find most common
            if counter['0'] == counter['1']:
                match = defaultval
            else:
                match = counter.most_common()[diagidx][0]
            # filter valid list
            for idx in valid.copy():
                if PARSED[idx][bit] != match:
                    valid.remove(idx)
            bit += 1
        if viz:
            while len(counters) % 12:
                counters.append(Counter())
        return PARSED[valid.pop()]

    oxygen = get_diagnostic('1', 0)
    co2 = get_diagnostic('0', 1)

    if viz:
        viz(counters)

    return int(oxygen,2) * int(co2,2)

##### visualization #######

def viz1(counters):
    """stacked bar graph"""
    fig, ax = plt.subplots()
    xlabels = range(len(counters))
    ones = [_['1'] for _ in counters]
    noughts = [_['0'] for _ in counters]
    ax.bar(xlabels, noughts, label="0")
    ax.bar(xlabels, ones, label="1", bottom=noughts)
    ax.set(ylim=[450, 550], title="Bit Value Counters")
    ax.grid(visible=True, axis="y")
    ax.set_xlabel("bit position")
    ax.set_xticks(range(0,12))
    ax.set_yticks(range(450,560,10))
    ax.legend()
    full = Path(__file__).parent / 'output' / 'day3a.png'
    thumb = full.parent / 'day3athumb.png'
    fig.set_tight_layout(True)
    fig.savefig(full)
    img = Image.open(full)
    img.resize((100,100)).save(thumb)

def viz2(counters):
    """3d stacked bar graph"""
    # setup the figure and axes
    fig = plt.figure(figsize=(7,6))
    ax = fig.add_subplot(111, projection='3d', title="Valid codes remaining")
    width = 0.75
    depth = 0.5
    x = [0,1,2,3,4,5,6,7,8,9,10,11]*2
    y = [0]*12 + [1]*12
    z = [0]*24
    ones = [c['1'] for c in counters]
    noughts = [c['0'] for c in counters]
    ax.set_xticks(range(0,12))
    ax.set_xlabel("bits checked")
    ax.set_ylabel("oxygen            CO2")
    ax.set_yticks([])
    ax.bar3d(x, y, z, width, depth, noughts, shade=True, label="0")
    ax.bar3d(x, y, noughts, width, depth, ones, shade=True, label="1")
    fig.set_tight_layout(True)
    full = Path(__file__).parent / 'output' / 'day3b.png'
    thumb = full.parent / 'day3bthumb.png'
    fig.savefig(full)
    img = Image.open(full)
    img.resize((100,100)).save(thumb)

######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
    p1(viz=viz1)
    p2(viz=viz2)
