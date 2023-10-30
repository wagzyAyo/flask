from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Hello word!</h1>"

@app.route("/about")
def about():
    return "<h2>This is about page</h2>"

if __name__ == "__main__":
    app.run(debug=True)