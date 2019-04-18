from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Celsius to Kelvin Converter</h1><h2>Type a number at the end of the URL</h2><h3>IE) localhost:5000/0</h3>'

@app.route("/<string:celsius>")
def convert_celsius_to_kelvin(celsius):
    try:
        celsius = float(celsius)
    except:
        return '<h1>Invalid URL</h1>'
    kelvin = round(celsius + 273.15, 2)
    return f'<h1>Convert Celsius to Kelvin</h1><h2>{celsius}°C == {kelvin}K</h2>'

if __name__ == "__main__":
    app.run()