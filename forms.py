import pandas as pd
from flask_wtf import FlaskForm
from wtforms import SelectField,FloatField,IntegerField,SubmitField
from wtforms.validators import DataRequired

#importing the data
data=pd.read_csv("Data/Mobile Price Prediction Datatset.xls")

class input_form(FlaskForm):
    RAM=SelectField(label="RAM"
                    ,choices=data.RAM.unique().tolist(),
                    validators=[DataRequired()])
    
    ROM=SelectField(label="ROM"
                    ,choices=data.ROM.unique().tolist(),
                    validators=[DataRequired()])
    
    Display=FloatField(label="Display size",
                    validators=[DataRequired()])
    
    Primary_Cam=SelectField(label="Primary Camera",
                        choices=data.Primary_Cam.unique().tolist(),    
                    validators=[DataRequired()])
    
    Selfi_Cam=SelectField(label="Primary Camera",
                          choices=data.Selfi_Cam.unique().tolist(),
                    validators=[DataRequired()])
    
    Battery=IntegerField(label="Battery Size",
                    validators=[DataRequired()])
    
    Predict=SubmitField("Predict")