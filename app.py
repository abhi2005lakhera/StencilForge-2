from flask import Flask, send_file, request, jsonify
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return send_file('./templates/index.html')

@app.route('/style.css')
def serve_css():
    return send_file('style.css')

UPLOAD_FOLDER = 'pics'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part in the request'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    if file:
        # Save the file in the 'pics' folder
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        return jsonify({'message': 'File uploaded successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 4000))
    app.run(host="0.0.0.0", port=port)
