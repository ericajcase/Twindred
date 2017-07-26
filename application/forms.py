from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, HiddenField, validators, widgets, SelectMultipleField
from wtforms.validators import DataRequired


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class SearchForm(FlaskForm):
    hashtag = StringField('#',  [
        validators.DataRequired(),
        validators.Length(min=1, max=139)
        ])

class SimpleForm(FlaskForm):
    pos = MultiCheckboxField('Label', choices=[])
    neg = MultiCheckboxField('Label', choices=[])

class AutoSearch(FlaskForm):
    hashtag = HiddenField('hashtag')
