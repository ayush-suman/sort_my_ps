import itertools
from utils import index_of_best_match

def sort_by_industry(stations_list, order):
    if isinstance(stations_list[0], list):
        for stations in stations_list:
            stations = sort_by_industry(stations, order)
    else:
        stations_list.sort(key = lambda station: order.index(station.industry))
        stations_list = [list(g) for k, g in itertools.groupby(stations_list, lambda station: order.index(station.industry))]
    return stations_list


def sort_by_stipend(stations_list):
    if isinstance(stations_list[0], list):
        for stations in stations_list:
            stations = sort_by_stipend(stations)
    else:
        stations_list.sort(key = lambda station: station.stipend, reverse=True) 
        stations_list = [list(g) for k, g in itertools.groupby(stations_list, lambda station: station.stipend)]
    return stations_list


def sort_by_location(stations_list, locations):
    if isinstance(stations_list[0], list):
        for stations in stations_list:
            stations = sort_by_location(stations, locations)
    else:
        stations_list.sort(key = lambda station: index_of_best_match(station.location, locations))
        stations_list = [list(g) for k, g in itertools.groupby(stations_list, lambda station: index_of_best_match(station.location, locations))]
    return stations_list


def flatten(stations_list):
    flattened_list = []
    for stations in stations_list:
        if isinstance(stations[0], list):
            flattened_list += flatten(stations)
        else:
            flattened_list += stations
    return flattened_list
