import datetime
from flask import jsonify
from bson import ObjectId
from app.utils.ai_generator import generate_website_content
from app.database import mongo
from app.utils.jwt_utils import decode_token

def serialize_website(doc):
    doc["_id"] = str(doc["_id"])
    return doc


def generate_website(req):
    try:
        token = req.headers.get('Authorization')
        if not token or not token.startswith("Bearer "):
            return jsonify({"error": "Authorization token missing or invalid"}), 401

        decoded_token = decode_token(token.split(" ")[1])
        user_email = decoded_token.get("user_id")

        data = req.json
        business_type = data.get("business_type")
        industry = data.get("industry")

        content = generate_website_content(business_type, industry)

        website = {
            "user_id": user_email,
            "business_type": business_type,
            "industry": industry,
            "content": content,
            "created_at": datetime.datetime.utcnow()
        }

        inserted = mongo.db.websites.insert_one(website)
        website["_id"] = str(inserted.inserted_id)

        return jsonify({"message": "Website generated", "website": website}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def get_websites(req):
    try:
        token = req.headers.get('Authorization')
        decoded_token = decode_token(token.split(" ")[1])
        user_email = decoded_token.get("user_id")

        websites = list(mongo.db.websites.find({"user_id": user_email}))
        serialized = [serialize_website(w) for w in websites]

        return jsonify({"websites": serialized}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def update_website(req, website_id):
    try:
        token = req.headers.get('Authorization')
        decoded_token = decode_token(token.split(" ")[1])
        user_email = decoded_token.get("user_id")

        update_data = req.json
        update_fields = {}

        if "business_type" in update_data:
            update_fields["business_type"] = update_data["business_type"]
        if "industry" in update_data:
            update_fields["industry"] = update_data["industry"]
        if "content" in update_data:
            update_fields["content"] = update_data["content"]

        result = mongo.db.websites.update_one(
            {"_id": ObjectId(website_id), "user_id": user_email},
            {"$set": update_fields}
        )

        if result.matched_count == 0:
            return jsonify({"error": "Website not found or unauthorized"}), 404

        return jsonify({"message": "Website updated"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def delete_website(req, website_id):
    try:
        token = req.headers.get('Authorization')
        decoded_token = decode_token(token.split(" ")[1])
        user_email = decoded_token.get("user_id")

        result = mongo.db.websites.delete_one(
            {"_id": ObjectId(website_id), "user_id": user_email}
        )

        if result.deleted_count == 0:
            return jsonify({"error": "Website not found or unauthorized"}), 404

        return jsonify({"message": "Website deleted"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
