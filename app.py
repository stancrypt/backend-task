from flask import Flask, request, jsonify, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('hello'))

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Guest')
    client_ip = request.remote_addr

    # Get location based on IP address
    geo_response = requests.get(f"https://ipapi.co/{client_ip}/json/")
    if geo_response.status_code == 200:
        geo_data = geo_response.json()
        city = geo_data.get('city', 'Unknown')
    else:
        city = 'Unknown'

    # For the sake of example, let's hardcode the temperature
    temperature = 11  # in degrees Celsius

    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}"
    response = {
        "client_ip": client_ip,
        "location": city,
        "greeting": greeting
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)