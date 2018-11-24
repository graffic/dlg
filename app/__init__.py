"""Application module

Configures the quart app
"""
from quart import Quart
from app.total import total

def build_app():
    """Builds a new quart app"""
    app = Quart(__name__)
    app.register_blueprint(total, '/total')
    return app
