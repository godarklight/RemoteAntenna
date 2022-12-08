from flask import Flask, abort, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    f = open("antenna.txt", "r")
    antenna = f.readlines()[0]
    f.close()
    return render_template('index.html', antenna=antenna)

@app.route("/switch/<antenna>")
def switch(antenna):
    f = open("antenna.txt", "w")
    f.write(antenna)
    f.close()
    return render_template('switch.html', antenna=antenna)
