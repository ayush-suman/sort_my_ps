import os
from bs4 import BeautifulSoup as bs
from station import Station, Industry
from thefuzz import fuzz


def load_problem_bank(filename):
    base = os.path.dirname(os.path.abspath(__file__))
    problem_bank = open(os.path.join(base, filename))

    soup = bs(problem_bank, 'html.parser')
    body = soup.find("tbody", {"id": "PBData"})
    rows = body.find_all("tr")

    stations_list = []

    for row in rows:
        location = row.find("td", {"id": "lOCATION"}).text
        company_name = row.find("td", {"id": "stationname"}).text.strip()
        # last_index = company_name.rfind('(' + location + ')')
        # company = company_name[:last_index]
        company = company_name.removesuffix('(' + location + ')')
        industry_name = row.find("td", {"id": "Industry"}).text.strip()
        industry = Industry(industry_name)
        stipend = int(row.find("td", {"id": "stipend"}).text.strip())
        station = Station(company = company, industry = industry, location = location, stipend = stipend)
        stations_list.append(station)

    return stations_list


class Sortable:
    def __init__(self, soup):
        self.__soup__ = soup
        self.__sortable_nav__ = self.__soup__.find("form").find("ul", {"id": "sortable_nav"})
        self.stations = self.__sortable_nav__.find_all("li")
        self.__sortable_nav__.clear()


    def __search__(self, name) -> int:  
        for index, station in enumerate(self.stations):
            if station.find('span').text == name:
                return index
        # Use slower Fuzzy match if not found
        for index, station in enumerate(self.stations):
            if fuzz.ratio(station.find('span').text, name) > 95:
                print("Fuzzy matched " + station.find('span').text + " with " + name)
                return index
        print("NOT FOUND: " + name)
        return index

    def apply_sorting(self, stations_list: list[Station]):
        length = len(self.stations)
        print("Total Station Count: " + str(length))
        for station in stations_list:
            index = self.__search__(station.get_name())
            if index != -1:
                i = len(self.__sortable_nav__.find_all("li")) + 1
                self.stations[index].div.span.string = str(i)
                self.__sortable_nav__.append(self.stations[index])

        
    def save(self, filename):
        with open(filename, "wb") as f_output:
            f_output.write(self.__soup__.prettify("utf-8"))


def get_sortable_stations(filename):
    base = os.path.dirname(os.path.abspath(__file__))
    ps = open(os.path.join(base, filename))
    soup = bs(ps, 'html.parser')
    sortable = Sortable(soup)
    return sortable


