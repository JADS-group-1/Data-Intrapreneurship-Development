from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("form_page.html")

@app.route('/results')
def results():
    return render_template("result_page.html")

@app.route('/logo')
def logo():
    return send_file("logo.jpg", mimetype="image/jpg")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)