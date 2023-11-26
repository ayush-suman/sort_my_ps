import os
from bs4 import BeautifulSoup as bs
from station import Station, Industry


def load_problem_bank(filename):
    base = os.path.dirname(os.path.abspath(__file__))
    problem_bank = open(os.path.join(base, filename))

    soup = bs(problem_bank, 'html.parser')
    body = soup.find("tbody", {"id": "PBData"})
    rows = body.find_all("tr")

    stations_list = []

    for row in rows:
        company_name = row.find("td", {"id": "stationname"}).text.strip()
        last_index = company_name.rfind('(')
        company = company_name[:last_index]
        industry_name = row.find("td", {"id": "Industry"}).text.strip()
        industry = Industry.from_name(industry_name)
        location = row.find("td", {"id": "lOCATION"}).text.strip()
        stipend = int(row.find("td", {"id": "stipend"}).text.strip())
        station = Station(company = company, industry = industry, location = location, stipend = stipend)
        stations_list.append(station)

    return stations_list


class Sortable:
    def __init__(self, soup):
        self.soup = soup
        self.sortable_nav = self.soup.find("form").find("ul", {"id": "sortable_nav"})
        self.stations = self.sortable_nav.find_all("li")
        self.sortable_nav.clear()


    def __append__(self, name, start = 0, end = -1):
        if end < 0: 
            end += len(self.stations)
        
        if end >= start:
            index = (start + end) // 2
            if self.stations[index].find('span').text.strip() == name:
                i = len(self.sortable_nav.find_all("li")) + 1
                self.stations[index].div.span.string = str(i)
                self.sortable_nav.append(self.stations[index])
            elif self.stations[index].find('span').text.strip() > name:
                self.__append__(name, start, index - 1)
            else:
                self.__append__(name, index + 1, end)
        

    def apply_sorting(self, stations_list: list[Station]):
        for station in stations_list:
            self.__append__(station.get_name())

        
    def save(self, filename):
        with open(filename, "wb") as f_output:
            f_output.write(self.soup.prettify("utf-8"))


def get_sortable_stations(filename):
    base = os.path.dirname(os.path.abspath(__file__))
    ps = open(os.path.join(base, filename))
    soup = bs(ps, 'html.parser')
    sortable = Sortable(soup)
    return sortable


