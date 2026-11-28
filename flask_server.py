from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def handle_post():
    # Automatically parses incoming JSON payload
    data = request.get_json(silent=True) or request.form.to_dict()
    print("Received:", data)
    
    return jsonify({"status": "success", "you_sent": data}), 200

if __name__ == '__main__':
    app.run(host='localhost', port=8000)