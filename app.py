# Flaskからimportしてflaskを使えるようにする。
from flask import Flask, render_template, request, redirect
import sqlite3
import random

# appっていう名前でFlaskアプリを作っていくよーみたいな
app = Flask(__name__)

# 秘密鍵
app.secret_key = "prog"


@app.route("/")
def template():
    return render_template("top.html")


@app.route("/point")
def point():


@app.errorhandler(404)
def notfound(code):
    return "404ページだよ。ごめんね"


if __name__ == "__main__":
    # Flaskが持っている開発用サーバーを実行します。
    app.run(debug=True)
