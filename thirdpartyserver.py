from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/numbers/<number_type>', methods=['GET'])
def get_number(number_type):
    if number_type == 'prime':
        number = 17  
    elif number_type == 'fibonacci':
        number = 34  
    elif number_type == 'even':
        number = 16  
    elif number_type == 'random':
        number = 42  
    else:
        return jsonify({"error": "Invalid number type"}), 400

    return jsonify({"number": number})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
