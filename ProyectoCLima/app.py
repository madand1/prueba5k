
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    lang = request.form['lang']
    units = request.form['units']

    api_key = '5bec4243e88e2d89184dfb14d75df481'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}&lang={lang}'

    response = requests.get(url)
    data = response.json()

    if 'name' not in data:
        return jsonify({'error': 'Ciudad no válida'}), 400
    else:
        return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
