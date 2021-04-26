from flask import Flask, render_template, url_for, request, make_response, session
from shop_products import db_session
from shop_products.products import Prod

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init("db/shop_prod.db")
db_sess = db_session.create_session()


# products = Prod()

@app.route('/')
@app.route('/main_page')
def main_page():
    link2 = ".." + url_for('static', filename='css/style.css')
    return render_template('test.html', link=link2)


@app.route('/ship&payment')
def shipping_and_payment():
    return render_template('urn.html')


@app.route('/admin', methods=['POST', 'GET'])
def admin_panel():
    if request.method == 'GET':
        return render_template('admin_panel.html')
    elif request.method == 'POST':
        db_sess.add(Prod(type=request.form['type'], name=request.form['name'], price=int(request.form['price']),
                         info=request.form['info'], quantity=request.form['quantity']))
        db_sess.commit()
        return render_template('admin_panel.html')


def main():
    db_session.global_init("db/shop_prod.db")

    app.run(port=5000, host='127.0.0.1')


if __name__ == '__main__':
    main()