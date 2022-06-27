import json
from flask import Flask, jsonify, request
from calc import Calc
from calcB import CalcB
from calcq2 import Calcq2
from calcq2B import Calcq2B

app = Flask(__name__)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response
  
@app.route('/calculate/', methods=['GET', 'POST'])
def calculate():
    logg = request.args.get('logg', default = 2, type = float)
    teff = request.args.get('teff', default = 8500, type = float)
    logz = request.args.get('logz', default = -1.5, type = float)
    
    calc_obj = Calc()
    return calc_obj.calculate(logg, teff, logz)

@app.route('/calculate2/', methods=['GET', 'POST'])
def calculate2():
    logg = request.args.get('logg', default = 2, type = float)
    teff = request.args.get('teff', default = 8500, type = float)
    logz = request.args.get('logz', default = -1.5, type = float)
    
    calc_obj = Calcq2()
    return calc_obj.calculate(logg, teff, logz)

@app.route('/calculate-test/', methods=['GET', 'POST'])
def calculateTest():
    logg = request.args.get('logg', default = 2, type = float)
    teff = request.args.get('teff', default = 8500, type = float)
    logz = request.args.get('logz', default = -1.5, type = float)
    vel = request.args.get('vel', default = 0.5, type = float)
    
    calc_obj = CalcB()
    return calc_obj.calculate(logg, teff, logz, vel)

@app.route('/calculate2-test/', methods=['GET', 'POST'])
def calculate2Test():
    logg = request.args.get('logg', default = 2, type = float)
    teff = request.args.get('teff', default = 8500, type = float)
    logz = request.args.get('logz', default = -1.5, type = float)
    vel = request.args.get('vel', default = 0.5, type = float)
    
    calc_obj = Calcq2B()
    return calc_obj.calculate(logg, teff, logz, vel)

if __name__ == '__main__':
     app.run(host='0.0.0.0')