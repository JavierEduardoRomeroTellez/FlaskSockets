from flask import Flask, render_template
from flask_socketio import SocketIO, send
from gpiozero import LED

led1 = LED(18)
led_state1 = False
led2 = LED(23)
led_state2 = False
led3 = LED(24)
led_state3 = False

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

socketio = SocketIO(app)

@app.route('/')
def index():
   return render_template('index.html')

@socketio.on('turnOnLed1')
def turnOnLED():
    print("Encender led")
    led1.on()
    led_state1 = True
    send('True', broadcast = True)

@socketio.on('turnOffLed1')
def turnOffLED():
    print("Apagar led")
    led1.off()
    led_state1 = False
    send('False', broadcast = True)

@socketio.on('turnOnLed2')
def turnOnLED():
    print("Encender led")
    led2.on()
    led_state2 = True
    send('True', broadcast = True)

@socketio.on('turnOffLed2')
def turnOffLED():
    print("Apagar led")
    led2.off()
    led_state2 = False
    send('False', broadcast = True)

@socketio.on('turnOnLed3')
def turnOnLED():
    print("Encender led")
    led3.on()
    led_state3 = True
    send('True', broadcast = True)

@socketio.on('turnOffLed3')
def turnOffLED():
    print("Apagar led")
    led3.off()
    led_state3 = False
    send('False', broadcast = True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)