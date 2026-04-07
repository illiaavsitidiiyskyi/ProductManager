from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = '123'
products = [
    {'name': 'phone', 'price': 3000, 'category': 'device'},
    {'name': 'notebook', 'price': 100, 'category': 'school'}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name').lower()
        price = request.form.get('price')
        category = request.form.get('category').lower()

        for item in products:
            if item.get('name') == name:
                flash('Такий товар вже є!')
                break
        else:
            info_product = {'name': name, 'price': price, 'category': category}
            products.append(info_product)

        return redirect(url_for('index'))

    # збираємо всі категорії
    all_categories = map(lambda item: item['category'], products)

    # фіксуємо обрану категорії
    choice_category = request.args.get('category', 'all')

    # фільтруємо список товарів
    if choice_category == 'all':
        filter_products = products
    else:
        filter_products = filter(lambda item: item['category'] == choice_category, products)

    return render_template('index.html',
                           products=filter_products,
                           categories=all_categories,
                           choice_category=choice_category)


@app.route('/delete/<index>')
def delete(index):
    print(index)


app.run(debug=True)