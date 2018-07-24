from heapq import *

def huffman_tree(symb2weights):
    heap = [[w, [sym, ""]] for sym, w in symb2weights.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
         
    return sorted(heappop(heap)[1:], key = lambda p: (len(p[-1]), p))

def import_weights(src):
    symbols_weights = {}
    file = open(src)
    i = 0
    n = file.readline()
    for line in file:
        symbols_weights[i] = int(line)
        i+=1
    return n, symbols_weights


def mergeCodes(l, r):
    l_wt, l_sym_code = l[:]
    r_wt, r_sym_code = r[:]
    for lpair in l_sym_code:
        lpair[1] = '0' + lpair[1]
    for rpair in r_sym_code:
        rpair[1] = '1' + rpair[1]
    return ([l_wt + r_wt] + l_sym_code + r_sym_code)
    