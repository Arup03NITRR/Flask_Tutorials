from flask import Flask, render_template, url_for
from admin.admin import admin_obj


app = Flask(__name__)
app.register_blueprint(blueprint = admin_obj, url_prefix = "/admin")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
def test():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug = True)