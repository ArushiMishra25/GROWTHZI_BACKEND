from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.database import get_users_collection
from app.utils.jwt_utils import create_jwt_token
import datetime



# Signup Logic
def signup(request):
    users_collection= get_users_collection()
    print("Users collection:", users_collection)
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    existing_user = users_collection.find_one({"email": email})
    if existing_user:
        return jsonify({"error": "User already exists"}), 409

    hashed_password = generate_password_hash(password)
    users_collection.insert_one({
        "email": email,
        "password": hashed_password,
        "createdAt": datetime.datetime.utcnow()
    })

    token = create_jwt_token(email)
    return jsonify({"message": "Signup successful", "token": token}), 201


# Login Logic
def login(request):
    users_collection= get_users_collection()
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = users_collection.find_one({"email": email})
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_jwt_token(email)
    return jsonify({"message": "Login successful", "token": token}), 200
