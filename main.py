from flask import Flask
from flask_sqlachamy import SQLAlchemy
from flask_bcypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy

app = Flask(__name__)

app.run(debug=True)