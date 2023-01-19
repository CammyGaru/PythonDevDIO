from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/<int:id>')
def pessoas(id):
    soma = 1 + id
    return jsonify({"id": id, "Nome": "Camily", "Profissao": "Analista de seguranca de aplicacoes"})

@app.route('/soma', methods=['POST'])
def soma():
    dados = json.loads(request.data)
    total = sum(dados['valores'])
    return jsonify({'soma': total})

#@app.route('/soma/<int:valor1>/<int:valor2>/')
#def soma(valor1, valor2):
#    return jsonify({'soma': valor1 + valor2})

if __name__ == "__main__":
    app.run(debug=True)
