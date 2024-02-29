def create_tuple(x: int, y: int, z: int):
    lista = []
    lista.append(x)
    lista.append(y)
    lista.append(z)
    lista.sort()
    
    tupla = (lista[0], lista[2], lista[0] + lista[1] + lista[2])
    return tupla
if __name__ == "__main__":
    print(create_tuple(5, 3, -1))