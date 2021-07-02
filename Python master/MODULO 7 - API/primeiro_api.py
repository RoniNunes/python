from flask import Flask, jsonify, request

app = Flask(__name__)

postagens = [
    {
        'titulo': 'Api com Flask',
        'autor': 'Roni nunes'
    },
    {
        'titulo': 'Voce ja usou o Selenium?',
        'autor': 'Roni nunes'
    },
    {
        'titulo': 'Como instalar o python',
        'autor': 'Roni nunes'
    }
]

nova_postagem = [
    {
        'titulo': 'Nova postagem com Flask',
        'autor': 'Roni nunes'
    }]

@app.route('/postagens', methods=['GET'])
def obter_todas_postagens():
    return jsonify(postagens)

@app.route('/postagens/<int:postagem_id>', methods=['GET'])
def obter_postagens_por_id(postagem_id): #Passamos o ID que queremos consultar.
    return jsonify(postagens[postagem_id])

@app.route('/postagens', methods=['POST'])
def nova_postagem():
    postagem = request.get_json()
    postagens.append(postagem)
    return jsonify({'mensagem': 'Recurso criado com sucesso'}), 200

@app.route('/postagens/<int:postagem_id>', methods=['PUT'])
def atualizar_postagem(postagem_id):#Passamos o ID que queremos consultar.
    resultado = request.get_json()
    postagens[postagem_id].update(resultado)
    return jsonify(postagens[postagem_id]), 200

@app.route('/postagens/<int:postagem_id>', methods=['DELETE'])   
def excluir_postagem(postagem_id):#Passamos o ID que queremos consultar.
    postagem = postagens[postagem_id]
    del postagens[postagem_id]
    return jsonify({'mensagem': 'A postagem foi excluida com sucesso'})


if __name__ == '__main__':
    app.run(port=5000, host='localhost',debug=True)