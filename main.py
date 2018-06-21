from flask import Flask, render_template
from RPi import GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(2, gpio.OUT)
gpio.setup(5, gpio.OUT)
gpio.output(5, gpio.HIGH)

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/ledon')
def ledon():
    gpio.output(2, gpio.HIGH)
    return(500)

@app.route('/ledoff')
def ledoff():
    gpio.output(2, gpio.LOW)
    return(500)

if __name__ == '__main__':
    app.run(host='192.168.1.60')