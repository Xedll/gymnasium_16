from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, URLField
from wtforms import SubmitField
from wtforms.validators import DataRequired, Length


class NewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    img = URLField("Ссылка на фото", validators=[DataRequired()])
    description = TextAreaField('Краткое описание', validators=[DataRequired(), Length(max=200)]) 
    content = TextAreaField('Новость', validators=[DataRequired()])
    submit = SubmitField('Применить')
