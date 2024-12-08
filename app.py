from flask import Flask,redirect,render_template
from forms import input_form

app=Flask(__name__)
app.config["SECRET_KEY"]="secret_key"

@app.route("/")
@app.route("/home")
def home():
    form=input_form()

    return render_template("home.html",form=form,title="Home")


if __name__ =="__main__":
    app.run(debug=True)
