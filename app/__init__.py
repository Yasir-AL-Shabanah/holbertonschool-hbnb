from flask import Flask
from flask_cors import CORS
from config import config

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # تفعيل CORS
    CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
    
    # تسجيل الـ Blueprints (قد تحتاج للتأكد من مساراتك هنا يدوياً لاحقاً)
    # from app.api.v1.users import users_bp
    # app.register_blueprint(users_bp)
    
    return app
