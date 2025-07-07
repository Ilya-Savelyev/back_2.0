from flask import Blueprint, request, jsonify, Flask

from app import db
from app.models import Postcard

app = Flask(__name__)

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return "Сервер работает!"

# Создание/отправка открытки
@bp.route('/postcards', methods=['POST'])
def create_postcard():
    data = request.json
    try:
        new_postcard = Postcard(
            sender_name=data['sender_name'],
            recipient_name=data['recipient_name'],
            message=data['message'],
            image_url=data.get('image_url')
        )
        db.session.add(new_postcard)
        db.session.commit()
        return jsonify({'status': 'success', 'postcard': new_postcard.to_dict()}), 201
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

# Получение всех открыток
@bp.route('/postcards', methods=['GET'])
def get_postcards():
    postcards = Postcard.query.all()
    return jsonify([p.to_dict() for p in postcards])

# Получение открытки по ID
@bp.route('/postcards/<int:postcard_id>', methods=['GET'])
def get_postcard(postcard_id):
    postcard = Postcard.query.get_or_404(postcard_id)
    return jsonify(postcard.to_dict())