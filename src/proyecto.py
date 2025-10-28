import csv

from datetime import datetime
from src.secundario import leer_argumentos, leer_csv

def procesar_ventas(filas):
    datos = {}
    for fila in filas:
        prod = fila["Producto"]
        cant = int(fila["Cantidad"])
        precio = float(fila["ValorUnitario"])
        fecha = datetime.strptime(fila["Fecha"], "%d/%m/%Y")

        if prod not in datos:
            datos[prod] = {
                "fecha_inicio": fecha,
                "fecha_fin": fecha,
                "cantidad": cant,
                "valor_total": cant * precio
            }
        else:
            if fecha < datos[prod]["fecha_inicio"]:
                datos[prod]["fecha_inicio"] = fecha

            if fecha > datos[prod]["fecha_fin"]:
                datos[prod]["fecha_fin"] = fecha
            datos[prod]["cantidad"] += cant
            datos[prod]["valor_total"] += cant * precio
    return datos


def escribir_csv(archivo_out, datos):
    campos = ["Producto", "FechaInicio", "FechaFin", "Cantidad", "ValorTotal"]

    with open(archivo_out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for prod, info in datos.items():
            writer.writerow({
                "Producto": prod,
                "FechaInicio": info["fecha_inicio"].strftime("%d/%m/%Y"),
                "FechaFin": info["fecha_fin"].strftime("%d/%m/%Y"),
                "Cantidad": info["cantidad"],
                "ValorTotal": round(info["valor_total"], 2)
            })

def mostrar_resultados(datos):
    for prod, info in datos.items():
        print(f"Producto: {prod}")
        print(f"  Fecha inicio: {info['fecha_inicio'].strftime('%d/%m/%Y')}")
        print(f"  Fecha fin: {info['fecha_fin'].strftime('%d/%m/%Y')}")
        print(f"  Cantidad total: {info['cantidad']}")
        print(f"  Valor total: {round(info['valor_total'], 2)}")
        print()

def main():
    archivo_in, archivo_out = leer_argumentos()
    filas = leer_csv(archivo_in)
    datos = procesar_ventas(filas)
    escribir_csv(archivo_out, datos)
    mostrar_resultados(datos)

if __name__ == "_main_":
    main()