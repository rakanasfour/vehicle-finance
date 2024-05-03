from flask import Flask
from app.data_access.database import init_db
# from app.presentation import routes
from app.presentation.routes import blueprint  # Import the Blueprint
from flask_cors import CORS


# Initialize the Flask app
app = Flask(__name__)
CORS(app)
# Initialize the database
init_db(app)
app.register_blueprint(blueprint)


# Import routes after initializing app to avoid circular imports

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
