try:
    from flask import Flask, render_template
    from dateutil.tz import *
    from flask_restful import Resource,Api
    from flask_restful import reqparse
    from flask import request
    import time
    import RPi.GPIO as GPIO
    from datetime import datetime
    import json
    import dht11
    print("All Module loaded")
except Exception as e:
    print("Error: {}".format(e))


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
instance = dht11.DHT11(pin=17)

app = Flask(__name__)
api = Api(app)
@app.route("/")


def index():
    
    local = tzlocal()
    now = datetime.now()
    now = now.replace(tzinfo = local)
    timeString = now.strftime("%Y-%m-%d   %H:%M")
    temperature, humidity = sensor_DHT11()
    templateData = {'title':'Home Page','time':timeString,'temperature':temperature, 'humidity':humidity}
    return render_template('sensor.html', **templateData)


def sensor_DHT11():
    while True:
            result= instance.read()
            if result.is_valid():

                                
                return result.temperature, result.humidity
                    

if __name__=="__main__":
    app.run(host='192.168.0.101', debug=True, port=5001)
