# 🧠 GROWTHZI_BACKEND

This is the backend for the **AI Website Builder** project—powered by Flask, MongoDB, JWT authentication, and OpenAI API. Users can register, log in, generate websites using AI, and preview/manage their content securely.

---

## 🚀 Tech Stack

- **Backend Framework:** Flask (Python)
- **Database:** MongoDB (via Atlas)
- **Auth:** JWT
- **AI:** GOOGLE GEMINI API
- **Deployment:** Railway

---

## 📁 Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── auth_routes.py
│   │   ├── website_routes.py
│   │   └── other_routes.py
│   ├── models/
│   └── utils/
├── requirements.txt
├── run.py
└── README.md
```

---

## 🛠️ How to Run Locally

1. **Clone the repo**

```bash
git clone https://github.com/your-username/ai-website-builder-backend.git
cd ai-website-builder-backend
```

2. **Set up virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # for Linux/macOS
venv\Scripts\activate     # for Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create a `.env` file**

```
MONGO_URI=your_mongodb_uri
JWT_SECRET=your_jwt_secret
OPENAI_API_KEY=your_openai_api_key
```

5. **Run the app**

```bash
python run.py
```

App will run on `http://localhost:5000`

---

## 🌐 API Routes

| Route                   | Method | Description                   |
|------------------------   |--------|-------------------------------|
| `/api/auth/signup`        | POST   | Register a new user           |
| `/api/auth/login`         | POST   | Log in and get JWT token      |
| `/api/websites/generate`  | POST   | Create website via AI         |
| `/api/websites/`          | GET    | Get website content           |
| `/api/websites/<id>`      | PUT    | Update website content        |
| `/api/websites/<id>`      | DELETE | Delete a website              |

---

## ☁️ Deployment on Railway

1. Push your code to GitHub.
2. Go to [Railway](https://railway.app/), click “New Project” → “Deploy from GitHub”.
3. Add your environment variables:
   - `MONGO_URI`
   - `JWT_SECRET`
   - `OPENAI_API_KEY`
4. Set the **start command**:
   ```bash
   python run.py
   ```
5. Railway will build and deploy automatically.
6. Copy your backend URL (e.g., `https://your-backend.up.railway.app`) and you're ready to integrate with the frontend!

---


---
