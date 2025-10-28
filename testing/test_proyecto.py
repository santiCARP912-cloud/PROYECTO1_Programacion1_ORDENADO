import sys
import os
import unittest
import csv
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) #unico arreglo que encontre para que encuentre la ruta correcta.

from src.proyecto import procesar_ventas, escribir_csv


class TestVentas(unittest.TestCase):

    def setUp(self):
        self.datos_csv = [
            {"Fecha": "01/03/2024", "Producto": "CocaCola", "Cantidad": "10", "ValorUnitario": "2000"},
            {"Fecha": "02/03/2024", "Producto": "Pepsi", "Cantidad": "5", "ValorUnitario": "1800"},
            {"Fecha": "03/03/2024", "Producto": "CocaCola", "Cantidad": "7", "ValorUnitario": "2000"},
            {"Fecha": "04/03/2024", "Producto": "Fanta", "Cantidad": "8", "ValorUnitario": "2000"},
            {"Fecha": "05/03/2024", "Producto": "Pepsi", "Cantidad": "4", "ValorUnitario": "1800"},
            {"Fecha": "06/03/2024", "Producto": "Fanta", "Cantidad": "6", "ValorUnitario": "1800"},
        ]

        self.archivo_salida = "ventas_resumen_test.csv"


    def test_procesar_ventas(self):
        resumen = procesar_ventas(self.datos_csv)

        self.assertEqual(resumen["CocaCola"]["cantidad"], 17)
        self.assertEqual(round(resumen["CocaCola"]["valor_total"], 2), 34000)

        self.assertEqual(resumen["Pepsi"]["cantidad"], 9)
        self.assertEqual(round(resumen["Pepsi"]["valor_total"], 2), 16200)

        #Fechas de inicio y de fin
        fecha_inicio_coca = datetime.strptime("01/03/2024", "%d/%m/%Y")
        fecha_fin_coca = datetime.strptime("03/03/2024", "%d/%m/%Y")
        self.assertEqual(resumen["CocaCola"]["fecha_inicio"], fecha_inicio_coca)
        self.assertEqual(resumen["CocaCola"]["fecha_fin"], fecha_fin_coca)

    def test_escribir_csv(self):
        datos = {
            "CocaCola": {
                "fecha_inicio": datetime.strptime("01/03/2024", "%d/%m/%Y"),
                "fecha_fin": datetime.strptime("03/03/2024", "%d/%m/%Y"),
                "cantidad": 17,
                "valor_total": 34000
            }
        }

        escribir_csv(self.archivo_salida, datos)

        self.assertTrue(os.path.exists(self.archivo_salida))

        with open(self.archivo_salida, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            filas = list(lector)

        self.assertEqual(len(filas), 1)
        self.assertEqual(filas[0]["Producto"], "CocaCola")
        self.assertEqual(filas[0]["Cantidad"], "17")
        self.assertEqual(filas[0]["ValorTotal"], "34000.0")


if __name__ == "__main__":
    unittest.main()
