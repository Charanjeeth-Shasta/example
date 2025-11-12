from flask import Flask, render_template
app=Flask()

@app.route("/index.html")
def index():
    render_template("index.html")

@app.route("/education.html")
def education():
    render_template("education.html")

@app.route("/experience.html")
def experience():
    render_template("experience.html")

@app.route("/projects.html")
def projects():
    render_template("projects.html")

@app.route("/writetome.html")
def writetome():
    render_template("writetome.html")


if __name__=="__main__":
    app.run(debug=True)