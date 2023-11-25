from bs4 import BeautifulSoup as bs
from station import Station, Industry
from sorting import sort_by_stipend, sort_by_industry, sort_by_location, flatten
import os

base = os.path.dirname(os.path.abspath(__file__))

problem_bank = open(os.path.join(base, 'problem_bank.html'))

soup_1 = bs(problem_bank, 'html.parser')
body = soup_1.find("tbody", {"id": "PBData"})
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
    print("inserting " + station.company)
    stations_list.append(station)

stations_list = sort_by_industry(stations_list, [Industry.IT, Industry.FINNMGMT, Industry.ELECTRONICS, Industry.INFRASTRUCTURE, Industry.HEALTHCARE, Industry.MECHANICAL, Industry.OTHERS, Industry.CHEMICAL])

stations_list = sort_by_stipend(stations_list)

stations_list = flatten(stations_list)

ps = open(os.path.join(base, 'ps.html'))
soup_2 = bs(ps, 'html.parser')
form = soup_2.find("form")
sortable_nav = form.find("ul", {"id": "sortable_nav"})
stations = sortable_nav.find_all("li")
stations_count = len(stations)

def bsearch_station_index(station_array, name, start, end):
    if end >= start:
        index = (start + end) // 2
        if station_array[index].find('span').text.strip() == name:
            return index
        elif station_array[index].find('span').text.strip() > name:
            return bsearch_station_index(station_array, name, start, index - 1)
        else:
           return bsearch_station_index(station_array, name, index + 1, end)
    else:
        return -1

sortable_nav.clear()
for i, station in enumerate(stations_list):
    index = bsearch_station_index(stations, station.get_name(), 0, stations_count)   
    stations[index].div.span.string = str(i + 1)
    print(stations[index].div.span.string)
    sortable_nav.append(stations[index])

#sortable_nav.clear()
#for station in arranged_stations:
#    sortable_nav.append(station)

#print(stations)
with open("ps_modified.html", "wb") as f_output:
    f_output.write(soup_2.prettify("utf-8"))
    
