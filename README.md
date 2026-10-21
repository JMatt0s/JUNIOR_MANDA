# 🚩 Junior de Barranquilla

Proyecto de consola desarrollado en **Python** principalmente para la venta de entradas a los partidos del Club Deportivo Popular Junior F.C. Es un proyecto universitario originalmente. Ahora un proyecto apasionado al tiburón.   

> 🦈 *¡Junior Manda!*

---

## 📋 Descripción del proyecto original

Este proyecto originalmente permite simular la gestión y venta de boletas para partidos de Junior en el Estadio Metropolitano Roberto Meléndez o Estadio Municipal Romelio Martínez. Desde una interfaz de consola, el usuario puede consultar los partidos disponibles (aun en desarrollo), elegir una localidad, comprar boletas y revisar o cancelar sus compras.

## ✨ Funcionalidades

- Ver la lista de partidos disponibles (rival, fecha y hora) (AUN EN DESARROLLO). 
- Consultar localidades y precios.
- Calcular el valor total de la compra.
- Calculadora de resultados.
- Ver el historial de compras realizadas (aun en desarrollo).
- Cancelar una compra (devuelve los cupos a la localidad).

## 🏟️ Localidad Estadio Metropolitano Roberto Meléndez

| Localidad  | Precio (COP) | Capacidad |
|------------|--------------|-----------|
| Norte      | $30.000      | x        |
| Sur        | $30.000      | x        |
| Oriental   | $50.000      | x        |
| Occidental | $100.000     | x        |

## 🏟️ Localidades Estadio Municipal Romelio Martínez

| Localidad  | Precio (COP) | Capacidad |
|------------|--------------|-----------|
| Norte      | $30.000      | 3464     |
| Oriental   | $50.000      | 2612     |
| Occidental | $100.000     | 2500     |

> Los valores son de ejemplo y se pueden modificar en el código.

## 🛠️ Tecnologías

- **Lenguaje:** Python 3.10 o superior
- **Interfaz:** Consola (terminal)
- **Librerías:** solo la biblioteca estándar de Python (no requiere instalar nada extra)

## 📁 Estructura del proyecto

```
boleteria-junior/
│
├── inicio.py            # Punto de entrada y menú principal
├── partidos.py        # Gestión de partidos
├── Junior_boleteria.py    # Compra de boletas
├── datos/
│   └── datos.json     # Almacenamiento de partidos y compras (opcional)
└── README.md
```

## 🚀 Instalación y ejecución

1. Verifica que tengas Python instalado:

   ```bash
   python --version
   ```

2. Clona el repositorio o descarga el proyecto:

   ```bash
   git clone https://github.com/tu-usuario/boleteria-junior.git
   cd boleteria-junior
   ```

3. Ejecuta el programa:

   ```bash
   python inicio.py
   ```

## 💻 Ejemplo de uso

```
===== BOLETERÍA JUNIOR DE BARRANQUILLA =====
1. Ver partidos disponibles
2. Comprar boletas
3. Ver mis compras
4. Cancelar compra
5. Salir

Seleccione una opción: 1

--- Partidos disponibles ---
1. Junior vs Millonarios  | 15/11/2026 | 8:00 PM
2. Junior vs Nacional     | 22/11/2026 | 6:00 PM
```

## 🧠 Conceptos aplicados

- Variables, listas y diccionarios
- Funciones y modularización
- Estructuras de control (`if`, `while`, `for`)
- Validación de entradas del usuario
- Manejo de errores con `try / except`
- Programación orientada a objetos y manejo de archivos JSON

## 🔮 Mejoras futuras

- Registro e inicio de sesión de usuarios.
- Calendario de partidos.
- Descuentos para abonados.
- Interfaz gráfica o versión web.
- Conexión a una base de datos.
- ## NOTA: A medida que desarrollo este proyecto habrá mejoras significativa  

## 👥 Autor

- 📸**IG** - @mattoss99_ https://www.instagram.com/mattoss99_/
- **Juan Mattos** - @JMatt0s https://github.com/usuario](https://github.com/JMatt0s

## 📄 Licencia

Proyecto académico sin fines comerciales. Junior de Barranquilla es una marca de su respectivo propietario; este proyecto no tiene afiliación oficial con el club. (solo soy hicha del tiburon 🦈 ❤️)
