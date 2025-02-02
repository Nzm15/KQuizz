import firebase_admin
from firebase_admin import credentials, db
import os

cred = credentials.ApplicationDefault()

try:
    firebase_admin.initialize_app(cred, {
        'databaseURL': os.environ.get("https://console.firebase.google.com/u/0/project/kidocodequizz-7d53d/overview") # Make sure to set FIREBASE_DATABASE_URL
    })
except ValueError:
    pass

db_ref = db.reference()

def test_firebase_connection():
    try:
        db_ref.child('test_data').set({'message': 'Firebase connection successful!'})
        data = db_ref.child('test_data').get()
        return data['message']
    except Exception as e:
        return str(e)

__all__ = ["db_ref", "test_firebase_connection"]