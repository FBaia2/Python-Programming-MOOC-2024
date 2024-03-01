import math



def get_station_data(filename: str):
    counter = 0
    lati = 0.0
    longi = 0.0
    latitude = []
    longitude = []
    nome_completo = []
    dicionario = {}
    with open(filename) as new_file:
    # with open("stations1.csv") as new_file:
        for line in new_file:   
            line = line.replace("\n", "")
            parts = line.split(';')
            if parts[0] == "Longitude":
                continue
            else:
                for i in parts:
                    if counter == 0:
                        counter +=1
                        longi = float(i)
                        longitude.append(longi)
                    elif counter == 1:
                        counter +=1
                        lati = float(i)
                        latitude.append(lati)
                    elif counter == 2:
                        counter +=1
                    elif counter == 3:
                        counter +=1
                        dicionario[i] = None
                    elif counter == 4:
                        counter +=1
                    elif counter == 5:
                        counter +=1
                    elif counter == 6:
                        counter = 0
    count = 0
    for i in dicionario:
        dicionario[i] = (longitude[count],latitude[count])
        count += 1 
    return dicionario 
      
def distance(stations: dict, station1: str, station2: str):
    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km
    
def greatest_distance(stations: dict):
    best = 0
    best_station1 = None
    best_station2 = None
    station_names = list(stations.keys())
    num_stations = len(station_names)
    for counter in range(num_stations):
        for counting in range(counter+1, num_stations):
            x_km = (stations[station_names[counter]][0] - stations[station_names[counting]][0]) * 55.26
            y_km = (stations[station_names[counter]][1] - stations[station_names[counting]][1]) * 111.2
            distance_km = math.sqrt(x_km**2 + y_km**2)
            if distance_km > best:
                best = distance_km
                best_station1 = station_names[counter]
                best_station2 = station_names[counting]
    return best_station1, best_station2, best


if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)