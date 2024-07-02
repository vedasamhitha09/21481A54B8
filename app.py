from flask import Flask, jsonify
import requests
import threading
import time

app = Flask(__name__)

WINDOW_SIZE = 10
NUMBER_TYPES = {'p': 'prime', 'f': 'fibonacci', 'e': 'even', 'r': 'random'}
numbers_window = []
lock = threading.Lock()

def fetch_number(number_type):
    try:
        response = requests.get(f'http://localhost:5000/numbers/{number_type}', timeout=0.5)
        if response.status_code == 200:
            return response.json()['number']
    except (requests.RequestException, KeyError):
        return None

def add_number(number):
    global numbers_window
    with lock:
        if number not in numbers_window:
            if len(numbers_window) >= WINDOW_SIZE:
                numbers_window.pop(0)
            numbers_window.append(number)

@app.route('/numbers/<numberid>', methods=['GET'])
def get_numbers(numberid):
    if numberid not in NUMBER_TYPES:
        return jsonify({"error": "Invalid number type"}), 400

    prev_state = numbers_window.copy()
    new_number = fetch_number(NUMBER_TYPES[numberid])

    if new_number is not None:
        add_number(new_number)
    curr_state = numbers_window.copy()

    avg = sum(curr_state) / len(curr_state) if curr_state else 0.0
    response = {
        "windowPrevState": prev_state,
        "windowCurrState": curr_state,
        "numbers": [new_number] if new_number is not None else [],
        "avg": round(avg, 2)
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9876)
