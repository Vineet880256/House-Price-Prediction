from flask import Flask, request, redirect, render_template, jsonify
import util

app = Flask(__name__)

MODEL_PATH = '../data/banglore_home_prices_model.pickle'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/get_location_names', methods=['GET'])
def get_location_name():
    response = jsonify({
        'location': util.get_location_name(),
        'area_type': util.get_atype_name(),
        'data_columns': util.get_columns_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_home_price', methods=['GET', 'POST'])
def get_home_price():
    sqft = float(request.form['sqft'])
    location = request.form['location']
    area_type = request.form['area_type']
    bhk = int(request.form['bath'])
    bath = int(request.form['bhk'])

    response = jsonify({
        'estimated_price': util.get_estimates_price(location, area_type, sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Program Starting........")
    util.load_stuff()
    app.run(port=5000, debug=True)
