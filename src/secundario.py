import csv
import argparse

def leer_argumentos():
    parser = argparse.ArgumentParser(
        description = "Procesa un archivo CSV de ventas y genera un resumen por producto."
    )
    parser.add_argument("archivo_in", help="Ruta del archivo CSV de entrada")
    parser.add_argument("archivo_out", help="Ruta del archivo CSV de salida")
    args = parser.parse_args()
    return args.archivo_in, args.archivo_out


def leer_csv(archivo_in):
    with open(archivo_in, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        return list(lector)