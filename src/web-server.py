from kuas_api import app
from flask_compress import Compress

if __name__ == "__main__":
    Compress(app)
    app.run(host="0.0.0.0", port=5001, debug=True)
