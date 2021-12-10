# import our helpers
from utils import load, show, day, TRACE, Map

####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__)).splitlines()

# parse the input
PARSED = [_.split() for _ in DATA]

######## Part 1 ##########
def p1(expect=514, viz=None):
    acc = 0
    for data in PARSED:
        for code in data[-4:]:
            if len(code) in (2,3,4,7):
                acc += 1
    return acc


######## Part 2 ##########
def get_digit_map(lettersoup):
    # add the keys after sorting jumbled letters
    digit_map = { ''.join(sorted(_)): None for _ in lettersoup }

    # get the easy digits
    for key in digit_map:
        if len(key) == 2:
            digit_map[key] = '1'
            one = key
        elif len(key) == 3:
            digit_map[key] = '7'
        elif len(key) == 4:
            digit_map[key] = '4'
            four = key
        elif len(key) == 7:
            digit_map[key] = '8'

    # find 2, 3, 5 using one and four
    for key in [k for k in digit_map.copy() if len(k)==5]:
        if len(set(one).intersection(set(key))) == 2:
            digit_map[key] = '3'
        elif len(set(four).union(set(key))) == 7:
            digit_map[key] = '2'
        else:
            digit_map[key] = '5'
            five = key

    # find 0, 6, 9 using one and five
    for key in [k for k in digit_map.copy() if len(k)==6]:
        if len(set(one).union(set(key))) == 7:
            digit_map[key] = '6'
        elif len(set(five).union(set(key))) == 7:
            digit_map[key] = '0'
        else:
            digit_map[key] = '9'

    return digit_map


def p2(expect=1012272, viz=None):
    acc = 0
    for data in PARSED:
        # map codes to digits
        digit_map = get_digit_map(data[:10])
        # decode the four code numbers
        code = [digit_map[''.join(sorted(_))] for _ in data[-4:]]
        acc += int(''.join(code))
    return acc

######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
