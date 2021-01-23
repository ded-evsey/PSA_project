from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import os
import json
import zipfile
app = Flask(__name__)
CORS(app)

def unzip_data():
    os.system('kaggle competitions download -c airbus-ship-detection')
    zip_files = zipfile.ZipFile('airbus-ship-detection.zip','r')
    zip_files.extractall('input')
    zip_files.close()


@app.route('/api/test_get', methods=['GET'])
@cross_origin()
def test_get():
    return jsonify({'message': 'Hello, I am your backend'})


@app.route('/api/test_post', methods=['POST'])
@cross_origin()
def test_post():
    if request.method == "POST":
        response = request.get_json()
        result = "Hello " + response['user_name']
        return result


if __name__ == "__main__":
    unzip_data()
    app.run(host='0.0.0.0')
