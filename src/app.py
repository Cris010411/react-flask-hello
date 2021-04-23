"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, send_from_directory
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from api.utils import APIException, generate_sitemap
from api.models import db
from api.routes import api
from api.admin import setup_admin
from models import db, User
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity
import json
#from models import Person

ENV = os.getenv("FLASK_ENV")
static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../public/')
app = Flask(__name__)
app.url_map.strict_slashes = False

# database condiguration
if os.getenv("DATABASE_URL") is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)

# Allow CORS requests to this API
CORS(app)

# add the admin
setup_admin(app)

# Add all endpoints form the API with a "api" prefix
app.register_blueprint(api, url_prefix='/api')

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    if ENV == "development":
        return generate_sitemap(app)
    return send_from_directory(static_file_dir, 'index.html')

# any other endpoint will try to serve it like a static file
# @app.route('/<path:path>', methods=['GET'])
# def serve_any_other_file(path):
#     if not os.path.isfile(os.path.join(static_file_dir, path)):
#         path = 'index.html'
#     response = send_from_directory(static_file_dir, path)
#     response.cache_control.max_age = 0 # avoid cache memory
#     return response

# #INICIO DE PROYECTO
# @app.route("/login", methods=["POST"])
# def login():
#     email=request.json.get("email", None)
#     password=request.json.get("password", None)

#     user=User.query.filter_by(email=email, password=password).first()
#     if user is None:
#         return jsonify ({"message:" "Bad user or password"})

#     access_token = create_access_token(identity=user.id)
#     return jsonify({"token": access_token})

# @app.route("/protected", methods=["GET"])
# @jwt_required()
# def protected():
#     current_user_id=get_jwt_identity()
#     user=User.query.get(current_user_id)
#     return jsonify({"id":user.id, "email":user.email})

# @app.route("/createUser", methods=["POST"])
# def create_User():
#     email=request.json.get("email", None)
#     password=request.json.get("password", None)
#     name=request.json.get("name", None)
#     user=User(email=email, password=password, name=name)
#     db.session.add(user)
#     db.session.commit()
#     return jsonify({"user":"ok"})

@app.route('/user', methods=['GET'])
def getUser():
    usuario = User.query.all()
    request = list(map(lambda user:user.serialize(),usuario))    
    return jsonify(request), 200


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3001))
    app.run(host='0.0.0.0', port=PORT, debug=True)
