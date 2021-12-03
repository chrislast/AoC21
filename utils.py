from pathlib import Path
import pdb
import time

## OLD STUFF

import random
from PIL import Image

class Map:
    """
    DATA = get_input(15)
    m = Map(DATA)
    m.show()
    """
    def __init__(self, data, colorseed=0):
        height = len(data)
        width = max([len(_) for _ in data])
        self.img = Image.new("P", (width,height))
        for y in range(height):
            for x in range(width):
                try:
                    self.set((x,y),data[y][x])
                except IndexError:
                    continue
        random.seed(colorseed)
        #             black  + white + 254 randomized RGB colours
        self.palette=[0,0,0] + [255,255,255] + [random.randint(0,255) for _ in range(254*3)]
        self.img.putpalette(self.palette)
        self.gif = []
        self.addtogif()

    def ival(self, val):
        # weirdly True is an int so test bool first!
        if isinstance(val, bool):
            return int(val)
        elif isinstance(val, int):
            return val
        elif isinstance(val, str) and len(val)==1:
            return ord(val)
        else:
            raise ValueError(f"{val}")

    def set(self, pos, val, out_of_range_is_error=True):
        """set pixel accepts int, bool, char"""
        val = self.ival(val)
        x, y = pos
        sx, sy = self.img.size
        if out_of_range_is_error or x<sx and y<sy:
            self.img.putpixel(pos,val)

    def get(self, pos):
        """get *integer* value
        cast it back to char or bool if needed"""
        return self.img.getpixel(pos)

    def resized(self):
        x,y = self.img.size
        while x<=200 and y<=200:
            x*=2
            y*=2
        return self.img.copy().resize((x,y))

    def show(self):
        """show the PIL image"""
        self.resized().show()

    def save(self, *args, **kwargs):
        """save the PIL image"""
        self.resized().save(*args,**kwargs)

    def setcolour(self, val, rgb):
        """
        set a byte/bool/char representation to
        a fixed RGB value
        e.g.
          self.setcolour("#",(255,0,0))
          self.setcolour(".",(0,0,255))
        """
        val = self.ival(val)
        r, g, b = rgb
        self.palette[val*3+0] = r
        self.palette[val*3+1] = g
        self.palette[val*3+2] = b
        self.img.putpalette(self.palette)

    def addtogif(self):
        self.gif.append(self.resized())

    def savegif(self, fname):
        self.gif[0].save(fname, append_images=self.gif[1:], save_all=True, duration=100, loop=1, palette=self.palette, optimize=True)

        ##
        #
     #######
    ## # # ##
     #######

    SUBMARINE = [(0, -2), (1, -2), (0, -1), (-4, 1), (4, 1), # periscope and ends
                 *[(_,0) for _ in range(-3, 4)], # roof
                 *[(_,1) for _ in range(-3, 4, 2)], # walls
                 *[(_,2) for _ in range(-3, 4)]] # floor
    SUBMARINE_WINDOWS = [(-2, 1), (0, 1), (2, 1)]

    def add_a_submarine(self, x, y, body='@'):
        self.setcolour(body, (255,255,0)) # yellow (obviously)
        for sx, sy in self.SUBMARINE:
            self.set((x+sx,y+sy), body, out_of_range_is_error=False)
        for sx, sy in self.SUBMARINE_WINDOWS:
            self.set((x+sx,y+sy), 0, out_of_range_is_error=False)

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

TRACE=pdb.set_trace

def load(n):
    f = Path(__file__).parent / "input" / f"{n}.txt"
    if f.is_file():
        return f.read_text()
    return ''

def day(ospath):
    n = int(Path(ospath).stem[3:])
    return n

import importlib
import traceback
from pathlib import Path
from types import SimpleNamespace
import time

TESTS = SimpleNamespace(
    FAILED = 0,
    PASSED = 0,
    EXECUTED = 0,
    ERRORS = 0,
    SKIPPED = 0)

REPORT = """
###### Totals #######

EXECUTED = {}
PASSED = {}
FAILED = {}
ERRORS = {}
SKIPPED = {}
"""

def show(*funcs):
    part = 1
    for func in funcs:
        t1 = time.time()
        ret = func()
        elapsed = time.time()-t1
        if ret is None:
            TESTS.SKIPPED += 1
            return
        TESTS.EXECUTED += 1
        expect = None
        try:
            expect = func.__defaults__[0]
        except TypeError:
            pass
        if expect:
            if ret == expect:
                print(f"\n    Part {part}\n    PASS: {ret}\n    in {elapsed:.3f} seconds")
                TESTS.PASSED += 1
            else:
                print(f"\n    Part {part}\n    FAIL: {ret} expected {expect}")
                TESTS.FAILED += 1
        else:
            print(f"\n    Part {part}\n    {ret}\n    in {elapsed:.3f} seconds")
        if part==2:
            print("")
        part += 1

def test():
    # import each module and run it's tests
    for n in range(1,26):
        module_name = f"day{n}"
        if (Path(__file__).parent / f"{module_name}.py").is_file():
            try:
                print(f"\n####### Day {n} #######\n")
                mod = importlib.import_module(module_name)
                mod.main()
            except:
                TESTS.ERRORS += 1
                traceback.print_exc()

    # print test report
    print(REPORT.format(
        TESTS.EXECUTED,
        TESTS.PASSED,
        TESTS.FAILED,
        TESTS.ERRORS,
        TESTS.SKIPPED))

if __name__ == "__main__":
    test()
