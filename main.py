from flask import Flask
from config import Config
from routes import users_bp
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from models import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(users_bp)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
