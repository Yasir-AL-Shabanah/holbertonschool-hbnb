from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from hbnb.app.extensions import bcrypt, jwt

db = SQLAlchemy()

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # السماح للمتصفح بالاتصال (CORS)
    CORS(app, resources={r"/*": {"origins": "*"}})

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    api = Api(app, version="1.0", title="HBnB API", description="HBnB Application API", doc="/api/v1/")

    # استدعاء ملفات الـ API (تأكد أن هذه الملفات موجودة لديك من Part 2)
    # إذا ظهر خطأ هنا، فهذا يعني أن ملفات Part 2 ناقصة
    from hbnb.app.api.v1.users import api as users_ns
    from hbnb.app.api.v1.places import api as places_ns
    from hbnb.app.api.v1.reviews import api as reviews_ns
    from hbnb.app.api.v1.amenities import api as amenities_ns
    from hbnb.app.api.v1.auth import api as auth_ns

    # تسجيل المسارات
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(auth_ns, path='/api/v1/auth')

    return app
