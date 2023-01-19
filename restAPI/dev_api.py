from flask import Flask, jsonify, request
import json

app =  Flask(__name__)

devs = [
    {'nome': 'Lua',
     'profissao': 'Analista de seguranca de aplicacoes',
     'lingaguens': ['Python', 'Java']
     },
    {'nome': 'Sol',
     'profissao': 'Desenvolvedora',
     'lingaguens': ['Python', 'Java']
     }
]

@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = devs[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(desenvolvedor)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        devs[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        devs.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluído'})

@app.route('/dev/', methods=['GET', 'POST'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        devs.append(dados)
        return jsonify({'status':'sucesso', 'mensagem':'Registro inserido'})


if __name__ == "__main__":
    app.run(debug=True)
