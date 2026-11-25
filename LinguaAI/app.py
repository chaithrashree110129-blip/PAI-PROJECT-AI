
from flask import Flask, render_template

# Initialize Flask application
app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("home.html")

# Login and signup page
@app.route("/account")
def account():
    return render_template("account.html")

# Dashboard page
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# Start the website
if __name__ == "__main__":
    app.run(debug=True)

