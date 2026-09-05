from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Hello, World!'})

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'status': 'success', 'data': []})

if __name__ == '__main__':
    app.run(debug=True)
