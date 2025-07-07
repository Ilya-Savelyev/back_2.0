from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    # Конфигурация базы данных и других настроек
    app.config.from_object('app.config')
    # Инициализация расширений
    db.init_app(app)
    from . import routes
    app.register_blueprint(routes.bp)
    # Регистрация маршрутов (blueprints или напрямую)
    with app.app_context():
        from . import routes

    return app