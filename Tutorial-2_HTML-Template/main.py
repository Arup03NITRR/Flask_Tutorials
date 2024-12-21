from flask import Flask, render_template

app=Flask("__name__")

@app.route("/route1")
def fn1():
    return render_template("page1.html")

@app.route("/route2/<name> <age>")
def fn2(name, age):
    return render_template("page2.html", name=name, age=age)

@app.route("/route3")
def fn3():
    return render_template("page3.html", list_data=['Arup', 'NIT Raipur', 'Siliguri'])

if __name__=="__main__":
    app.run()