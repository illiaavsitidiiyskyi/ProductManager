from flask import Blueprint, request, render_template, url_for, session, redirect, flash
from action_db import *

product_bp = Blueprint('product', __name__, template_folder='templates')


def is_logged():
    return 'company_name' in session


def current_company():
    name_company = session.get('company_name')
    if not name_company:
        return None
    return get_company_by_name(name_company)


@product_bp.route('/', methods=['GET', 'POST'])
def index():
    if not is_logged():
        return redirect(url_for('auth.login'))

    company = current_company()

    # Add this check to handle None company
    if company is None:
        flash('Company not found. Please log in again.', 'error')
        session.clear()  # Clear invalid session
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        name = request.form.get('name').lower()
        price = float(request.form.get('price'))
        category = request.form.get('category').lower()

        if product_exist(name, company.id):
            flash('Product already exists!')
        else:
            add_product(name, price, category, company.id)
            flash('Product added!')
        return redirect(url_for('product.index'))

    # Get all categories
    all_categories = get_all_categories(company.id)

    # Get selected category
    choice_category = request.args.get('category', 'all')

    # Filter products
    if choice_category == 'all':
        filter_products = get_all_products(company.id)
    else:
        filter_products = get_product_by_category(choice_category, company.id)

    return render_template('product/index.html',
                           products=filter_products,
                           categories=all_categories,
                           choice_category=choice_category)


@product_bp.route('/delete/<name>')
def delete(name):
    if not is_logged():
        return redirect(url_for('auth.login'))

    company = current_company()

    # Add this check here too
    if company is None:
        flash('Company not found. Please log in again.', 'error')
        session.clear()
        return redirect(url_for('auth.login'))

    delete_product(name, company.id)
    flash(f'Product {name} - deleted!')
    return redirect(url_for('product.index'))


@product_bp.route('/edit')
def edit():
    return render_template('product/edit.html')