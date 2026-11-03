# python-streamlit

Coleção de projetos de estudo em Python: análise de dados, automação, orientação a objetos e aplicações web com Streamlit.

## Projetos

| Pasta | Tipo | Stack | Descrição |
|-------|------|-------|-----------|
| [`analise_dados_python`](analise_dados_python/) | Jupyter Notebook | pandas, plotly | Análise exploratória de cancelamento de clientes (churn) |
| [`automacao_pyautogui`](automacao_pyautogui/) | Script (RPA) | pyautogui, pandas | Cadastro automático de produtos em um sistema web a partir de um CSV |
| [`modelos_restaurantes`](modelos_restaurantes/) | Script (POO) | Python puro | Modelagem de restaurantes e avaliações com classes |
| [`python_ia`](python_ia/) | App Streamlit | streamlit, openai (API Gemini) | Chatbot com respostas em streaming |
| [`sistema_python`](sistema_python/) | App Streamlit | streamlit, pandas, plotly | Cadastro de vendas com dashboard e filtros |

Cada pasta tem um `README.md` próprio, com pré-requisitos, instruções de execução e limitações conhecidas.

## Pré-requisitos gerais

- Python 3.9 ou superior
- `pip` e `venv`
- Git

## Uso rápido

```bash
git clone https://github.com/Davidleoc/python-streamlit.git
cd python-streamlit/<projeto>

python -m venv .venv
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt
```

Depois, siga o `README.md` do projeto escolhido. Os apps Streamlit rodam com:

```bash
python -m streamlit run <arquivo>.py
```

## Estrutura

```
python-streamlit/
├── analise_dados_python/
├── automacao_pyautogui/
├── modelos_restaurantes/
├── python_ia/
├── sistema_python/
├── .gitignore
└── README.md
```

## Segurança

- **Não versione credenciais.** `.streamlit/secrets.toml`, `.env` e similares estão no `.gitignore`.
- O `python_ia` precisa de uma chave de API. Crie o arquivo `python_ia/.streamlit/secrets.toml` localmente (o README do projeto mostra como).
- Os apps Streamlit são para uso local. Não exponha a porta 8501 na rede sem autenticação.
