from flask import Flask, render_template, redirect, request
from flask_login import LoginManager, login_required, login_user, logout_user
import json

from forms.news_form import NewsForm
from forms.login_form import LoginForm
from data.admin import Admin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gymnasium16_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return Admin(id, "admin", "admin123")


@app.route('/')
def index():
    with open("./data/news.json", "r") as f:
        data = json.load(f)
        f.close()
    news = data["news"][::-1][:6]
    return render_template('index.html', title="Гимназия 16", news=news)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.login.data == "admin" and form.password.data == "admin123":
            admin = Admin(1, "admin", "admin123")
            login_user(admin, remember=form.remember_me.data)
            return redirect('/')
        return render_template("login.html", title="Авторизация", form=form, message="Неправильный логин или пароль!")
    return render_template('login.html', title="Авторизация", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/news')
def news():
    with open("./data/news.json", "r") as f:
        data = json.load(f)
        f.close()
    news = data["news"][::-1]
    return render_template("news.html", title="Новости Гимназии", news=news)


@app.route('/news/<int:id>')
def news_one(id):
    with open("./data/news.json", "r") as f:
        data = json.load(f)
        f.close()
    news = None
    for i in data["news"]:
        if i["id"] == id:
            news = i
            break
    if news is not None:
        return render_template("one_news.html", title=news["title"], item=news)
    return "Новость не найдена"


@app.route("/news/create", methods=["GET", "POST"])
@login_required
def news_create():
    form = NewsForm()
    if form.validate_on_submit():
        with open("./data/news.json", "r") as f:
            d = json.load(f)
            f.close()
        if len(d["news"]) == 0:
            id = 1
        else:
            id = d["news"][-1]["id"] + 1
        data = {
            "id": id,
            "title": form.title.data,
            "img": form.img.data,
            "description": form.description.data,
            "content": form.content.data
        }
        d["news"].append(data)
        with open("./data/news.json", "w") as f:
            json.dump(d, f)
            f.close()
        return redirect("/news")
    return render_template("add_news.html", title="Создать новость", form=form)


@app.route("/news/delete/<int:id>", methods=['GET', 'POST'])
@login_required
def news_delete(id):
    with open("./data/news.json", "r") as f:
        d = json.load(f)
        f.close()
    i = 0
    flag = False
    for news in d["news"]:
        if news["id"] == id:
            flag = True
            break
        i += 1
    if flag:
        print(i)
        del d["news"][i]
    with open("./data/news.json", "w") as f:
        json.dump(d, f)
        f.close()
    return redirect('/news')


@app.route('/news/edit/<int:id>', methods=['GET', 'POST'])
def edit_news(id):
    form = NewsForm()
    if request.method == 'GET':
        with open("./data/news.json", "r") as f:
            data = json.load(f)
            f.close()
        news = None
        for i in data["news"]:
            if i["id"] == id:
                news = i
                break
        if news is not None:
            form.title.data = news["title"]
            form.description.data = news["description"]
            form.img.data = news["img"]
            form.content.data = news["content"]
        else:
            return "Новость не найдена!"
    if form.validate_on_submit():
        with open("./data/news.json", "r") as f:
            d = json.load(f)
            f.close()
        i = 0
        flag = False
        for news in d["news"]:
            if news["id"] == id:
                flag = True
                break
            i += 1
        if flag:
            d["news"][i]["title"] = form.title.data
            d["news"][i]["description"] = form.description.data
            d["news"][i]["img"] = form.img.data
            d["news"][i]["content"] = form.content.data
            with open("./data/news.json", "w") as f:
                json.dump(d, f)
                f.close()
            return redirect("/news")
        return "Ошибка!"
    return render_template("add_news.html", title="Изменение новости", form=form)


def main():
    app.run()


if __name__ == '__main__':
    main()


# from flask import Flask, render_template, redirect, request
# from flask_login import LoginManager, login_user, logout_user, login_required, current_user


# from data import db_session
# from forms.news_form import NewsForm
# from forms.login_form import LoginForm
# from data.news import News
# from data.admins import Admin
# from werkzeug.utils import secure_filename
# import os
# import os.path

# app = Flask(__name__)

# app.config['SECRET_KEY'] = 'gymnasium16_secret_key'

# login_manager = LoginManager()
# login_manager.init_app(app)


# @login_manager.user_loader
# def load_user(user_id):
#     db_sess = db_session.create_session()
#     return db_sess.query(Admin).get(user_id)


# @app.route('/')
# def index():
#     db_sess = db_session.create_session()
#     news = db_sess.query(News).all()[::-1]
#     if len(news) > 5:
#         news = news[:6]

#     return render_template('index.html', title="Гимназия №16", news=news)


# @app.route('/news')
# def news():
#     db_sess = db_session.create_session()
#     news = db_sess.query(News).all()[::-1]
#     return render_template('news.html', title="Новости Гимназии", news=news)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         db_sess = db_session.create_session()
#         admin = db_sess.query(Admin).filter(
#             Admin.login == form.login.data).first()
#         if admin and admin.check_password(form.password.data):
#             login_user(admin, remember=form.remember_me.data)
#             return redirect('/')
#         return render_template('login.html',
#                                title='Авторизация',
#                                form=form,
#                                message='Неправильный логин или пароль')
#     return render_template("login.html", title="Авторизация", form=form)


# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect("/")


# @app.route('/news/create', methods=['GET', 'POST'])
# @login_required
# def add_news():
#     form = NewsForm()
#     if form.validate_on_submit():
#         db_sess = db_session.create_session()
#         news = News()
#         news.title = form.title.data
#         news.description = form.description.data
#         news.content = form.description.data
#         f = form.img.data
#         filename = secure_filename(f.filename)
#         i = 1
#         while os.path.isfile(f"static\\img\\news\\{filename}"):
#             if not os.path.isfile(f"static\\img\\news\\{i}_{filename}"):
#                 filename = str(i) + "_" + filename
#                 break
#             i += 1
#         f.save(os.path.join("static\\img", 'news', filename))
#         news.img_src = filename
#         db_sess.add(news)
#         db_sess.commit()
#         return redirect('/news')
#     return render_template('add_news.html', title="Добавление новостей", form=form)


# @app.route("/news/<int:id>")
# def one_news(id):
#     db_sess = db_session.create_session()
#     news = db_sess.query(News).filter(News.id == id).first()
#     return render_template('one_news.html', title=news.title, news=news)


# @app.route("/news/delete/<int:id>", methods=['GET', 'POST'])
# @login_required
# def news_delete(id):
#     db_sess = db_session.create_session()
#     news = db_sess.query(News).filter(News.id == id).first()
#     if news:
#         db_sess.delete(news)
#         db_sess.commit()
#     return redirect('/news')


# def main():
#     db_session.global_init("./db/news.db")
#     app.run()


# if __name__ == '__main__':
#     main()
