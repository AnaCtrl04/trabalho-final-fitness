# FitPlatform API — Trabalho Final Cloud Computing

## Aluno
Ana Martins — ana.martins@unidavi.edu.br

## Tema
Plataforma de Treinos e Exercicios Online

## Descricao
API REST desenvolvida com Python + Flask para gerenciamento de treinos.
Implementa pipeline de Integracao Continua com GitHub Actions.

## Tecnologias
- Python 3.11 + Flask 3.0
- pytest + pytest-flask (testes unitarios)
- flake8 (analise estatica)
- GitHub Actions (CI)

## Estrutura
```
trabalho-final-fitness/
├── api/
│   ├── app.py
│   ├── data/treinos.json
│   └── tests/test_api.py
├── .github/workflows/ci.yml
├── requirements.txt
└── README.md
```

## Como Executar Localmente
```bash
# 1. Clonar o repositorio
git clone https://github.com/SEU_USUARIO/trabalho-final-fitness.git
cd trabalho-final-fitness

# 2. Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Rodar a API
cd api && python app.py
```

## Rotas da API
| Rota | Metodo | Descricao |
|------|--------|-----------|
| /status | GET | Saude da aplicacao |
| /treinos | GET | Lista todos os treinos |
| /treinos/{id} | GET | Busca treino por ID |

## Como Rodar os Testes
```bash
pytest api/tests/ -v
```

## Pipeline CI
Cada push na branch main aciona automaticamente:
1. Lint com flake8
2. Execucao dos 4 testes unitarios
