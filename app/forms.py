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
    string_of_files = ['one\r\ntwo\r\nthree\r\n']
    list_of_files = string_of_files[0].split()
    # create a list of value/description tuples
    files = [(x, x) for x in list_of_files]

    example = MultiCheckboxField('Label', choices=files)
