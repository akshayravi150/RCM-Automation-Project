from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for("login_page"))


@app.route("/login")
def login_page():
    return render_template("login.html")


@app.route("/charge-entry", methods=["GET", "POST"])
def charge_entry():
    if request.method == "POST":
        return render_template("charge_entry.html", success=True)

    return render_template("charge_entry.html", success=False)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
