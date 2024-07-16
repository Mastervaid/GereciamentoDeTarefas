from flask import Flask
from config import Config
from routes import users_bp
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from models import db
from models.user import User

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar extensões com a aplicação
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id): 
    return User.query.get(int(user_id))

# Registrar blueprints
app.register_blueprint(users_bp)

# Criar o banco de dados e tabelas
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
