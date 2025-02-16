from flask import Flask, request, jsonify
import threading
import time
import requests

app = Flask(__name__)

# Fonction de conversion des secondes en HH:MM:SS
def convertir_secondes(secondes):
    heures = secondes // 3600
    minutes = (secondes % 3600) // 60
    secondes = secondes % 60
    return f"{heures:02}:{minutes:02}:{secondes:02}"

# Route API pour convertir les secondes
@app.route('/convert', methods=['GET'])
def convert():
    try:
        secondes = int(request.args.get('seconds', 0))
        formatted_time = convertir_secondes(secondes)
        return jsonify({"formatted_time": formatted_time})
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

# Keep Alive pour empêcher Render de couper l’API
def keep_alive():
    url = "https://api-botghost.onrender.com/convert?seconds=1"  # Remplace par ton URL Render
    while True:
        try:
            requests.get(url)
            print("Keep Alive Ping !")
        except Exception as e:
            print(f"Erreur Keep Alive : {e}")
        time.sleep(300)  # Ping toutes les 5 minutes

# Démarrer Keep Alive en arrière-plan
thread = threading.Thread(target=keep_alive, daemon=True)
thread.start()

# Lancer le serveur Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
