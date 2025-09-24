from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Predefined credentials
USERNAME = "admin"
PASSWORD = "1234"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == USERNAME and password == PASSWORD:
            flash("Login successful!", "success")
            return redirect(url_for("welcome"))
        else:
            flash("Invalid username or password!", "danger")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

if __name__ == "__main__":
    app.run(debug=True)
