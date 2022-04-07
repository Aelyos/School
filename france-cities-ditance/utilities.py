from math import radians, cos, sin, asin, sqrt
from urllib.request import urlopen

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r

# organize data
def organize_data():
    url = "https://devw.github.io/supn/data/laposte_hexasmal.small.csv"
    response = urlopen(url)
    data = response.read().decode('utf-8')
    lines = data.split("\n")
    for line in lines:
      fields = line.split(";")
      print("CAP", fields[0])

organize_data()
