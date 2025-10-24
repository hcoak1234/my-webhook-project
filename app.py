from flask import Flask, request
from flask_cors import CORS  # <-- 1. ADD THIS IMPORT

app = Flask(__name__)
CORS(app)  # <-- 2. ADD THIS LINE to allow all origins

@app.route("/my_webhook", methods=["POST"])
def jotform_webhook():
    # ... (rest of your code is the same)
    print(request.json)
    print("--- NEW SUBMISSION RECEIVED ---")
    return "Webhook Received!", 200

if __name__ == '__main__':
    app.run(debug=True)