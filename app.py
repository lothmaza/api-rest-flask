from flask import Flask, jsonify, request

app = Flask(__name__)

def kmh_to_ms(kmh):
    calculo = (kmh / 3600) * 1000
    return calculo

def ms_to_kmh(ms):
    calculo = (ms * 3600) / 1000
    return calculo

@app.route('/convert', methods = ['POST'])
def convert_velocity():
    data = request.get_json()
    input_temp=data.get('velocity')
    if data['type'] == 'km/h':
        result = kmh_to_ms(input_temp)
        output_unit = 'm/s'
    if data['type'] == 'm/s':
        result = ms_to_kmh(input_temp)
        output_unit = 'km/h'
    
    return jsonify({"velocity": result, "unit": output_unit})


if __name__ == '__main__':
    app.run(debug=False)