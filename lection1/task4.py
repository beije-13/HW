from itertools import combinations

def bananas(s):
    TARGET_STRING = "banana"
    REPLACEMENT = "-"
    input_string = list(s)
    index_list = range(0, len(input_string))

    combos = list(combinations(input_string, len('banana')))
    index_reverse_combos = list(combinations(index_list, len(input_string)-len(TARGET_STRING)))
    index_reverse_combos.reverse()
    output = set()
    
    for n, word in enumerate(combos):
        if "".join(word) == "banana":
            string_copy = input_string.copy()
            for excluded_index in index_reverse_combos[n]:
                string_copy[int(excluded_index)] = REPLACEMENT
            output.add("".join(string_copy))
    return output

assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
