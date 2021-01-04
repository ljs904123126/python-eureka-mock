from flask import Flask

app = Flask("test")


@app.route("/")
def hello_world():
    return "HelloWorld"


app.run("127.0.0.1", 8081)
