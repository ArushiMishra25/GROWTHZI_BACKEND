import jwt
import datetime
from app.config import Config
from flask import jsonify

def create_jwt_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }
    token = jwt.encode(payload, Config.SECRET_KEY, algorithm="HS256")
    return token



def decode_token(token):
    try:
        decoded = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
        return decoded
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401
