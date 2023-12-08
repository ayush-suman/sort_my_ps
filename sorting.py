from itertools import groupby, repeat
from typing import Iterable, Callable
from utils import get_best_match_index, get_order_index, get_bracket_index, get_bucket_index
from station import Station, Industry


class StationsListMeta(type):
    def __init_subclass__(cls, iterable) -> None:
        return super().__init_subclass__()


class StationsList(list[StationsListMeta | Station], metaclass=StationsListMeta):
    def __init__(self, iterable: Iterable[StationsListMeta]):
        super().__init__(iterable)


    def copy(self):
        return StationsList(self.__iter__())
    

    def __update__(self, iter: list[StationsListMeta | Station]):
        self.clear()
        self.extend(iter)


    def get(self, indices: int | list[int]) -> StationsList | Station:
        if isinstance(indices, int):
            return self[indices]
        else:
            index = indices.pop(0)
            if len(indices > 1):
                return self[index].get(indices)
            else:
                return self[index][indices[0]]


    def pop(self, indices: int | List[int]) -> StationsList | Station:
        if isinstance(indices, int):
            return super().pop(indices)
        else:
            index = indices.pop(0)
            if len(indices) > 1:
                return self[index].pop(indices)
            else:
                return self[index].pop(indices[0])


    def remove(self, station: Station):
        for stations in self:
            if isinstance(stations, Station):
                if station in self:
                    super().remove(station)
            else:
                stations.remove(station)


    def insert(self, indices: int | list[int], station: Station):
        if isinstance(indices, int):
            super().insert(indices, station)
        else:
            index = indices.pop(0)
            if len(indices) > 1:
                self[index].insert(indices, station)
            else:
                self[index].insert(indices[0], station)


    def add_to_top(self, stations: list[Station]):
        if len(stations) == 0:
            return
        for station in stations: 
            self.remove(station)
        self.__update__([StationsList(stations), self.copy()])


    def pick_favourites(self, favourites: list[str]):
        picks = StationsList(repeat(StationsList([]), len(favourites)))
        for stations in self:
            if isinstance(stations, StationsList):
                stations.pick_favourites(favourites)
            else:
                index = get_best_match_index(stations.company, favourites, tolerance=90)
                if index < len(favourites):
                    print("Added " + stations.get_name() + " as favourites")
                    picks[index].append(stations)
        picks.flatten()
        for pick in picks:
            self.remove(pick)
        self.__update__([picks, self.copy()])
    


    def sort_by_industry(self, order: list[Industry]):
        for stations in self:
            if isinstance(stations, StationsList):
                stations.sort_by_industry(order)
            else:
                self.sort(key = lambda station: get_order_index(order, station.industry))
                self.__update__([StationsList(g) for k, g in groupby(self, lambda station: get_order_index(order, station.industry))])
                return


    def sort_by_stipend(self, brackets: list[int] = None):
        for stations in self:
            if isinstance(stations, StationsList):
                stations.sort_by_stipend(brackets)
            else:
                self.sort(key = lambda station: station.stipend, reverse=True) 
                if brackets is not None:
                    brackets.sort()
                    self.__update__([StationsList(g) for k, g in groupby(self, lambda station: get_bracket_index(brackets, station.stipend))])
                return


    def sort_by_location(self, locations: list[str]):
        for stations in self:
            if isinstance(stations, StationsList):
                stations.sort_by_location(locations)
            else:
                self.sort(key = lambda station: get_best_match_index(station.location, locations))
                self.__update__([StationsList(g) for k, g in groupby(self, lambda station: get_best_match_index(station.location, locations))])
                return

    def sort_into_custom_buckets(self, buckets: list[Callable[[Station], bool]]):
        for stations in self:
            if isinstance(stations, StationsList):
                stations.sort_by_custom_buckets(buckets)
            else:
                self.sort(key = lambda station: get_bucket_index(bucket, station))
                self.__update__([StationsList(g) for k, g in groupby(lambda station: get_bucket_index(buckets, station))])
                return


    def flatten(self):
        flattened_list = []
        for stations in self:
            if isinstance(stations, StationsList):
                stations.flatten()
                flattened_list.extend(stations)
            else:
                flattened_list.append(stations)
        self.__update__(flattened_list)

