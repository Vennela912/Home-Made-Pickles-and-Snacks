from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        return render_template("welcome.html", username=username)
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        if password != confirm_password:
            return "Passwords do not match!"
        return f"Account created for {username}!"
    return render_template("register.html")

@app.route("/veg-pickles")
def veg_pickles():
    return render_template("veg_pickles.html")

@app.route("/nonveg-pickles")
def nonveg_pickles():
    return render_template("nonveg_pickles.html")

@app.route("/snacks")
def snacks():
    return render_template("snacks.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
