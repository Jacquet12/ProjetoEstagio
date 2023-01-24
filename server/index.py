import math
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/calculate',  methods=['POST', 'GET'])
@cross_origin()
def calculate():
    body = request.get_json()
    a = body.get('a')
    b = body.get('b')
    c = body.get('c')

    a = int(a) if a != '' else -1
    b = int(b) if b != '' else -1
    c = int(c) if c != '' else -1
    resultado = {
        "value": -1,
        "side": "",
        "isSuccess": False
    }

    if a >= 0 and b >= 0:
        c = (a*a) + (b*b)
        if c > 0:
            resultado["value"] = math.sqrt(c)
            resultado["isSuccess"] = True
            resultado["side"] = "Hypotenusa"
    elif a >= 0 and c >= 0:
            b = (c*c) - (a*a)
            if b > 0:
                resultado["value"] = math.sqrt(b)
                resultado["isSuccess"] = True
                resultado["side"] = "Lado b"
    elif b >= 0 and c >= 0:
            a = (c*c) - (b*b)
            if a > 0:
                resultado["value"]= math.sqrt(a)
                resultado["isSuccess"] = True
                resultado["side"] = "Lado a"

    resultado["value"] = round(resultado["value"], 2) 
    return jsonify(resultado)        

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


