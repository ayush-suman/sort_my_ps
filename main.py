from helper import load_problem_bank, get_sortable_stations
from station import Industry

# Load Stations from Problem Bank
stations_list = load_problem_bank('problem_bank.html')

# Pushes your favourites to the top. Preferrably this should be the first sorting to be applied to the list
stations_list.pick_favourites(['Cenizas Labs'])

# Separates list into two brackets - stipend > 25000 pushed to top and stipend < 25000 (inclusive) pushed to the bottom
# You can create multiple brackets such as - [75000, 30000] will create brackets > 75000, < 75000 (inclusive) but > 30000, < 30000 (inclusive)
# If no value is passed to this function, it simply sorts the stations based on the stipend. Since this creates a bracket for every stipend offered, 
# further sort will be applied to those multiple small brackets created, and hence will be undesirable. If you wish to apply sorting by stipend 
# without brackets, apply this sort after you apply other sorts (by industry, by location etc.).
stations_list.sort_by_stipend([25000]) 

# Sorting applied earlier will have precedence over the latter. Since the list has been seggregated into two stipend brackets, this sort will arrange
# the list such that the upper part of the list will have all IT or FINANCE or NONE specified stations with stipend > 25000 first, then ELELCTRONICS (> 25000),
# HEALTHCARE (> 25000), OTHERS or MECHANICAL or INFRASTRUCTURE or CHEMICAL (> 25000). The lower part of the list will have the same order of domains but 
# will have stations offering stipend less than or equal to 25000.
stations_list.sort_by_industry([
    Industry.IT + Industry.NONE + Industry.FINNMGMT, 
    Industry.ELECTRONICS, 
    Industry.HEALTHCARE, 
    Industry.OTHERS + Industry.MECHANICAL + Industry.INFRASTRUCTURE + Industry.CHEMICAL
])

# Location wise sorting has tolerance for spelling errors
# stations_list.sort_by_location(['bangalore', 'mumbia'])

# Do not change the line below (Line No. 21)
stations_list.flatten()

# Load sortable Stations, apply sorting order from Stations_List, save
sortable_stations = get_sortable_stations('ps.html')
sortable_stations.apply_sorting(stations_list)
sortable_stations.save('ps_modified.html')
