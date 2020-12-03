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

<<<<<<< HEAD
@app.route("/map")
def map():
    return render_template("map.html")
=======
@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/menu2")
def menu2():
    return render_template("menu2.html")

@app.route("/menu3")
def menu3():
    return render_template("menu3.html")
>>>>>>> d65a5265474084e4104507a1b0af1beb5d274140

@app.errorhandler(404)
def notfound(code):
    return "404ページだよ。ごめんね"


if __name__ == "__main__":
    # Flaskが持っている開発用サーバーを実行します。
    app.run(debug=True)