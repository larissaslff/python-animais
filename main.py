from flask import Flask, jsonify

app = Flask(__name__)

animals = [
    {"id": 1, "nome": "Nina", "tipo": "cachorro"},
    {"id": 2, "nome": "Preta", "tipo": "cachorro"},
    {"id": 3, "nome": "Pity", "tipo": "cachorro"}
]

#Get all
@app.route('/animals', methods=['GET'])
def all_animals():
    return jsonify(animals)


#server execution
if __name__ == '__main__':
    app.run()
