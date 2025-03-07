from flask import Flask, render_template, request, jsonify
from firebase_setup import db_ref, test_firebase_connection  # Correct import

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    # ... (get answer from request.form)
    # ... (write answer to Firebase using db_ref)
    return jsonify({'message': 'Answer submitted!'})

@app.route('/test_firebase')
def test_firebase():
    message = test_firebase_connection()
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(debug=True)