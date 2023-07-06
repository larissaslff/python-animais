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


@app.route('/animals/<int:animal_id>', methods=["GET"])
def get_animal_by_id(animal_id):
    animal = next((animal for animal in animals if animal['id'] == animal_id), None)
    if animal:
        return jsonify(animal)
    return jsonify({"messagem":"Animal não encontrado"}), 404


#server execution
if __name__ == '__main__':
    app.run()
