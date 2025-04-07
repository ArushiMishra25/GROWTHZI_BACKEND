def website_schema(data):
    return {
        "user_id": data["user_id"],
        "business_type": data["business_type"],
        "industry": data["industry"],
        "content": data["content"],
        "created_at": data.get("created_at"),
    }
def users_schema(data):
    return {
        "email": data["email"],
        "password": data["password"],
        "created_at": data.get("created_at"),
    }