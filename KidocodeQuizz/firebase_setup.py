import firebase_admin
from firebase_admin import credentials, db
import os

# Load credentials
cred = credentials.Certificate("path/to/serviceAccountKey.json")

try:
    firebase_admin.initialize_app(cred, {
        'databaseURL': os.environ.get("FIREBASE_DATABASE_URL")  # Ensure this variable is set
    })
except firebase_admin.exceptions.FirebaseError as e:
    print("Firebase initialization error:", e)

# Database reference
db_ref = db.reference()

def test_firebase_connection():
    try:
        db_ref.child('test_data').set({'message': 'Firebase connection successful!'})
        data = db_ref.child('test_data').get()
        return data.get('message', 'No data found')
    except Exception as e:
        return str(e)

__all__ = ["db_ref", "test_firebase_connection"]
