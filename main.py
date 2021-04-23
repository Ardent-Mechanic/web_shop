from flask import Flask, render_template, url_for
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    # arr = []
    # for root, dirs, files in os.walk("./static/img/carusel_img"):
    #     for filename in files:
    #         arr.append(filename)
    return render_template('test.html', link=url_for('static', filename='css/style.css'),)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
