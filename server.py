from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/paintings.html')
def paintings():
    return render_template('paintings.html')

@app.route('/trips.html')
def works():
    return render_template('trips.html')

