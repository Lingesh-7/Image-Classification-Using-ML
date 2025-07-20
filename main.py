from flask import Flask, request, render_template, jsonify
import util

app = Flask(__name__, template_folder='templates')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB upload limit

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    error_message = None

    if request.method == 'POST':
        try:
            image_data = request.form['image_data']
            result = util.classify_image(image_data)

            if not result:
                error_message = "❌ No face with 2 visible eyes detected. Please upload a clearer image."
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"

    return render_template("index.html", result=result, error_message=error_message)


if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(debug=True)
