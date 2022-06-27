from math import log, prod, floor
from itertools import combinations_with_replacement

def count_find_num(primesL, limit):
    true_limit = floor(log(limit, primesL[0]))
    result = []

    for i in range(len(primesL),true_limit+1):
        res = list(combinations_with_replacement(primesL, i))
        for item in res:
            if set(primesL).issubset(item):
                p = prod(item)
                if p <= limit:
                    result.append(p)
    
    if result:
        return [len(result), max(result)]
    else:
        return []


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []
