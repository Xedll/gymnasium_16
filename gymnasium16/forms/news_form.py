from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField, FileField
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    img = FileField('Фотография', validators=[DataRequired()])
    description = TextAreaField('Краткое описание', validators=[DataRequired()]) 
    content = TextAreaField('Новость', validators=[DataRequired()])
    submit = SubmitField('Применить', validators=[DataRequired()])
