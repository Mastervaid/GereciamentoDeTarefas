from flask import Flask
from config import Config
from models import db  
from routes.tasks import tasks_bp

from flask_sqlachamy import SQLAlchemy
from flask_bcypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app) 

app.register_blueprint(tasks_bp)

with app.app_context():
    db.create_all()
    

if __name__ == "__main__":
    app.run(debug=True)
