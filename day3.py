# import our helpers
from utils import load, show, day, TRACE, Map, Path
from collections import Counter

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

    def get_diagnostic(defaultval, diagidx):
        valid = set(range(len(PARSED)))
        bit = 0
        while len(valid) > 1:
            counter = Counter([PARSED[i][bit] for i in valid])
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
        return PARSED[valid.pop()]

    oxygen = get_diagnostic('1', 0)
    co2 = get_diagnostic('0', 1)
    return int(oxygen,2) * int(co2,2)

def viz1(counters):
    from PIL import Image
    from matplotlib import pyplot as plt
    fig, ax = plt.subplots()
    xlabels = range(len(counters))
    ones = [_['1'] for _ in counters]
    noughts = [_['0'] for _ in counters]
    ax.bar(xlabels, noughts, label="0")
    ax.bar(xlabels, ones, label="1", bottom=noughts)
    ax.legend()
    full = Path(__file__).parent / 'output' / 'day3a.png'
    thumb = full.parent / 'day3athumb.png'
    fig.savefig(full)
    img = Image.open(full)
    img.resize((100,100)).save(thumb)

######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
    p1(viz=viz1)
