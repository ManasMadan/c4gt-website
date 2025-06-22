import firebase_admin
from firebase_admin import credentials, storage
import json
import os
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': os.getenv("FIREBASE_BUCKET_NAME")
})
bucket = storage.bucket()

def putItem(path, filedata):
    blob = bucket.blob(path)
    blob.upload_from_string(filedata)
    return True

def getItem(path):
    try:
        blob = bucket.blob(path)
        return blob.download_as_text()
    except Exception:
        return None

def deleteItem(path):
    try:
        blob = bucket.blob(path)
        blob.delete()
        return True
    except Exception:
        return False

def existsItem(path):
    blob = bucket.blob(path)
    return blob.exists()
