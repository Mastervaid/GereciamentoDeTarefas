from flask import request, jsonify, Blueprint
from models.user import User
from flask_login import login_user

users_bp = Blueprint("users",__name__)
@users_bp.route("/register", methods=['POST'])
def register():
    from main import db
    data = request.get_json()
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'O email já existe'}), 400
    if User.query.filter_by(name=data['name']).first():
        return jsonify({'message': 'O nome de usuário já existe'}), 400
    user = User(name=data['name'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'Usuário criado com sucesso'})

@users_bp.route("/login", methods=['POST'])
def login():
    from main import db
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if user and user.check_password(data['password']):
        login_user(user)
        return jsonify({'message': 'Login bem-sucedido'})
    else:
        return jsonify({'message': 'Credenciais inválidas'}), 401
