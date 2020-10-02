import Adafruit_DHT
from flask import Flask, render_template, jsonify, request

sensor = Adafruit_DHT.DHT11
gpio = 17
app = Flask(__name__,
            static_url_path='',
            static_folder='templates/static',
            template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/thermometer')
def thermometer():
    humidity, temperature = Adafruit_DHT.read_retry(sensor,gpio)
    data = {"humidity":humidity,"temperature":temperature}
    return jsonify({"data": data})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
