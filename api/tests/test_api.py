import sys
import os
import pytest

# Adicionar o diretório da API ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app import app


@pytest.fixture
def cliente():
    """Cria um cliente de teste para a API Flask"""
    app.config['TESTING'] = True
    with app.test_client() as cliente:
        yield cliente


# Teste 1 (OBRIGATORIO): HTTP 200 para GET /treinos
def test_listar_treinos_retorna_200(cliente):
    """Verifica se a rota GET /treinos retorna status 200"""
    resposta = cliente.get('/treinos')
    assert resposta.status_code == 200


# Teste 2 (OBRIGATORIO): Validacao da estrutura JSON
def test_estrutura_json_treinos(cliente):
    """Verifica se o JSON retornado tem os campos obrigatorios"""
    resposta = cliente.get('/treinos')
    dados = resposta.get_json()
    assert 'sucesso' in dados
    assert 'total' in dados
    assert 'treinos' in dados
    assert dados['sucesso'] is True
    assert dados['total'] == 10
    # Verificar campos de cada treino
    primeiro = dados['treinos'][0]
    assert 'id' in primeiro
    assert 'nome' in primeiro
    assert 'nivel' in primeiro
    assert 'duracao_minutos' in primeiro
    assert 'calorias' in primeiro


# Teste 3 (OBRIGATORIO): HTTP 404 para ID inexistente
def test_buscar_treino_inexistente_retorna_404(cliente):
    """Verifica se buscar ID inexistente retorna 404"""
    resposta = cliente.get('/treinos/9999')
    assert resposta.status_code == 404
    dados = resposta.get_json()
    assert dados['sucesso'] is False
    assert 'erro' in dados


# Teste 4 (AUTORIA PROPRIA): Verificar rota /status
# Justificativa: A rota /status e critica para monitoramento em producao.
# Em ambientes cloud, healthchecks automaticos consultam essa rota para
# verificar se a aplicacao esta saudavel antes de rotear trafego.
def test_status_retorna_informacoes_corretas(cliente):
    """Verifica se /status retorna as informacoes corretas da API"""
    resposta = cliente.get('/status')
    assert resposta.status_code == 200
    dados = resposta.get_json()
    assert 'nome' in dados
    assert 'versao' in dados
    assert 'status' in dados
    assert dados['status'] == 'online'
    assert dados['nome'] == 'FitPlatform API'
