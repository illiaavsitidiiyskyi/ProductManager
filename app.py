from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = '123'
products = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        category = request.form.get('category')

        for item in products:
            if item.get('name') == name:
                flash('Такий товар вже є!')
                break
        else:
            info_product = {'name': name, 'price': price, 'category': category}
            products.append(info_product)

        return redirect(url_for('index'))

    return render_template('index.html', products=products)


@app.route('/delete/<int:index>')
def delete(index):
    product_name = products[index]['name']
    products.pop(index)
    flash(f'Товар {product_name} видалено!')
    return redirect(url_for('index'))


app.run(debug=True)