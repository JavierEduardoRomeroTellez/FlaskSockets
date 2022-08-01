from flask import Flask, render_template
from flask_socketio import SocketIO, send
from gpiozero import LED
from gpiozero import Button

led1 = LED(18)
led_state1 = False
led2 = LED(23)
led_state2 = False
led3 = LED(24)
led_state3 = False

button1 = Button(22)
button2 = Button(27)
button3 = Button(17)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

socketio = SocketIO(app)

def buttonPressed1():
    global led_state1
    if led_state1:
        print("Encender led")
        socketio.emit('Button1On')
    else:
        print("Apagar led")
        socketio.emit('Button1Off')

button1.when_pressed = buttonPressed1

@app.route('/')
def index():
   return render_template('index.html')

@socketio.on('turnOnLed1')
def turnOnLED():
    print("Encender led")
    led1.on()
    led_state1 = True
    send('True1', broadcast = True)

@socketio.on('turnOffLed1')
def turnOffLED():
    print("Apagar led")
    led1.off()
    led_state1 = False
    send('False1', broadcast = True)

@socketio.on('turnOnLed2')
def turnOnLED():
    print("Encender led")
    led2.on()
    led_state2 = True
    send('True2', broadcast = True)

@socketio.on('turnOffLed2')
def turnOffLED():
    print("Apagar led")
    led2.off()
    led_state2 = False
    send('False2', broadcast = True)

@socketio.on('turnOnLed3')
def turnOnLED():
    print("Encender led")
    led3.on()
    led_state3 = True
    send('True3', broadcast = True)

@socketio.on('turnOffLed3')
def turnOffLED():
    print("Apagar led")
    led3.off()
    led_state3 = False
    send('False3', broadcast = True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
