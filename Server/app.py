from flask import request, jsonify, session, make_response
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask_cors import CORS
from services import app, db

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pawesomeDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)
CORS(app)

# app.secret_key = os.environ.get("secretkey")


if __name__ == '__main__':
    app.run(port=5555)