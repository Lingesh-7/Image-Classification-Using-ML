import os
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import util

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB file size limit

util.load_saved_artifacts()

@app.route('/')
def index():
    return render_template('index.html', error_message=None)

@app.route('/classify', methods=['POST'])
def classify():
    error_message = None
    try:
        if 'image' not in request.files:
            error_message = "No image part in the request."
            return render_template('index.html', error_message=error_message)

        file = request.files['image']
        if file.filename == '':
            error_message = "No file selected."
            return render_template('index.html', error_message=error_message)

        if file:
            filename = secure_filename(file.filename)
            image_bytes = file.read()

            try:
                result = util.classify_image(image_bytes)
                return render_template('index.html', result=result[0], error_message=None)
            except ValueError as ve:
                error_message = str(ve)
            except Exception as e:
                error_message = f"Unexpected error: {str(e)}"

    except Exception as e:
        error_message = f"Unexpected error: {str(e)}"

    return render_template('index.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
