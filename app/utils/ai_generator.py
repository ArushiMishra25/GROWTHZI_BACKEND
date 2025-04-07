#import openai
from app.config import Config
from google import genai

#openai.api_key = Config.OPENAI_API_KEY

def generate_website_content(business_type, industry):
    client=genai.Client(api_key=Config.OPENAI_API_KEY)
    prompt = f"Act like a top-tier Professional content writer . Write professional, concise, and compelling content for business type {business_type} and {industry} industry. I just want the content nothing else should be there in your response"
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    if(response.text == None):
        raise Exception("No content generated")
    return response.text;
