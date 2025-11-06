import csv
import argparse
    

def leer_argumentos():
    parser = argparse.ArgumentParser(
        description="Procesa un archivo CSV de ventas y genera un resumen por producto."
    )
    parser.add_argument("archivo_in", help="Ruta del archivo CSV de entrada")
    parser.add_argument("archivo_out", help="Ruta del archivo CSV de salida")
    args = parser.parse_args()
    return args.archivo_in, args.archivo_out


def leer_csv(archivo_in):
    with open(archivo_in, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        return list(lector)


def mergesort(lista):
    if len(lista) <= 1:
        return lista

    mitad = len(lista) // 2
    izquierda = mergesort(lista[:mitad])
    derecha = mergesort(lista[mitad:])
    return merge(izquierda, derecha)


def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i][1]["valor_total"] >= derecha[j][1]["valor_total"]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


def escribir_csv(archivo_out, datos, columnas_salida):
    lista_datos = list(datos.items())

    lista_ordenada = mergesort(lista_datos)

    with open(archivo_out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columnas_salida)
        writer.writeheader()
        for prod, info in lista_ordenada:
            writer.writerow({
                "Producto": prod,
                "FechaInicio": info["fecha_inicio"].strftime("%d/%m/%Y"),
                "FechaFin": info["fecha_fin"].strftime("%d/%m/%Y"),
                "Cantidad": info["cantidad"],
                "ValorTotal": round(info["valor_total"], 2)
            })