# CambiaQ – Conversor de Moneda
## Proyecto Final · Programación VI · USAC-EFPEM · Helary Castro 202308320

---

## Descripción

Aplicación web desarrollada en Python + Flask que convierte entre 15 monedas diferentes usando tasas de cambio en tiempo real obtenidas desde la API pública `open.er-api.com`.

---

## Monedas soportadas (15)

| Código | Moneda |
|--------|--------|
| USD | Dólar estadounidense |
| GTQ | Quetzal guatemalteco |
| EUR | Euro |
| MXN | Peso mexicano |
| GBP | Libra esterlina |
| JPY | Yen japonés |
| CAD | Dólar canadiense |
| BRL | Real brasileño |
| COP | Peso colombiano |
| ARS | Peso argentino |
| CLP | Peso chileno |
| PEN | Sol peruano |
| CHF | Franco suizo |
| CNY | Yuan chino |
| HNL | Lempira hondureño |

---

## Herramientas utilizadas

### Lenguaje
- Python 3.x – Lenguaje de programación principal.

### Framework Web
- Flask – Microframework ligero para crear la aplicación web. Maneja las rutas HTTP, los templates y la comunicación entre front-end y back-end.

### Módulos de Python (estándar, sin instalación extra)
- urllib.request – Para realizar solicitudes HTTP a la API de tasas de cambio.
- json – Para parsear las respuestas JSON de la API.

### API de Tasas de Cambio
- open.er-api.com – API pública y gratuita que provee tasas de cambio actualizadas en tiempo real. No requiere API key.

### Frontend
- HTML5 / CSS3 – Estructura y estilos de la interfaz de usuario.
- JavaScript (Vanilla) – Lógica del cliente: llamadas al backend (fetch API), actualización dinámica de la interfaz.
- Google Fonts – Fuentes tipográficas: Playfair Display y DM Sans.

### Plantillas
- Jinja2 – Motor de plantillas integrado en Flask, usado para renderizar el HTML dinámicamente con los datos de Python.

---

## Instalación y ejecución

### Requisitos
- Python 3.8 o superior
- Conexión a Internet (para obtener tasas en tiempo real)

### Pasos

```bash
# 1. Instalar dependencias
pip install flask

# 2. Ejecutar la aplicación
python app.py

# 3. Abrir en el navegador
# http://localhost:5000
```

---

## Estructura del proyecto

```
conversor/
├── app.py                  # Backend Flask (lógica y rutas)
├── requirements.txt        # Dependencias
├── README.md               # Este archivo
└── templates/
    └── index.html          # Interfaz de usuario
```

---

## Funcionalidades

- ✅ Conversión entre 15 monedas distintas (supera el mínimo de 10)
- ✅ Tasas de cambio en tiempo real
- ✅ Interfaz web intuitiva y responsiva
- ✅ Tabla de todas las tasas desde la moneda seleccionada
- ✅ Botón de intercambio rápido de monedas
- ✅ Indicador de última actualización de la API
- ✅ Manejo de errores de conexión

---

*USAC – Escuela de Formación de Profesores de Enseñanza Media (EFPEM)*  
*Licenciatura en la Enseñanza de la Informática y Computación*  
*Curso: Programación VI – Lic. Lusvin de León*
