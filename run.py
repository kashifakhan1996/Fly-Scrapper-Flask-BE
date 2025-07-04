import os
from flask_cors import CORS
from app import create_app

app = create_app()
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

@app.route('/')
def home():
    return 'Hello from Flask on Render!'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Fallback to 5000 if PORT is not set
    app.run(host='0.0.0.0', port=port)