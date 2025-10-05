from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/check', methods=['POST'])
def check_pollen():
    data = request.get_json()
    lat = data.get('latitude')
    lon = data.get('longitude')

    # Simulação de cálculo com base na latitude
    pollen_level = "High" if float(lat) > 0 else "Low"

    return jsonify({
        "latitude": lat,
        "longitude": lon,
        "pollen_potential": pollen_level
    })


if __name__ == "__main__":
    app.run(debug=True)


