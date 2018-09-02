from flask_wtf import FlaskForm, Form
from wtforms.widgets import TextInput, HiddenInput
from wtforms import StringField, SelectField, RadioField, BooleanField
from gallery.custom_widgets import TestInput

class DemoForm(FlaskForm):
    demo_str = StringField(label='Standard string field')
    demo_select = SelectField(label='Standard dropdown selector',
                              choices=[('Alt1', '1'), ('Alt2', '2'), ('Alt3', '3')])
    demo_radio = RadioField(label='Standard radio buttons selector',
                            choices=[('Alt1', 'Select 1'), ('Alt2', 'Select 2'), ('Alt3', 'Select 3')])
    demo_boolean = BooleanField(label="Standard Yes/No (boolean) field")

