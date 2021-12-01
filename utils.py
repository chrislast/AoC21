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
        self.height = len(data)
        self.width = max([len(_) for _ in data])
        self.img = Image.new("P", (self.width,self.height))
        for y in range(self.height):
            for x in range(self.width):
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

    def set(self, pos, val):
        """set pixel accepts int, bool, char"""
        val = self.ival(val)
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
