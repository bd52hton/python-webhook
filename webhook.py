from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.json # Get the JSON payload sent to the webhook
        print(f"Received data: {data}")

        # Perform any processing you need here
        response = {
            "status": "success",
            "message": "Webhook received successfully",
            "received_data": data
        }
        
        return jsonify(response), 200
    else:
        return jsonify({"error": "Invalid request method"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)