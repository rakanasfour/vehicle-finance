from flask import Flask
from app.data_access.database import init_db
from app import app
# Initialize the Flask app
app = Flask(__name__)

# Initialize the database
init_db(app)

# Import routes after initializing app to avoid circular imports
from app.presentation import routes

if __name__ == '__main__':
    app.run(debug=True)
