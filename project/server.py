from flask import Flask, request, jsonify,render_template,Response
import json
import util

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("server.html")

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict', methods=['GET','POST'])
def predict_home_price():
    location = request.form.get('location')
    total_sqft = float(request.form.get('area'))
    bed=int(request.form.get('bedroom'))
    resale=int(request.form.get('resale'))
    indoor=int(request.form.get('indoor'))
    intercom=int(request.form.get('intercom'))
    sports=int(request.form.get('sports'))
    power=int(request.form.get('power'))
    gas=int(request.form.get('gas'))
    lift=int(request.form.get('lift'))
    vastu=int(request.form.get('vaastu'))
    response= util.get_estimated_price(location,total_sqft,bed,resale,indoor,intercom,sports,power,gas,lift,vastu)
    return render_template('server.html',pred='Estimated House Price is\n {}'.format(response)+'  INR')


   # response = jsonify({
     #   'estimated_price': util.get_estimated_price(location,total_sqft,bed,resale,indoor,intercom,sports,power,gas,lift,vastu)
    #})
    #response.headers.add('Access-Control-Allow-Origin', '*')'''
  




if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)