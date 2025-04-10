from flask import Flask, render_template
from views import register_blueprints_main
from utils import register_blueprints_sub
from db import init_db

AIMA = Flask(__name__)

# API Specification
@AIMA.route('/')
def index():
    return render_template('apispec.html')

# Initialize the database
init_db()

# Register blueprints
register_blueprints_main(AIMA)
register_blueprints_sub(AIMA)

if __name__ == '__main__':
    AIMA.run(host='0.0.0.0', port=5000, debug=True)