import json
import os
from flask import Flask, jsonify

app = Flask(__name__)


# Carregar dados do arquivo JSON externo
def carregar_treinos():
    caminho = os.path.join(os.path.dirname(__file__), 'data', 'treinos.json')
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)['treinos']


# Rota 1: GET /status — saude da aplicacao
@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        'nome': 'FitPlatform API',
        'versao': '1.0.0',
        'status': 'online',
        'tema': 'Plataforma de Treinos e Exercicios Online',
        'autor': 'Ana Martins'
    }), 200


# Rota 2: GET /treinos — lista todos os treinos
@app.route('/treinos', methods=['GET'])
def listar_treinos():
    try:
        treinos = carregar_treinos()
        return jsonify({
            'sucesso': True,
            'total': len(treinos),
            'treinos': treinos
        }), 200
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'erro': str(e)
        }), 500


# Rota 3: GET /treinos/<id> — busca treino por ID
@app.route('/treinos/<int:treino_id>', methods=['GET'])
def buscar_treino(treino_id):
    try:
        treinos = carregar_treinos()
        treino = next((t for t in treinos if t['id'] == treino_id), None)
        if treino is None:
            return jsonify({
                'sucesso': False,
                'erro': f'Treino com id {treino_id} nao encontrado'
            }), 404
        return jsonify({
            'sucesso': True,
            'treino': treino
        }), 200
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'erro': str(e)
        }), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
