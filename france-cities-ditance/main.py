import csv
from utilities import haversine

cities = []

with open('C:/Users/peael/Documents/code/france-cities-ditance/laposte_hexasmal.small.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        row = str(row)
        row = row.replace(']', '')
        row = row.replace("'", '')
        row = row.split(";")
        coordonees = row[5].split(",")
        cities.append({'nom': row[4], 'longitude': coordonees[0], 'latitude': coordonees[1]})

print(cities)

selected = input("Enter a city's name : ")

for city in cities:
    if city['nom'] in selected:
        selected_city = city

print(selected_city)

selected_distances = []

for city in cities:
    if city['nom'] in selected:
        elem = {}
        elem['nom'] = city['nom']
        elem['distance'] = 0
        selected_distances.append(elem)
    else:
        elem = {}
        elem['nom'] = city['nom']
        elem['distance'] = haversine(float(selected_city['latitude']), float(selected_city['longitude']), float(city['latitude']), float(city['longitude']))
        selected_distances.append(elem)

print(selected_distances)


