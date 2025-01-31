from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class RCB(Resource):
    list = []

    def get(self):
        return {"players": RCB.list}

    def post(self):
      
        data = request.get_json() 
        player = data.get('player') 
        RCB.list.append(player)
        return {"message": f"Player {player} added successfully!"}, 

api.add_resource(RCB, '/rcb')

if __name__ == '__main__':
    app.run(debug=True)
