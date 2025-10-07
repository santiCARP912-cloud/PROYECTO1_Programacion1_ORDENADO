import csv
from datetime import datetime

def main():
    archivo_in = "ventas.csv"      
    archivo_out = "ventas_salida.csv"  

    datos = {}

    with open(archivo_in, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            prod = fila["Producto"]
            cant = int(fila["Cantidad"])
            precio = float(fila["ValorUnitario"])
            fecha = datetime.strptime(fila["Fecha"], "%d/%m/%Y")

            if prod not in datos:
                datos[prod] = {
                    "fecha de Inicio": fecha,
                    "fecha de Finalizacion": fecha,
                    "Cantidad Vendida": cant,
                    "valor Total": cant * precio
                }
            else:
                if fecha < datos[prod]["fecha de Inicio"]:
                    datos[prod]["fecha de Inicio"] = fecha
                if fecha > datos[prod]["fecha de Finalizacion"]:
                    datos[prod]["fecha de Finalizacion"] = fecha
                datos[prod]["Cantidad Vendida"] += cant
                datos[prod]["valor Total"] += cant * precio

    #Nuevo archivo 
    campos = ["Producto", "FechaInicio", "FechaFin", "Cantidad", "ValorTotal"]

    with open(archivo_out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for prod, info in datos.items():
            writer.writerow({
                "Producto": prod,
                "FechaInicio": info["fecha de Inicio"].strftime("%d/%m/%Y"),
                "FechaFin": info["fecha de Finalizacion"].strftime("%d/%m/%Y"),   
                "Cantidad": info["Cantidad Vendida"],
                "ValorTotal": round(info["valor Total"], 2)
            })

    
    print("Resumen de ventas:\n")
    for prod, info in datos.items():
        print("Producto:", prod)
        print("  Fecha inicio:", info["fecha de Inicio"].strftime("%d/%m/%Y"))
        print("  Fecha fin:", info["fecha de Finalizacion"].strftime("%d/%m/%Y"))
        print("  Cantidad total:", info["Cantidad Vendida"])
        print("  Valor total:", round(info["valor Total"], 2))
        print()

if __name__ == "__main__":
    main()