# import our helpers
from utils import load, show, day, Map, TRACE
from pathlib import Path
import numpy
####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__)).splitlines()

# parse the input

######## Part 1 ##########
def p1(expect=389):
    m = Map(DATA)
    w, h = m.img.size
    done = False
    count = 0
    while not done:
        data = numpy.array(m.img.getdata()).reshape(h,w)
        count += 1
        done = True
        for y in range(h):
            for x in range(w):
                if data[y,x] == ord(">") and data[y, (x+1)%w] == ord('.'):
                    m.set((x, y), '.')
                    m.set(((x+1)%w, y), ">")
                    done = False
        data = numpy.array(m.img.getdata()).reshape(h,w)
        for y in range(h):
            for x in range(w):
                if data[y,x] == ord("v") and data[(y+1)%h, x] == ord('.'):
                    m.set((x, y), '.')
                    m.set((x, (y+1)%h), "v")
                    done = False
        m.addtogif()
    m.savegif(Path("output/day25.gif"))
    return count


######## Part 2 ##########
def p2(expect=1683):
    pass

######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()

