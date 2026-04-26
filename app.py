from flask import Flask, render_template, request, jsonify
import urllib.request
import json

app = Flask(__name__)

# Monedas soportadas (mínimo 10)
MONEDAS = {
    "USD": "Dólar estadounidense 🇺🇸",
    "GTQ": "Quetzal guatemalteco 🇬🇹",
    "EUR": "Euro 🇪🇺",
    "MXN": "Peso mexicano 🇲🇽",
    "GBP": "Libra esterlina 🇬🇧",
    "JPY": "Yen japonés 🇯🇵",
    "CAD": "Dólar canadiense 🇨🇦",
    "BRL": "Real brasileño 🇧🇷",
    "COP": "Peso colombiano 🇨🇴",
    "ARS": "Peso argentino 🇦🇷",
    "CLP": "Peso chileno 🇨🇱",
    "PEN": "Sol peruano 🇵🇪",
    "CHF": "Franco suizo 🇨🇭",
    "CNY": "Yuan chino 🇨🇳",
    "HNL": "Lempira hondureño 🇭🇳",
}


def obtener_tasas(base: str):
    """Obtiene tasas de cambio en tiempo real desde la API pública."""
    url = f"https://open.er-api.com/v6/latest/{base}"
    try:
        with urllib.request.urlopen(url, timeout=8) as response:
            data = json.loads(response.read().decode())
            if data.get("result") == "success":
                return data["rates"], data.get("time_last_update_utc", "")
    except Exception as e:
        print(f"Error al obtener tasas: {e}")
    return None, None


@app.route("/")
def index():
    return render_template("index.html", monedas=MONEDAS)


@app.route("/convertir", methods=["POST"])
def convertir():
    datos = request.get_json()
    cantidad = float(datos.get("cantidad", 0))
    moneda_origen = datos.get("origen", "USD")
    moneda_destino = datos.get("destino", "GTQ")

    if cantidad <= 0:
        return jsonify({"error": "La cantidad debe ser mayor a 0"}), 400

    tasas, actualizado = obtener_tasas(moneda_origen)

    if tasas is None:
        return jsonify({"error": "No se pudo conectar a la API de tasas de cambio"}), 503

    if moneda_destino not in tasas:
        return jsonify({"error": f"Moneda destino no soportada: {moneda_destino}"}), 400

    tasa = tasas[moneda_destino]
    resultado = cantidad * tasa

    return jsonify({
        "resultado": round(resultado, 4),
        "tasa": round(tasa, 6),
        "origen": moneda_origen,
        "destino": moneda_destino,
        "cantidad": cantidad,
        "actualizado": actualizado,
    })


@app.route("/todas_tasas", methods=["POST"])
def todas_tasas():
    datos = request.get_json()
    base = datos.get("base", "USD")
    tasas, actualizado = obtener_tasas(base)

    if tasas is None:
        return jsonify({"error": "No se pudo obtener tasas"}), 503

    # Filtrar solo las monedas que soportamos
    tasas_filtradas = {k: round(v, 4) for k, v in tasas.items() if k in MONEDAS}
    return jsonify({"tasas": tasas_filtradas, "base": base, "actualizado": actualizado})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
