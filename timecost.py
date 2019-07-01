import math


# Compute the cost of commute route relative to how long it takes.
def get_time_cost(route, duration):
    print(
        f'A minute costs{duration/math.fsum(route): .2f} pesos if you take this commute route')


# Mode of transportation fare
tricycleFare = 30
jeepneyFare = 9
grabFare = 350
taxiFare = 300
fxFare = 15

# Get to the office via tricycle, fx and 2 jeepney rides which will take around 90 minutes.
routeA = []
routeA.append(tricycleFare)
routeA.append(fxFare)
routeA.append(jeepneyFare)
routeA.append(jeepneyFare)

# A minute costs 1.43 pesos if you take this commute route
get_time_cost(routeA, 90)

# Get to the office via 3 jeepney rides which will take around 115 minutes.
routeB = []
routeB.append(jeepneyFare)
routeB.append(jeepneyFare)
routeB.append(jeepneyFare)

# A minute costs 4.26 pesos if you take this commute route
get_time_cost(routeB, 115)

# Get to the office via Grab which will take around 45 minutes.
# A minute costs 0.13 pesos if you take this commute route
get_time_cost([grabFare], 45)

# Get to the office via Taxi which will take around 60 minutes.
# A minute costs 0.20 pesos if you take this commute route
get_time_cost([taxiFare], 60)
