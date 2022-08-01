from flask import Flask, render_template
from flask_socketio import SocketIO, send
from gpiozero import LED

led1 = LED(18)
led_state1 = False

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

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
