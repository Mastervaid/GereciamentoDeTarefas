from flask import Flask
<<<<<<< Updated upstream
=======
from config import Config
from models import db  # Importa db do models
from routes import tasks_bp
>>>>>>> Stashed changes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)  # Inicializa o db com o app

app.register_blueprint(tasks_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
