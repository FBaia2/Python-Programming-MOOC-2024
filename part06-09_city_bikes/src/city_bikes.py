def get_station_data(filename: str):
    with open(filename) as new_file:
# with open("stations1.csv") as new_file:
        lati = 0.0
        longi = 0.0
        latitude = []
        longitude = []
        nome_completo = []
        dicionario = {}
        counter = 0
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
        
    
    
        
        
        
if __name__ == "__main__":
    
    stations = get_station_data("stations1.csv")
    print(stations)
    
    
    
    
