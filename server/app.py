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
    humidity, temperature = Adafruit_DHT.read_entry(sensor,gpio)
    if humidity is not None and temperature is not None:
        json = {"humidity": humidity,"temperature": temperature}
        Return jsonify(json)
    
    else:
        json = {"humidity": 0, "temperature": 0}
        Return jsonify(json)
