from helper import load_problem_bank, get_sortable_stations
from station import Industry
from sorting import sort_by_stipend, sort_by_industry, flatten

# Load Stations from Problem Bank
stations_list = load_problem_bank('problem_bank.html')

# Apply sorting. Sorting applied earlier will have precedence over the latter.
stations_list = sort_by_industry(stations_list, [
    Industry.IT + Industry.NONE + Industry.FINNMGMT, 
    Industry.ELECTRONICS, 
    #Industry.HEALTHCARE, 
    Industry.OTHERS + Industry.MECHANICAL + Industry.INFRASTRUCTURE + Industry.CHEMICAL
])

stations_list = sort_by_stipend(stations_list)

# stations_list = sort_by_location(stations_list, ["Bangalore", "Mumbai"])

# Do not change the line below (Line No. 24)
stations_list = flatten(stations_list)

# Load sortable Stations, apply sorting order from Stations_List, save
sortable_stations = get_sortable_stations('ps.html')
sortable_stations.apply_sorting(stations_list)
sortable_stations.save('ps_modified.html')
