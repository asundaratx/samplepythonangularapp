from flask import Flask, json, request
from app.kudo.service import Service as Kudo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

user_id=1234
kudo_service = Kudo(user_id)

@app.route("/kudos", methods=["GET"])
def index():
 user_id=1234
 return json_response(kudo_service.find_all_kudos())


@app.route("/kudos", methods=["POST"])
def create():
   user_id=1234
   payload = json.loads(request.data)
   print("request payload: {}".format(payload))
   kudo = kudo_service.create_kudo_for(payload)
   return json_response(kudo)


@app.route("/kudo/<int:repo_id>", methods=["DELETE"])
def delete(repo_id):
 print("repo id:{}".format(repo_id))
 if kudo_service.delete_kudo_for(repo_id):
   return json_response({})
 else:
   return json_response({'error': 'kudo not found'}, 404)


def json_response(payload, status=200):
 return (json.dumps(payload), status, {'content-type': 'application/json'})
