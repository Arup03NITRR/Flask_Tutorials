from flask import Flask, redirect, render_template, request, url_for, session, flash
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
        flash("Login Successful...")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("You are already logged in...", "info")
            return redirect(url_for("user"))
        return render_template('login.html')


@app.route('/user')
def user():
    if "user" in session:
        user=session["user"]
        return render_template("user.html", usr=user)
    else:
        flash("You are not logged in...", "info")
        return redirect(url_for("login"))

@app.route('/logout')
def logout():
    flash("You have been logged out...", "info")
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__=='__main__':
    app.run(debug=True)