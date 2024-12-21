from flask import Flask, render_template, url_for, Blueprint

admin_obj = Blueprint("admin", __name__, static_folder="static", template_folder="templates")

@admin_obj.route("/")
def index2():
    return render_template("index2.html")

@admin_obj.route("/test")
def test2():
    return render_template("test2.html")