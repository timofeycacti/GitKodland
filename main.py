from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    with open("./main_page.html") as page:
        return page.read()

app.run(debug=True)