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
    return render_template("map.html")


@app.route("/lesson")
def lesson():
    return render_template("lesson.html")

# @app.route("/point")
# def point():
#     return render_template("point.html")


@app.route("/regist", methods=["GET"])
def regist_get():
    if 'user_id' in session:
        return redirect("/point")
    else:
        return render_template("regist.html")


@app.route("/regist", methods=['POST'])
def regist_post():
    name = request.form.get("name")
    password = request.form.get("password")
    conn = sqlite3.connect('prog.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES(null,?,?)", (name, password))
    conn.commit()
    c.close()
    return redirect("/login")


@app.route("/login", methods=["GET"])
def login_get():
    if 'user_id' in session:
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
    c.close()
    if user_id is None:
        return render_template("login.html")
    else:
        session['user_id'] = user_id[0]
        return redirect("/point")


@app.route("/logout")
def logout():
    session.pop('user_id', None)
    return redirect("/login")


@app.route("/point")
def point():
    if 'user_id' in session:
        conn = sqlite3.connect('prog.db')
        c = conn.cursor()
        c.execute("select user_name , point, Lv from user where id = ?", (id,))
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
