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
- Python 3.x – Lenguaje de programación principal. Es un lenguaje de propósito general, de sintaxis sencilla y ampliamente utilizado para desarrollo web, automatización y ciencia de datos.

### Framework Web
- Flask – Microframework ligero para crear la aplicación web en Python. Maneja las rutas HTTP, los templates y la comunicación entre el front-end y el back-end.

### Módulos de Python (estándar, sin instalación extra)
- urllib.request – Módulo integrado de Python utilizado para realizar solicitudes HTTP a la API de tasas de cambio.
- json – Módulo integrado de Python para parsear y manipular las respuestas en formato JSON recibidas desde la API.

### API de Tasas de Cambio
- open.er-api.com – API pública y gratuita que provee tasas de cambio actualizadas en tiempo real. No requiere API key ni registro.

### Frontend
- HTML5 – Lenguaje de marcado utilizado para estructurar la interfaz de usuario.
- CSS3 – Lenguaje de estilos utilizado para el diseño visual, animaciones y diseño responsivo de la aplicación.
- JavaScript (Vanilla) – Lenguaje de programación del lado del cliente. Se utilizó para las llamadas al backend (fetch API) y la actualización dinámica de la interfaz sin recargar la página.
- Google Fonts – Servicio de fuentes tipográficas web. Se utilizaron las fuentes Playfair Display y DM Sans.

### Plantillas
- Jinja2 – Motor de plantillas integrado en Flask. Permite renderizar el HTML dinámicamente combinando datos de Python con la estructura HTML.

### Servidor de producción
- Gunicorn – Servidor WSGI para Python. Permite ejecutar la aplicación Flask en un entorno de producción real, reemplazando el servidor de desarrollo integrado de Flask.

### Control de versiones y despliegue
- Git – Sistema de control de versiones utilizado para rastrear los cambios en el código del proyecto.
- GitHub – Plataforma de alojamiento de repositorios Git en la nube. Permite almacenar, versionar y compartir el código del proyecto.
- **GitHub Desktop** – Aplicación de escritorio que facilita el uso de Git y GitHub mediante una interfaz gráfica, sin necesidad de usar comandos en la terminal.
- Render – Plataforma de despliegue en la nube (hosting) que permite publicar la aplicación web y obtener una URL pública accesible desde cualquier dispositivo con conexión a internet.

---

## Instalación y ejecución local

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
├── Procfile                # Configuración para Render
├── requirements.txt        # Dependencias del proyecto
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
- ✅ Desplegado en la nube con URL pública

---

*USAC – Escuela de Formación de Profesores de Enseñanza Media (EFPEM)*  
*Licenciatura en la Enseñanza de la Informática y Computación*  
*Curso: Programación VI – Lic. Lusvin de León*
