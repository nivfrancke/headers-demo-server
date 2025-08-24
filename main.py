import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def show_headers(path):
    """Captures all requests and returns the HTTP headers as JSON."""
    headers_dict = {key: value for key, value in request.headers.items()}
    return jsonify(headers_dict)

if __name__ == "__main__":
    # Get the port number from the environment variable PORT
    # Default to 8080 if it's not set (for local testing)
    port = int(os.environ.get("PORT", 8080))
    # Run the app, listening on all available network interfaces
    app.run(debug=True, host='0.0.0.0', port=port)