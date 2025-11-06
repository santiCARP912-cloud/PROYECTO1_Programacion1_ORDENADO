import csv
import argparse
import json


def leer_configuracion():
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)
    

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
    

def escribir_csv(archivo_out, datos, columnas_salida):
    with open(archivo_out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columnas_salida)
        writer.writeheader()
        for prod, info in datos.items():
            writer.writerow({
                "Producto": prod,
                "FechaInicio": info["fecha_inicio"].strftime("%d/%m/%Y"),
                "FechaFin": info["fecha_fin"].strftime("%d/%m/%Y"),
                "Cantidad": info["cantidad"],
                "ValorTotal": round(info["valor_total"], 2)
            })