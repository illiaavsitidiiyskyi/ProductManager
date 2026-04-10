from flask import Flask, render_template, request, redirect, url_for, flash
from models import init_db
from action_db import *
app = Flask(__name__)
app.secret_key = '123'
init_db()



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name').lower()
        price = float(request.form.get('price'))
        category = request.form.get('category').lower()

        if product_exist(name):
            flash('Такий товар вже існує')
        else:
            add_product(name, price, category)

        return redirect(url_for('index'))

    # збираємо всі категорії
    all_categories = get_all_categories()

    # фіксуємо обрану категорії
    choice_category = request.args.get('category', 'all')

    # фільтруємо список товарів
    if choice_category == 'all':
        filter_products = get_all_products()
    else:
        filter_products = get_product_by_category(choice_category)

    return render_template('index.html',
                           products=filter_products,
                           categories=all_categories,
                           choice_category=choice_category)


@app.route('/delete/<name>')
def delete(name):
    delete_product(name)
    return redirect(url_for('index'))

app.run(debug=True)