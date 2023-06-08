from .helpers import check_competition_date
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'something_special'

    from .server import routes

    app.register_blueprint(routes, url_prefix='/')
    app.add_template_filter(check_competition_date)

    return app
