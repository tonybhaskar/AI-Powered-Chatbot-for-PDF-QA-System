from flask import Flask
from app.routes import routes

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(routes)


@app.route('/')
def home():
    return "hii babe"
if __name__ == "__main__":
    app.run(debug=True)
