from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

""" animals = [
    {"id": 1, "name": "Nina", "type": "cachorro"},
    {"id": 2, "name": "Preta", "type": "cachorro"},
    {"id": 3, "name": "Pity", "type": "cachorro"}
]
 """
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='senhadomysql',
    database='pets'
)

#Get all
@app.route('/animals', methods=['GET'])
def all_animals():
    mycursor = db.cursor()
    mycursor.execute('SELECT * FROM pets')
    animals = []
    for animal in mycursor.fetchall():
        animals.append({
            "id": animal[0],
            "nome": animal[1],
            "tipo": animal[2]
        })
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
    name = request.json['name']
    type = request.json['type']
    
    mycursor = db.cursor()
    sql = 'INSERT INTO pets (name, type) VALUES (%s, %s)'
    val = (name, type)
    mycursor.execute(sql, val)
    db.commit()
    
    new_animal_id = mycursor.lastrowid
    new_animal = {
        'id': new_animal_id,
        'name': name,
        'type': type
    }
    
    return jsonify(new_animal), 201

#Update animal
@app.route('/animals/<int:animal_id>', methods=['PUT'])
def update_animal(animal_id):
    name = request.json['name']
    type = request.json['type']
    
    mycursor = db.cursor()
    sql = 'UPDATE pets SET name = %s, type = %s WHERE id = %s'
    val = (name, type, animal_id)
    mycursor.execute(sql, val)
    db.commit()
    
    if mycursor.rowcount > 0:
        animal = {
            'id': animal_id,
            'name': name,
            'type': type 
        }
        return jsonify(animal)
    return jsonify({"message":"Animal not found"}), 404

#Delete animals
@app.route('/animals/<int:animal_id>', methods=['DELETE'])
def delete_animals(animal_id):
    mycursor = db.cursor()
    sql = 'DELETE FROM pets WHERE id = %s'
    val = (animal_id)
    mycursor.execute(sql, (val,))
    db.commit()
    
    
    if mycursor.rowcount > 0:
        return jsonify({"message":"Animal deleted successfully"})
    return jsonify({"message":"Animal not found"}), 404
    
    

#server execution
if __name__ == '__main__':
    app.run()
