# cloud/authenticate/firebase_auth.py
import pyrebase
import os
from dotenv import load_dotenv

load_dotenv()

firebase_config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
    "storageBucket": os.getenv("FIREBASE_BUCKET_NAME"),
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

def login_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return {"email": email, "token": user["idToken"]}
    except Exception as e:
        raise Exception(f"Firebase login failed: {str(e)}")


def register_user(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        return {"email": email, "token": user["idToken"]}
    except Exception as e:
        raise Exception(f"Firebase registration failed: {str(e)}")
