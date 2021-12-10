# import our helpers
from utils import load, show, day, TRACE, Map
from collections import Counter

####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__))

# parse the input
PARSED = DATA.split(',')

######## Part 1 ##########
def p1(expect=360268, viz=None):
    lanternfish = [int(_) for _ in PARSED]
    for i in range(80):
        babies = [8 for f in lanternfish if f == 0]
        for fish, val in enumerate(lanternfish):
            if val == 0:
                lanternfish[fish] = 6
            else:
                lanternfish[fish] -= 1
        lanternfish += babies
    if viz:
        viz(lanternfish)
    return len(lanternfish)

######## Part 2 ##########
def p2(expect=1632146183902, viz=None):
    lanternfish = dict(Counter([int(_) for _ in PARSED]))
    population = [lanternfish.copy()]
    for i in range(256):
        lanternfish = {k-1:v for k,v in lanternfish.items() if k>=0}
        newfish = lanternfish.get(-1, 0)
        if newfish:
            lanternfish.pop(-1)
        lanternfish[8] = newfish
        lanternfish[6] = newfish + lanternfish.get(6, 0)
        population.append(lanternfish.copy())
    if viz:
        viz(population)
    return sum(population[-1].values())

# This would have been even neater if I'd thought of it although no quicker
# rotating and cleaning the array using list.pop(index) is one to remember

#     school = [0] * 9
#     for i in PARSED:
#         school[int(i)] += 1
#     for i in range(256):
#         new_fish = school.pop(0)
#         school.append(new_fish)
#         school[6] += new_fish
#     print(sum(school))

######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
    from visualizations import viz6a, viz6b
    p1(viz=viz6a)
    p2(viz=viz6b)
