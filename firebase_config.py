import firebase_admin
from firebase_admin import credentials, storage


cred = credentials.Certificate("serviceAccountKey.json")


firebase_admin.initialize_app(cred, {
    'storageBucket': 'flask-app-project-faf0c.appspot.com'

})


bucket = storage.bucket()
