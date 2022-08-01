from flask import Flask, render_template
from flask_socketio import SocketIO, send
from gpiozero import LED

led = LED(18)
led_state = False

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

socketio = SocketIO(app)

@app.route('/')
def index():
   return render_template('index.html')

@socketio.on('turnOn')
def turnOnLED():
    print("Encender led")
    led.on()
    led_state = True
    send('True', broadcast = True)

@socketio.on('turnOff')
def turnOffLED():
    print("Apagar led")
    led.off()
    led_state = False
    send('False', broadcast = True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
