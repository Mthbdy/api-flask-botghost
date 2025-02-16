from flask import Flask, request, jsonify
import threading
import time
import requests

app = Flask(__name__)


def convertir_secondes(secondes):
    heures = secondes // 3600
    minutes = (secondes % 3600) // 60
    secondes = secondes % 60
    return f"{heures:02}:{minutes:02}:{secondes:02}"


@app.route('/convert', methods=['GET'])
def convert():
    try:
        secondes = int(request.args.get('seconds', 0))
        formatted_time = convertir_secondes(secondes)
        return jsonify({"formatted_time": formatted_time})
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)