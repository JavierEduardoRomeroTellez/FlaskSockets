from flask import Flask, render_template
from flask_socketio import SocketIO, send
from gpiozero import LED
from gpiozero import Button
import time

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
    if led_state1 == False:
        print("Encender led")
        led1.on()
        led_state1 = True
        socketio.emit('message','True1')
    else:
        print("Apagar led")
        led1.off()
        led_state1 = False
        socketio.emit('message','False1')

button1.when_pressed = buttonPressed1

def buttonPressed2():
    global led_state2
    if led_state2 == False:
        print("Encender led")
        led2.on()
        led_state2 = True
        socketio.emit('message','True2')
    else:
        print("Apagar led")
        led2.off()
        led_state2 = False
        socketio.emit('message','False2')

button2.when_pressed = buttonPressed2

def buttonPressed3():
    global led_state3
    if led_state3 == False:
        print("Encender led")
        led3.on()
        led_state3 = True
        socketio.emit('message','True3')
    else:
        print("Apagar led")
        led3.off()
        led_state3 = False
        socketio.emit('message','False3')

button3.when_pressed = buttonPressed3

@app.route('/')
def index():
   return render_template('index.html')

@socketio.on('turnOnLed1')
def turnOnLED():
    global led_state1
    print("Encender led")
    led1.on()
    led_state1 = True
    send('True1', broadcast = True)

@socketio.on('turnOffLed1')
def turnOffLED():
    global led_state1
    print("Apagar led")
    led1.off()
    led_state1 = False
    send('False1', broadcast = True)

@socketio.on('turnOnLed2')
def turnOnLED():
    global led_state2
    print("Encender led")
    led2.on()
    led_state2 = True
    send('True2', broadcast = True)

@socketio.on('turnOffLed2')
def turnOffLED():
    global led_state2
    print("Apagar led")
    led2.off()
    led_state2 = False
    send('False2', broadcast = True)

@socketio.on('turnOnLed3')
def turnOnLED():
    global led_state3
    print("Encender led")
    led3.on()
    led_state3 = True
    send('True3', broadcast = True)

@socketio.on('turnOffLed3')
def turnOffLED():
    global led_state3
    print("Apagar led")
    led3.off()
    led_state3 = False
    send('False3', broadcast = True)

@socketio.on('message')
def handleMessage(msg):
    global led_state1
    global led_state2
    global led_state3
    if msg == 'parpadear':
        send('OK', broadcast = True)
        led1.off()
        led2.off()
        led3.off()
        time.sleep(1)
        for x in range(5):
            led1.on()
            time.sleep(.1)
            led1.off()
            led2.on()
            time.sleep(.1)
            led2.off()
            led3.on()
            time.sleep(.1)
            led3.off()

        if led_state1:
            led1.on()
        if led_state2:
            led2.on()
        if led_state3:
            led3.on()


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
    print(led_state1)
