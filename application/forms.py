from flask_wtf import Form
from wtforms import StringField, BooleanField, validators, widgets, SelectMultipleField
from wtforms.validators import DataRequired

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class SearchForm(Form):
    hashtag = StringField('#',  [
        validators.DataRequired(),
        validators.Length(min=1, max=139)
        ])

class SimpleForm(Form):
    pos = MultiCheckboxField('Label', choices=[])
    neg = MultiCheckboxField('Label', choices=[])
