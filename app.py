from flask import Flask, request, render_template, Markup

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Celsius to Kelvin Converter: Type a number after the last / in the URL</h1>'

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