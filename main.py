from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('index.html')

@app.route('/lapa1')
def lapa1():
  return render_template('lapa1.html')

@app.route('/lapa2')
def lapa2():
  return render_template('lapa2.html')

@app.route('/lapa3')
def lapa3():
  return render_template('lapa3.html')








app.run(host='0.0.0.0', port=8020)