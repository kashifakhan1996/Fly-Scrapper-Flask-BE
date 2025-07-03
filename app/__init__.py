from flask import Flask


def create_app():
    app = Flask(__name__)

    from .routes.flights import flights_bp
    from .routes.insights import insights_bp
    app.register_blueprint(flights_bp,url_prefix='/api')
    app.register_blueprint(insights_bp, url_prefix='/api')
    return app