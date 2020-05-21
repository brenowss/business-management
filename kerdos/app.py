from flask import Flask
from kerdos.ext import configuration
from kerdos.blueprints.charts.charts import charts
from kerdos.blueprints.auth.auth import auth
from kerdos.blueprints.landing.landing import landing


def create_app():
    app = Flask(__name__)
    app.register_blueprint(charts)
    app.register_blueprint(auth)
    app.register_blueprint(landing)
    # configuration.init_app(app)
    return app
