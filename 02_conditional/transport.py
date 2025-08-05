# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

km = 8

if km < 3:
    print('Walk')
elif km >= 3 and km <= 15:
    print('Bike')
elif km > 15:
    print('car')
    