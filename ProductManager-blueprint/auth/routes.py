from flask import Blueprint, request, render_template, url_for, session, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from action_db import *

auth_bp = Blueprint('auth', __name__, template_folder='templates')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name_company = request.form.get('name_company').lower()
        password = request.form.get('password')

        if company_exists(name_company):
            flash('Така компанія вже є!')
            return redirect(url_for('auth.register'))
        else:
            # отримуємо хеш паролю
            password_hash = generate_password_hash(password)

            flash(f'Компанія {name_company} зареєстрована!')
            add_company(name_company, password_hash)

            return redirect(url_for('auth.login'))

    return render_template('auth/register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name_company = request.form.get('name_company').lower()
        password = request.form.get('password')

        if not company_exists(name_company):
            flash(f'Компанія {name_company} НЕ ІСНУЄ!')
            return redirect(url_for('auth.login'))

        company = get_company_by_name(name_company)
        if not check_password_hash(company.password, password):
            flash(f'Пароль НЕкоректний')
            return redirect(url_for('auth.login'))

        # зберігаємо в cookie файл запис про назву компанії
        session['company_name'] = company.name

        flash(f'Вітаємо, {company.name}!')
        return redirect(url_for('product.index'))

    return render_template('auth/login.html')
