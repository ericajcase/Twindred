from flask_wtf import Form
from wtforms import StringField, BooleanField, validators
from wtforms.validators import DataRequired

class SearchForm(Form):
    hashtag = StringField('#',  [
        validators.DataRequired(),
        validators.Length(min=1, max=139)
        ])
