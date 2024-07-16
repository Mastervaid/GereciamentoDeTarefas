from flask import request, jsonify, Blueprint
from models.user import User

users_bp = Blueprint("users",__name__)
@users_bp.route("/register", methods=['POST'])
def register():
    from main import db
    data = request.get_json()
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'O email já existe'}), 400
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'O nome de usuário já existe'}), 400
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'Usuário criado com sucesso'})
