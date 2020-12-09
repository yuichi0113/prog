# Flaskからimportしてflaskを使えるようにする。
from flask import Flask, render_template, request, redirect
import sqlite3

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


@app.route("/menu")
def menu():
    return render_template("menu.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/point")
def point():
    if

    # conn = sqlite3.connect('flasktest.db')
    # c = conn.cursor()
    # c.execute("select person_name from persons")

    return render_template("point.html")


@app.errorhandler(404)
def notfound(code):
    return "404ページだよ。ごめんね"


if __name__ == "__main__":
    # Flaskが持っている開発用サーバーを実行します。
    app.run(debug=True)
