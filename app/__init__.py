from flask import Flask
from .views.ocr import ocr_bp

app = Flask(__name__)
app.register_blueprint(ocr_bp)


if __name__ == "__main__":
    app.run(debug=True)
