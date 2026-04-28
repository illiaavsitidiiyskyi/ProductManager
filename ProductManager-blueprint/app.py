from flask import Flask
from models import init_db

# імпортація BLUEPRINT
from product.routes import product_bp
from auth.routes import auth_bp

app = Flask(__name__)
app.secret_key = '123'
init_db()

# Реєстрація BLUEPRINT
app.register_blueprint(product_bp)
app.register_blueprint(auth_bp)

app.run(debug=True)
