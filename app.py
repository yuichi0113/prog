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
    return render_template("login.html")


@app.route("/map")
def map():
    # flasktest.dbに接続します
    conn = sqlite3.connect("prog.db")
    c = conn.cursor()
    sql = "SELECT list, time, category_id  FROM maps ;"
    # sql文を実行
    c.execute(sql)
    # 取ってきた内容を変数に格納する
    map_info = c.fetchall()
    # データベースの接続終了
    c.close()

    # flasktest.dbに接続します
    conn = sqlite3.connect("prog.db")
    c = conn.cursor()
    sql = "SELECT category FROM categories"
    c.execute(sql)
    category_info = c.fetchall()
    # データベースの接続終了
    c.close()
    return render_template("map.html", map_info=map_info, category_info=category_info)


@app.route("/menu")
def menu():
    return render_template("menu.html")


@app.route("/lesson")
def lesson():
    return render_template("lesson.html")


@app.route("/regist", methods=["GET"])

def regist_get():
    if 'id' in session:
        return redirect("/point")
    else:
        return render_template("regist.html")


@app.route("/regist", methods=['POST'])
def regist_post():
    name = request.form.get("name")
    password = request.form.get("password")
    print(name)
    conn = sqlite3.connect('prog.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES(null,?,?)", (name, password))
    conn.commit()
    c.close()
    return redirect("/login")


@app.route("/login", methods=["GET"])
def login_get():
    if 'id' in session:
        return redirect("/point")
    else:
        return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    name = request.form.get("name")
    password = request.form.get("password")
    conn = sqlite3.connect('prog.db')
    c = conn.cursor()
    c.execute(
        "SELECT id FROM users WHERE user_name= ? and password = ?", (name, password))
    id = c.fetchone()
    c.close()
    if id is None:
        return render_template("login.html")
    else:
        session['id'] = id[0]
    return redirect("/point")


@app.route("/logout")
def logout():
    session.pop('id', None)
    return redirect("/login")


# @app.route("/point")
# def point():
#     return render_template("point.html")

@app.route("/point")
def point():
    if 'id' in session:
        id = session['id']
        conn = sqlite3.connect('prog.db')
        c = conn.cursor()
        c.execute("select * from users where id = ?", (id,))
        user_status = c.fetchone()
        c.close()
        return render_template("point.html", user_status=user_status)
    else:
        return redirect("/login")


@app.errorhandler(404)
def notfound(code):
    return "404ページだよ。ごめんね"


if __name__ == "__main__":
    # Flaskが持っている開発用サーバーを実行します。
    app.run(debug=True)
