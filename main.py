from flask import Flask, request, render_template, jsonify
import util

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/classify_image', methods=['POST'])
def classify_image():
    image_data = request.form['image_data']
    result = util.classify_image(image_data)
    return jsonify(result)

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(debug=True)







