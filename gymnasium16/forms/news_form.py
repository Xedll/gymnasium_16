from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, TextAreaField
from wtforms import SubmitField
from wtforms.validators import DataRequired, Length


class NewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    img = FileField('Фотографии', validators=[FileRequired()])
    description = TextAreaField('Краткое описание', validators=[DataRequired(), Length(max=100)]) 
    content = TextAreaField('Новость', validators=[DataRequired()])
    submit = SubmitField('Применить')
