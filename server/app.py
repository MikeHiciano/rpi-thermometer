import Adafruit_DHT
from flask import Flask, render_template, jsonify, request, url_for
import requests
import threading 
import time

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

def thermometer_db():
    humidity, temperature = Adafruit_DHT.read_retry(sensor,gpio)
    measures = {"device":"bedroom","temperature":temperature,"humidity":humidity}
    requests.post("http://10.0.0.14:5000/device", json=measures)    
    time.sleep(30)

if __name__ == "__main__":
    
    thermo = threading.Thread(target=thermometer_db)
    thermo.start()
    app.run(debug=True,host="0.0.0.0")