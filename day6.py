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

def viz1(lanternfish):
    """stacked bar graph"""
    data = Counter(lanternfish)
    fig, ax = plt.subplots()
    xlabels = []
    fish = []
    for days in range(9):
        xlabels.append(days)
        fish.append(data.get(days, 0))
    ax.bar(xlabels, fish, label="day 80 population")
    ax.grid(visible=True, axis="y")
    ax.set_xlabel("days to next birth")
    ax.set_xticks(range(9))
    ax.legend()
    full = Path(__file__).parent / 'output' / 'day6a.png'
    thumb = full.parent / 'day6athumb.png'
    fig.set_tight_layout(True)
    fig.savefig(full)
    img = Image.open(full)
    img.resize((100,100)).save(thumb)

def viz2(population):
    """stacked bar graph"""
    data = population[-1]
    fig, ax = plt.subplots()
    xlabels = []
    fish = []
    for days in range(9):
        xlabels.append(days)
        fish.append(data.get(days, 0))
    ax.bar(xlabels, fish, label="day 256 population")
    ax.grid(visible=True, axis="y")
    ax.set_xlabel("days to next birth")
    ax.set_xticks(range(9))
    ax.legend()
    full = Path(__file__).parent / 'output' / 'day6b.png'
    thumb = full.parent / 'day6bthumb.png'
    fig.set_tight_layout(True)
    fig.savefig(full)
    img = Image.open(full)
    img.resize((100,100)).save(thumb)


if __name__ == "__main__":
    main()
    p1(viz=viz1)
    p2(viz=viz2)
