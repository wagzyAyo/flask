from flask import Flask, render_template
app = Flask(__name__)

data = [
    {
        "author": "James  Bond",
        "title": "Blog Post1",
        "content": "New blog post on 999 street 2022",
        "date": "20/8/2020"
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post1",
        "content": "New blog post on 999 street 2022",
        "date": "20/8/2020"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=data)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
