import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials, db
import os


load_dotenv()
# Use service account JSON (fix the file path issue)
cred = credentials.Certificate('ServiceAccountKey.json')

# Set database URL properly
database_url = os.environ.get("FIREBASE_DATABASE_URL")

# If environment variable is missing, use fallback
if not database_url:
    database_url = "https://kidocodequizz-7d53d-default-rtdb.asia-southeast1.firebasedatabase.app/"

# Initialize Firebase
try:
    firebase_admin.initialize_app(cred, {"databaseURL": database_url})
except ValueError as e:
    print(f"Firebase initialization failed: {e}")

# Get database reference
db_ref = db.reference()

# Function to test connection
def test_firebase_connection():
    try:
        db_ref.child("test_data").set({"message": "Firebase connection successful!"})
        data = db_ref.child("test_data").get()
        return data["message"]
    except Exception as e:
        return str(e)
