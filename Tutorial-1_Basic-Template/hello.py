from flask import Flask, redirect, url_for

app=Flask(__name__)

@app.route("/")
def home():
    return "<h1> Hello </h1> This is the homepage..."

@app.route("/user/<name>")
def user(name):
    return f"<h1> Hello {name} </h1> Welcome to the flask webpage..."

@app.route("/admin")
def admin():
    return "<h1> Hello Admin! </h1> Welcome to the flask webpage..."

@app.route("/redirect")
def jump():
    #return redirect(url_for("admin"))
    return redirect(url_for("user", name="Arup"))

if __name__=='__main__':
    app.run()