import csv
import toml
from datetime import datetime
from src.secundario import leer_argumentos, leer_csv, escribir_csv, leer_configuracion


def leer_configuracion(ruta_config="config.toml"):
    with open(ruta_config, "r", encoding="utf-8") as f:
        config = toml.load(f)
    return config

def procesar_ventas(filas, fecha_formato):
    datos = {}
    for fila in filas:
        prod = fila["Producto"]
        cant = int(fila["Cantidad"])
        precio = float(fila["ValorUnitario"])
        fecha = datetime.strptime(fila["Fecha"], fecha_formato)

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
    config = leer_configuracion()
    filas = leer_csv(archivo_in)
    datos = procesar_ventas(filas, config["fecha_formato"])
    escribir_csv(archivo_out, datos, config["columnas_salida"])
    mostrar_resultados(datos)

if __name__ == "__main__":
    main()