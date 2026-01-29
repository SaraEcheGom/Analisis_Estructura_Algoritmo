import csv

prioridad_tipo = {
    "mujer": 0,
    "hombre": 1,
    "apellido": 2
}

def leer_csv(ruta_archivo):
    listado = []
    with open(ruta_archivo, newline='', encoding='latin-1') as archivo:
        lector = csv.reader(archivo, delimiter=';')
        next(lector)
        for fila in lector:
            if len(fila) == 2:
                listado.append(fila)
    return listado



def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    mitad = len(lista) // 2
    izquierda = merge_sort(lista[:mitad])
    derecha = merge_sort(lista[mitad:])

    return merge(izquierda, derecha)


def merge(izq, der):
    resultado = []
    i = j = 0

    while i < len(izq) and j < len(der):
        clave_izq = (
            prioridad_tipo.get(izq[i][1].lower(), 99),
            izq[i][0].lower()
        )
        clave_der = (
            prioridad_tipo.get(der[j][1].lower(), 99),
            der[j][0].lower()
        )

        if clave_izq <= clave_der:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado


ruta = r"C:\Users\Sara Echeverri\Downloads\listado.csv"

datos = leer_csv(ruta)
datos_ordenados = merge_sort(datos)

print("Listado ordenado:")
for fila in datos_ordenados:
    print(fila)
