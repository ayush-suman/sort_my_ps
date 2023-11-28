from thefuzz import fuzz

def get_best_match_index(value, array, tolerance = 60):
    max_ratio = tolerance
    index = len(array)
    for i, a in enumerate(array):
        match_ratio = fuzz.partial_ratio(value.lower(), a.lower())
        if match_ratio > max_ratio:
            index = i
            max_ratio = match_ratio

    return index


def get_order_index(array, value):
    try:
        return array.index(value)
    except:
        return len(array)
    

def get_bracket_index(array, value):
    def search_between(start, end):    
        if start <= end:
            index = (start + end) // 2
            if value == array[index]:
                return index
            elif value < array[index]:
                return search_between(index + 1, end)
            else:
                return search_between(start, index - 1)
            
        else:
            return start
    return search_between(0, len(array) - 1)
    