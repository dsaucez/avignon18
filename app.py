#BENCHRIFA Mohamed Amine
#CADI Hamza
#DESTREE Gabriel
#NDIAYE El Hadj Pathé 
#PORQUEZ William


# Import des différentes librairies flask
from flask import Flask, jsonify, render_template, redirect
from flask import make_response
from flask import abort
from flask import request
from flask import url_for
import hashlib
import random



app = Flask(__name__)

# On va générer une clé publique qui est donné par le hash md5 d'un nombre aléatoire.
#
def generate_hash():

	h = random.randint(1,101)
	h = hashlib.md5(str(h).encode())
	h = h.hexdigest()
	return(h)


# Le dictionnaire (JSON) contenant la liste des noeuds
nodes = [
	{
	'id': 1,
	'designation': 'node_1',
	'ip': '92.168.0.1',
	'port': '5435',
	'public_key': ''
	},
	{
	'id': 2,
	'designation': 'node_2',
	'ip': '92.168.0.1',
	'port': '5435',
	'public_key': ''

	},
	{
	'id': 3,
	'designation': 'node_3',
	'ip': '92.168.0.1',
	'port': '5435',
	'public_key': ''
	},
	{
	'id': 4,
	'designation': 'node_4',
	'ip': '92.168.0.1',
	'port': '5435' ,
	'public_key': ''
	},
	{
	'id': 5,
	'designation': 'node_5',
	'ip': '92.168.0.1',
	'port': '5435',
	'public_key': ''
	},
	{
	'id': 6,
	'designation': 'node_6',
	'ip': '92.168.0.1',
	'port': '5435',
	'public_key': ''
	},
	{
	'id': 7,
	'designation': 'node_7',
	'ip': '92.168.0.1',
	'port': '5435',
	'public_key': ''
	},
	{
	'id': 8,
	'designation': 'node_8',
	'ip': '34.168.0.1',
	'port': '5435',
	'public_key': ''
	}
	]

# Ajout de clé publique dans chaque noeud
for item in nodes:
	item['public_key'] = generate_hash()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

#-------------------------------------------------------------------------------------------------------------------------

# GET Method ----------------------------

@app.route('/nodes/api/v1.0/nodes/<int:node_id>', methods=['GET'])
def get_node(node_id):
    node = [node for node in nodes if node['id'] == node_id]
    if len(node) == 0:
        abort(404)
    return jsonify({'node': node[0]})


@app.route('/nodes/api/v1.0/nodes', methods=['GET'])
def get_nodes():
    return jsonify({'nodes': [make_public_node(node) for node in nodes]})


# POST Method ----------------------------


@app.route('/nodes/api/v1.0/nodes', methods=['POST'])
def create_node():
    if not request.json or not 'designation' in request.json:
        abort(400)

    node = {
        'id': nodes[-1]['id'] + 1,  # ID of previous node + 1
        'designation': request.json['designation'],
        'ip': request.json['ip'],
        'port': request.json['port'],

        }
    nodes.append(node)
    return jsonify({'node': node}), 201

# PUT Method

@app.route('/nodes/api/v1.0/nodes/<int:node_id>', methods=['PUT'])
def update_node(node_id):
    node = [node for node in nodes if node['id'] == node_id]
    if len(node) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'designation' in request.json and type(request.json['designation']) != str:
        abort(400)
    if 'ip' in request.json and type(request.json['ip']) != str:
        abort(400)

    node[0]['designation'] = request.json.get('designation', node[0]['designation'])
    node[0]['ip'] = request.json.get('ip', node[0]['ip'])


    return jsonify({'node': node[0]})


# Delete Method

@app.route('/nodes/api/v1.0/nodes/<int:node_id>', methods=['DELETE'])
def delete_node(node_id):
    node = [node for node in nodes if node['id'] == node_id]
    if len(node) == 0:
        abort(404)
    nodes.remove(node[0])
    return jsonify({'result': True})


#-------------------------------------------------------------------------------------------------------------------------

# Nos pages HTML


@app.route('/', methods=['GET', 'POST'])
def network():

	for item in nodes:
		item['public_key'] = generate_hash()



	return render_template('network.html', nodes=nodes)



# ---

def make_public_node(node):
    new_node = {}
    for field in node:
        if field == 'id':
            new_node['uri'] = url_for('get_node', node_id=node['id'], _external=True)
        else:
            new_node[field] = node[field]
    return new_node

if __name__ == '__main__':
    app.run(debug=True)
