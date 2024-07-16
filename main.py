from flask import Flask
from config import Config
from models import db  
from routes.tasks import tasks_bp


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app) 

app.register_blueprint(tasks_bp)

with app.app_context():
    db.create_all()
    

if __name__ == "__main__":
    app.run(debug=True)
