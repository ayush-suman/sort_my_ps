from thefuzz import fuzz



def index_of_best_match(value, array, tolerance = 0.6):
    max_ratio = tolerance
    index = len(array)
    for i, a in enumerate(array):
        match_ratio = fuzz.ratio(value.lower(), a.lower())
        if match_ration > max_ratio:
            index = i
            max_ratio = match_ratio

    return index

