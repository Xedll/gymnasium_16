from flask import Flask, render_template, redirect, request

from data import db_session
from forms.news_form import NewsForm
from data.news import News

app = Flask(__name__)

app.config['SECRET_KEY'] = 'gymnasium16_secret_key'


@app.route('/')
def index():
    return render_template('index.html', title="Гимназия №16")

@app.route('/news')
def news():
    return render_template('news.html', title="Новости Гимназии")

@app.route('/news/create', methods=['GET', 'POST'])
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = News()
        news.title = form.title.data
        news.description = form.description.data
        news.content = form.description.data
        db_sess.add(news)
        db_sess.commit()
        return redirect('/news')
    return render_template('add_news.html', title="Добавление новостей", form=form)

def main():
    db_session.global_init("db/blogs.db")
    app.run()


if __name__ == '__main__':
    main()
