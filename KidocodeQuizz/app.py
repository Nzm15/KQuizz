from flask import Flask, render_template, request, jsonify
from KidocodeQuizz.firebase_setup import db_ref, test_firebase_connection  # Adjusted import

app = Flask(__name__, template_folder='KidocodeQuizz/templates')  # Set correct templates path

@app.route('/header')
def header():
    return render_template('header.html')  # Serves header.html separately

@app.route('/')
def index():
    return render_template('index.html')  # Ensure "KidocodeQuizz/templates/index.html" exists

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    try:
        answer = request.form.get('answer')  # Get the submitted answer

        if not answer:
            return jsonify({'error': 'No answer provided!'}), 400

        db_ref.push({'answer': answer})  # Save answer to Firebase
        return jsonify({'message': 'Answer submitted successfully!'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Catch unexpected errors

@app.route('/test_firebase')
def test_firebase():
    try:
        message = test_firebase_connection()  # Check Firebase connection
        return jsonify({'message': message})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
