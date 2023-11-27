import itertools
from fuzz_match import index_of_best_match

def _get_index(order, station):
    try:
        return order.index(station.industry)
    except:
        return len(order)
    

def sort_by_industry(stations_list, order):
    for stations in stations_list:
        if isinstance(stations, list):
            stations = sort_by_industry(stations, order)
        else:
            stations_list.sort(key = lambda station: _get_index(order, station))
            stations_list = [list(g) for k, g in itertools.groupby(stations_list, lambda station: _get_index(order, station))]
            break
    return stations_list


def sort_by_stipend(stations_list):
    for stations in stations_list:
        if isinstance(stations, list):
            stations = sort_by_stipend(stations)
        else:
            stations_list.sort(key = lambda station: station.stipend, reverse=True) 
            stations_list = [list(g) for k, g in itertools.groupby(stations_list, lambda station: station.stipend)]
            break
    return stations_list


def sort_by_location(stations_list, locations):
    for stations in stations_list:
        if isinstance(stations, list):
            stations = sort_by_location(stations, locations)
        else:
            stations_list.sort(key = lambda station: index_of_best_match(station.location, locations))
            stations_list = [list(g) for k, g in itertools.groupby(stations_list, lambda station: index_of_best_match(station.location, locations))]
            break
    return stations_list


def flatten(stations_list):
    flattened_list = []
    for stations in stations_list:
        if isinstance(stations, list):
            flattened_list += stations
        else:
            return stations_list
    return flatten(flattened_list)
