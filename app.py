from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/my_webhook", methods=["POST"])
def jotform_webhook():
    
    # When files are involved, the data is in 'request.form'
    print("--- NEW SUBMISSION (FORM DATA) RECEIVED ---")
    
    # 'request.form' is a special dictionary.
    # We can convert it to a regular dictionary to print it.
    data = request.form.to_dict()
    
    print(data)
    
    # Your file upload will just be a URL in this dictionary
    # You'll have to look at the printout to find the real field name
    # Example: print("Link to file:", data.get('your_file_field_name'))

    return "Webhook Received!", 200

if __name__ == '__main__':
    app.run(debug=True)
