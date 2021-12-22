# import our helpers
from utils import load, show, day, TRACE
from dataclasses import dataclass
####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__))

# Parse input
MSG = bin(int(DATA, 16))[2:] # convert hex text to binary text
while len(MSG) & 3:
    MSG = "0" + MSG # pad with zeros at front if needed

@dataclass
class Packet:
    version: int=0
    ptype: int=0
    payload: object=None

######## Part 1 ##########
def get(i, n):
    return i+n, int(MSG[i:i+n],2)

def val(obj):
    if isinstance(obj, Packet):
        return obj.payload
    return obj

def decode_packet(i, decode_subpackets=False):
    pkt = Packet()
    i, pkt.version = get(i, 3)
    i, pkt.ptype = get(i, 3)
    # handle literals
    if pkt.ptype==4:
        acc = 0
        while True:
            i, more = get(i, 1)
            i, n = get(i, 4)
            acc = (acc<<4) + n
            if not more:
                pkt.payload = acc
                return i, pkt

    # handle operators
    i, lentype = get(i, 1)
    pkt.payload = []
    if lentype == 1:
        i, pktlen = get(i, 11)
        while pktlen:
            pktlen -= 1
            i, _pkt = decode_packet(i, decode_subpackets)
            pkt.payload.append(_pkt)
    else:
        i, pktlen = get(i, 15)
        end = i + pktlen
        while i < end:
            i, _pkt = decode_packet(i, decode_subpackets)
            pkt.payload.append(_pkt)

    if decode_subpackets:
        # 0 = sum of subpackets
        if pkt.ptype==0:
            pkt.payload = sum([val(_) for _ in pkt.payload])

        # 1 = product of subpackets
        elif pkt.ptype==1:
            acc = 1
            for subpacket in pkt.payload:
                acc *= val(subpacket.payload)
            pkt.payload = acc

        # 2 = minimum packet value
        elif pkt.ptype==2:
            pkt.payload = min([val(_) for _ in pkt.payload])

        # 3 = maximum packet value
        elif pkt.ptype==3:
            pkt.payload = max([val(_) for _ in pkt.payload])

        # 5 = sub1 greater than sub2
        elif pkt.ptype==5:
            pkt.payload = int(val(pkt.payload[0]) > val(pkt.payload[1]))

        # 6 = sub1 less than sub2
        elif pkt.ptype==6:
            pkt.payload = int(val(pkt.payload[0]) < val(pkt.payload[1]))

        # 7 = sub1 equal to sub2
        elif pkt.ptype==7:
            pkt.payload = int(val(pkt.payload[0]) == val(pkt.payload[1]))

    return i, pkt

def addversions(pkt):
    if isinstance(pkt.payload, int):
        return pkt.version
    return pkt.version + sum([addversions(p) for p in pkt.payload])

def p1(expect=963, viz=None):
    _, packet = decode_packet(0)
    return addversions(packet)

######## Part 2 ##########
def p2(expect=1549026292886, viz=None):
    _, packet = decode_packet(0, True)
    return packet.payload

######### Main ###########
def main():
    show(p1,p2)

if __name__ == "__main__":
    main()
