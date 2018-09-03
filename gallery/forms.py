from flask_wtf import FlaskForm, Form
from wtforms.widgets import TextInput, HiddenInput
from wtforms import StringField, SelectField, RadioField, BooleanField, DateField, DateTimeField, TextAreaField, DecimalField
from wtforms.widgets.html5 import DateInput, DateTimeLocalInput, EmailInput, RangeInput
from wtforms.fields.html5 import IntegerField
from gallery.custom_widgets import TestInput


class DemoForm(FlaskForm):
    demo_str = StringField(label='Standard string field')
    demo_select = SelectField(label='Standard dropdown selector',
                              choices=[('Alt1', '1'), ('Alt2', '2'), ('Alt3', '3')])
    demo_radio = RadioField(label='Standard radio buttons selector',
                            choices=[('Alt1', 'Select 1'), ('Alt2', 'Select 2'), ('Alt3', 'Select 3')])
    demo_boolean = BooleanField(label="Standard Yes/No (boolean) field")
    demo_date = DateField(label='Standard date field', widget=DateInput())
    demo_datetime = DateTimeField(label='Standard date and time field', widget=DateTimeLocalInput())
    demo_email = StringField(label='Email input field', widget=EmailInput())
    demo_textarea = TextAreaField(label='Textarea for more exhaustive input')
    demo_range = IntegerField(label='Range field', widget=RangeInput())
