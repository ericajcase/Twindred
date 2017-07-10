from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class SearchForm(Form):
    hashtag = StringField('#', validators=[
        DataRequired(),
        Length(min=1, max=139)
        ])
