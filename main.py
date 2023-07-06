from flask import Flask, jsonify, request

app = Flask(__name__)

animals = [
    {"id": 1, "name": "Nina", "type": "cachorro"},
    {"id": 2, "name": "Preta", "type": "cachorro"},
    {"id": 3, "name": "Pity", "type": "cachorro"}
]

#Get all
@app.route('/animals', methods=['GET'])
def all_animals():
    return jsonify(animals)

#Get animal by id
@app.route('/animals/<int:animal_id>', methods=["GET"])
def get_animal_by_id(animal_id):
    animal = next((animal for animal in animals if animal['id'] == animal_id), None)
    if animal:
        return jsonify(animal)
    return jsonify({"message":"Animal not found"}), 404

#Post animal
@app.route('/animals', methods=['POST'])
def save_animal():
    new_animal = {
        "id": len(animals) + 1,
        "name": request.json['name'],
        "type": request.json['type']
    }
    
    animals.append(new_animal)
    return jsonify(new_animal), 201

#Update animal
@app.route('/animals/<int:animal_id>', methods=['PUT'])
def update_animal(animal_id):
    animal = next((animal for animal in animals if animal['id'] == animal_id), None)
    if animal:
        animal['name'] = request.json['name']
        animal['type'] = request.json['type']
        return jsonify(animal)
    return jsonify({"message":"Animal not found"}), 404


#server execution
if __name__ == '__main__':
    app.run()
