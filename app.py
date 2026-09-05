from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return {'status': 'success', 'message': 'Webhook is ready'}, 200
    elif request.method == 'POST':
        return {'status': 'success', 'message': 'Data received'}, 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
