from flask import Flask


def create_app():
    app = Flask(__name__)

    # configuration (لاحقًا)
    app.config["RESTX_MASK_SWAGGER"] = False

    return app
