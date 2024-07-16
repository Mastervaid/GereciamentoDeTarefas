from flask_login import UserMixin
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from main import app
from . import db
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(10), nullable=False)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
