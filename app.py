from flask import Flask, render_template, request,redirect
import paho.mqtt.client as mqtt
import time

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    #print(request.method)
    broker ="tailor.cloudmqtt.com"
    port =  14596 
    username = "hbhxycja"
    password = "0Q8tFD0zRE4V"
    client = mqtt.Client()
    result="Status:"
    if request.method == 'POST':
        if request.form.get('OFF') == 'OFF':
            result += off(broker,port,username,password,client)
            #return redirect(url_for('index'))

        elif  request.form.get('ON') == 'ON':
            #print("ON")
	        result+=on(broker,port,username,password,client)
            #return redirect(url_for('index'))
        else:
                # pass # unknown
            return render_template("index.html")
    elif request.method == 'GET':
            # return render_template("index.html")
        print("No Post Back Call")
    return render_template("index.html",result=result)


def on(broker,port,username,password,client):
    client.username_pw_set(username,password)
    client.connect(broker,port)
    ret = client.publish("Status","Light glowing")
    return "Led Turned On"

def off(broker,port,username,password,client):
    client.username_pw_set(username,password)
    client.connect(broker,port,60)
    ret = client.publish("Status","Light stop glowing")
    return "Led Turned Off"

if __name__ == '__main__':
    app.run()