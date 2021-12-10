# import our helpers
from utils import load, show, day, TRACE, Map
from collections import Counter

####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__)).splitlines()

# parse the input
BITS = len(DATA[0])

######## Part 1 ##########
def p1(expect=3633500, viz=None):
    gamma = ''
    epsilon = ''
    counters = [] # save for viz
    for idx in range(BITS):
        counter = Counter([txt[idx] for txt in DATA])
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
        valid = set(range(len(DATA)))
        bit = 0
        while len(valid) > 1:
            counter = Counter([DATA[i][bit] for i in valid])
            if viz:
                counters.append(counter)
            # find most common
            if counter['0'] == counter['1']:
                match = defaultval
            else:
                match = counter.most_common()[diagidx][0]
            # filter valid list
            for idx in valid.copy():
                if DATA[idx][bit] != match:
                    valid.remove(idx)
            bit += 1
        if viz:
            while len(counters) % 12:
                counters.append(Counter())
        return DATA[valid.pop()]

    oxygen = get_diagnostic('1', 0)
    co2 = get_diagnostic('0', 1)

    if viz:
        viz(counters)

    return int(oxygen,2) * int(co2,2)

##### visualization #######

######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
    from visualizations import viz3a, viz3b
    p1(viz=viz3a)
    p2(viz=viz3b)
