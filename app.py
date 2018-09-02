from flask import Flask
from gallery.gallery_bp import bp
import os

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

