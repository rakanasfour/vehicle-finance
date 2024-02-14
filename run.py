from flask import Flask
from app.data_access.database import init_db
# from app.presentation import routes
from app.presentation.routes import blueprint  # Import the Blueprint


# Initialize the Flask app
app = Flask(__name__)

# Initialize the database
init_db(app)
app.register_blueprint(blueprint)


# Import routes after initializing app to avoid circular imports

if __name__ == '__main__':
    app.run(debug=True)
