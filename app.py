from flask import Flask,redirect,render_template
from forms import input_form
import joblib
import pandas as pd

app=Flask(__name__)
app.config["SECRET_KEY"]="secret_key"

model = joblib.load("best_decision_tree_model.joblib")

@app.route("/",methods=["GET","POST"])
@app.route("/home", methods=["GET","POST"])
def home():
    form=input_form()
    message=""
    if form.validate_on_submit():
        X_new=pd.DataFrame(dict(

            RAM=[form.RAM.data],
            ROM=[form.ROM.data],
            Mobile_Size=[form.Display.data],
            Primary_Cam=[form.Primary_Cam.data],
            Selfi_Cam=[form.Selfi_Cam.data],
            Battery_Power=[form.Battery.data]

        ))
        try:
            predicton = model.predict(X_new)[0]
            print("Prediction result:", predicton)
            message = f"The price is {predicton} INR"
        except Exception as e:
            print("Error during prediction:", e)
            message = "Prediction failed. Please try again."

    else:
        message="Please provide valid outputs"
    return render_template("home.html",form=form,title="Home",output=message)

if __name__ =="__main__":
    app.run(debug=True)
