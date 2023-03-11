from flask import Flask,render_template

africa = Flask(__name__)


@africa.route("/")
def homepage():
  return render_template("home.html")

if __name__ == "__main__":
  africa.run("0.0.0.0",debug=True)