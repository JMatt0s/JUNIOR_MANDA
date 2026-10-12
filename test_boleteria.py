import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("boleteria.py")


class PagoPseTests(unittest.TestCase):
    def ejecutar_flujo(self, resultado):
        respuestas = [
            "1",  # Localidad Occidental
            "2",  # Cantidad
            "3",  # PSE
            "1",  # Persona natural
            "1",  # CC
            "12345678",  # Documento ficticio
            "aprendiz@example.test",
            "2",  # Entidad de ejemplo
            resultado,
            "5",  # Salir
        ]
        directorio = tempfile.TemporaryDirectory()
        self.addCleanup(directorio.cleanup)
        ejecucion = subprocess.run(
            [sys.executable, str(SCRIPT)],
            input="\n".join(respuestas) + "\n",
            capture_output=True,
            check=True,
            cwd=directorio.name,
            text=True,
            timeout=5,
        )
        return ejecucion.stdout, Path(directorio.name)

    def test_aprobado_genera_factura_y_no_pide_claves_bancarias(self):
        salida, directorio = self.ejecutar_flujo("1")

        self.assertIn("Estado PSE simulado: APROBADO", salida)
        self.assertIn("No ingreses usuario ni contrasena", salida)
        self.assertNotIn("Usuario ficticio:", salida)
        self.assertNotIn("Contrasena ficticia:", salida)
        self.assertEqual(len(list(directorio.glob("factura_*.txt"))), 1)

    def test_resultados_no_aprobados_no_generan_factura(self):
        for opcion, estado in (("2", "RECHAZADO"), ("3", "PENDIENTE"), ("4", "CANCELADO")):
            with self.subTest(estado=estado):
                salida, directorio = self.ejecutar_flujo(opcion)

                self.assertIn(f"Estado PSE simulado: {estado}", salida)
                self.assertIn("No se genero la factura", salida)
                self.assertEqual(list(directorio.glob("factura_*.txt")), [])


if __name__ == "__main__":
    unittest.main()
