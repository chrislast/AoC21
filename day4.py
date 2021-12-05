# import our helpers
from utils import load, show, day, TRACE, Map, Path

####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__))

# parse the input
PARSED = DATA.splitlines()
NUMBERS = list(map(int,PARSED[0].split(",")))
CARDS = [PARSED[n:n+5] for n in range(2, len(PARSED), 6)]
MAP = Map([list(map(int,' '.join(x).split())) for x in CARDS], output_size=(100,100))
MAP.setcolour(255,(0,0,0))

######## Part 1 ##########
def p1(expect=6592, viz=None):
    data = list(MAP.img.getdata())

    for num in NUMBERS:
        # remove each number from all cards
        for idx, val in enumerate(data):
            if val == num:
                data[idx] = 255

        if viz:
            MAP.img.putdata(data)
            MAP.addtogif()

        for cidx in range(len(data)//25):
            card = data[cidx*25:cidx*25+25]
            for idx in range(5):
                if (sum(card[idx*5:idx*5+5]) == 255*5 or # test rows
                    sum(card[idx::5]) == 255*5): # test columns
                    return sum([_ for _ in card if _ != 255])*num


######## Part 2 ##########
def p2(expect=31755, viz=None):
    data = list(MAP.img.getdata())
    unwon=set(range(len(data)//25))

    for num in NUMBERS:
        # remove each number from all cards
        for idx, val in enumerate(data):
            if val == num:
                data[idx] = 255

        if viz:
            MAP.img.putdata(data)
            MAP.addtogif()

        for cidx in unwon.copy():
            card = data[cidx*25:cidx*25+25]
            for idx in range(5):
                if (sum(card[idx*5:idx*5+5]) == 255*5 or # test rows
                    sum(card[idx::5]) == 255*5): # test columns
                    if len(unwon) < 2:
                        return sum([_ for _ in card if _ != 255])*num
                    else:
                        unwon.remove(cidx)
                        break

######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
    p1(viz=True)
    MAP.savegif(Path(__file__).parent / 'output' / 'day4a.gif')
    p2(viz=True)
    MAP.savegif(Path(__file__).parent / 'output' / 'day4b.gif')
