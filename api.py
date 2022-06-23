import json
from flask import Flask, jsonify, request
from calc import Calc

app = Flask(__name__)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response
  
@app.route('/calculate/', methods=['GET', 'POST'])
def welcome():
    logg = request.args.get('logg', default = 2, type = float)
    teff = request.args.get('teff', default = 8500, type = float)
    logz = request.args.get('logz', default = -1.5, type = float)
    
    calc_obj = Calc()
    return calc_obj.calculate(logg, teff, logz)

if __name__ == '__main__':
     app.run(host='0.0.0.0')