from flask import Flask, render_template, redirect, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_restful import abort


from data import db_session
from forms.news_form import NewsForm
from forms.login_form import LoginForm
from data.news import News
from data.admins import Admin
from werkzeug.utils import secure_filename
import os
import os.path

app = Flask(__name__)

app.config['SECRET_KEY'] = 'gymnasium16_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(Admin).get(user_id)


@app.route('/')
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).all()[::-1]
    if len(news) > 5:
        news = news[:6]

    return render_template('index.html', title="Гимназия №16", news=news)


@app.route('/news')
def news():
    db_sess = db_session.create_session()
    news = db_sess.query(News).all()[::-1]
    return render_template('news.html', title="Новости Гимназии", news=news)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        admin = db_sess.query(Admin).filter(
            Admin.login == form.login.data).first()
        if admin and admin.check_password(form.password.data):
            login_user(admin, remember=form.remember_me.data)
            return redirect('/')
        return render_template('login.html',
                               title='Авторизация',
                               form=form,
                               message='Неправильный логин или пароль')
    return render_template("login.html", title="Авторизация", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/news/create', methods=['GET', 'POST'])
@login_required
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = News()
        news.title = form.title.data
        news.description = form.description.data
        news.content = form.description.data
        f = form.img.data
        filename = secure_filename(f.filename)
        i = 1
        while os.path.isfile(f"static\\img\\news\\{filename}"):
            if not os.path.isfile(f"static\\img\\news\\{i}_{filename}"):
                filename = str(i) + "_" + filename
                break
            i += 1
        f.save(os.path.join("static\\img", 'news', filename))
        news.img_src = filename
        db_sess.add(news)
        db_sess.commit()
        return redirect('/news')
    return render_template('add_news.html', title="Добавление новостей", form=form)


@app.route("/news/<int:id>")
def one_news(id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.id == id).first()
    return render_template('one_news.html', title=news.title, news=news)


@app.route("/news/delete/<int:id>", methods=['GET', 'POST'])
@login_required
def news_delete(id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.id == id).first()
    if news:
        db_sess.delete(news)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/news')


def main():
    db_session.global_init("db/news.db")
    app.run()


if __name__ == '__main__':
    main()
