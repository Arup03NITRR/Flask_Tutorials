from flask import Flask, redirect, render_template, request, url_for, session
from datetime import timedelta

app=Flask(__name__)
app.secret_key = "Hello"
#To store the session for 5 min
app.permanent_session_lifetime=timedelta(minutes=5)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method=="POST":
        #To store the session for 5 min
        session.permanent=True
        user=request.form["nm"]
        session["user"]=user
        return redirect(url_for("user"))
    else:
        return render_template('login.html')


@app.route('/user')
def user():
    if "user" in session:
        user=session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__=='__main__':
    app.run(debug=True)