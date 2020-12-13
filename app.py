# Flaskからimportしてflaskを使えるようにする。
from flask import Flask, render_template, request, redirect, session
import sqlite3
import random

# appっていう名前でFlaskアプリを作っていくよーみたいな
app = Flask(__name__)

# 秘密鍵
app.secret_key = "prog"


@app.route("/")
def template():
    return render_template("top.html")

@app.route("/map")
def map():
    # flasktest.dbに接続します
    conn = sqlite3.connect("prog.db")
    c = conn.cursor()
    sql = "SELECT list, time, category_id  FROM maps ;"
    # sql文を実行
    c.execute(sql)
    # 取ってきた内容を変数に格納する
    map_info = c.fetchone()
    # データベースの接続終了
    c.close()
    return render_template("map.html", map_info=map_info)


@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/touroku")
def touroku():
    return render_template("touroku.html")


@app.route("/login")
def login():
    return render_template("login.html")


# @app.route('/<name>')
# def greet(name):
#     return name + "さんこんにちは"


# @app.route('/template')
# def template():
#     py_name = 'wataru'
#     return render_template('index.html', name=py_name)


@app.route("/point")
def point():
    if 'user_id' in session:
        conn = sqlite3.connect('prog.db')
        c = conn.cursor()
        c.execute("select user_name , point, Lv, from user where id = ?", (id,))
        user_status = c.fetchone()
        c.close()
        return render_template("point.html", user_status=user_status)
    else:
        return redirect('/login')


# @app.route('/weather')
# def weather():
#     py_weather = '大雪のちみぞれ'
#     return render_template('base.html', tenki=py_weather)


@app.route('/dbtest')
def dbtest():
    # flasktest.dbに接続
    conn = sqlite3.connect('flasktest.db')
    # 中身が見られるようにしている
    c = conn.cursor()
    # SQL文の実行
    c.execute("select name,age,address from users")
    # 取ってきたレコードを格納
    user_info = c.fetchone()
    # データベース接続完了
    c.close()

    print(user_info)
    return render_template('dbtest.html', user_info=user_info)


@app.route('/add', methods=["GET"])
def add_get():
    if 'user_id' in session:
        return render_template('add.html')
    else:
        return redirect('/login')

    # get通信はページを読み取る専門


@app.route('/add', methods=["POST"])
def add_post():
    # フォームのtaskに入力されたデータを取得
    task = request.form.get("task")
    user_id = session['user_id']
    # DBと接続
    conn = sqlite3.connect('flasktest.db')
    c = conn.cursor()
    c.execute("insert into task values(null,?,?)", (task, user_id))
    # 変更を確定する
    conn.commit()
    conn.close()
    return redirect('/list')

    # post通信はデータを追加・登録・更新したりできる。


@app.route('/list')
def task_list():
    if 'user_id' in session:
        user_id = session['user_id']
        conn = sqlite3.connect('flasktest.db')
        c = conn.cursor()
        c.execute("select id, task from task where user_id = ?", (user_id,))
        task_list = []
        for row in c.fetchall():
            task_list.append({"id": row[0], "task": row[1]})
        c.close()
        return render_template('tasklist.html', task_list=task_list)

    else:
        return redirect('/login')


@app.route('/edit/<int:id>')
def edit(id):
    if 'user_id' in session:
        conn = sqlite3.connect('flasktest.db')
        c = conn.cursor()
        c.execute("select task from task where id = ?", (id,))
        task = c.fetchone()
        c.close()
        if task is not None:
            task = task[0]
        else:
            return "タスクはありません！"
        item = {"id": id, "task": task}
        return render_template('edit.html', task=item)
    else:
        return redirect("/login")


@app.route('/edit', methods=["POST"])
def edit_post():
    item_id = request.form.get("html_task_id")
    # inputタグはテキスト型なので、int型に修正
    item_id = int(item_id)
    task = request.form.get("html_task")

    conn = sqlite3.connect('flasktest.db')
    c = conn.cursor()
    c.execute("UPDATE task SET task = ? WHERE id = ?", (task, item_id))
    conn.commit()
    c.close()
    return redirect('/list')


@app.route('/del/<int:id>')
def task_del(id):
    if 'user_id' in session:
        conn = sqlite3.connect('flasktest.db')
        c = conn.cursor()
        c.execute("delete from task where id = ?", (id,))
        conn.commit()
        c.close()
        return redirect('/list')
    else:
        return redirect("/login")


@app.route('/regist')
def regist_get():
    if 'user_id' in session:
        return redirect("/list")
    else:
        return render_template('regist.html')


@app.route('/regist', methods=["POST"])
def regist_post():
    name = request.form.get("member_name")
    print(name)
    password = request.form.get("member_password")
    print(password)
    conn = sqlite3.connect('flasktest.db')
    c = conn.cursor()
    c.execute("insert into member values(null,?,?)", (name, password))
    conn.commit()
    c.close()
    return "登録完了"


@app.route('/login', methods=["GET"])
def login_get():
    if 'user_id' in session:
        return redirect("/list")
    else:
        return render_template("login.html")
# ログインの時は一番最初にloginページを読み込む必要があるからrender_templateになる


@app.route('/login', methods=["POST"])
def login_post():
    name = request.form.get("member_name")
    password = request.form.get("member_password")
    conn = sqlite3.connect('flasktest.db')
    c = conn.cursor()
    c.execute("select id from member where name=? and password = ?",
              (name, password))
    user_id = c.fetchone()
    print(user_id)
    c.close()
    if user_id is None:
        return render_template("login.html")
    else:
        session['user_id'] = user_id[0]
        return redirect("/list")


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect("/login")


@app.errorhandler(404)
def notfound(code):
    return "404ページだよ。すまんね"


# flaskが持っている開発用サーバーを起動する
if __name__ == "__main__":
    app.run(debug=True)


@app.route("touroku.html")
def login():
    return render_template("touroku.html")


@app.route("/menu")
def menu():
    return render_template("menu.html")


@app.errorhandler(404)
def notfound(code):
    return "404ページだよ。ごめんね"


if __name__ == "__main__":
    # Flaskが持っている開発用サーバーを実行します。
    app.run(debug=True)
