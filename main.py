from flask import Flask, render_template, url_for, request
import os

app = Flask(__name__)



@app.route('/')
@app.route('/main_page')
def main():
    link2 = ".." + url_for('static', filename='css/style.css')
    return render_template('test.html', link=link2)


@app.route('/ship&payment')
def shipping_and_payment():
    return render_template('urn.html')


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
