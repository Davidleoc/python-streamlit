# 💬 Chatbot de IA (Streamlit + Gemini)

Chatbot web em Streamlit que usa o modelo **Gemini** do Google pelo endpoint compatível com a API da OpenAI. As respostas aparecem em streaming.

## Funcionalidades

- Histórico da conversa na sessão (`st.session_state`)
- Resposta em tempo real (`st.write_stream`)
- Envio apenas das últimas 50 mensagens à API (`MAX_HISTORICO`)
- Mensagens de erro amigáveis para timeout, falha de conexão, erro de API e chave ausente
- Sidebar com modelo, contador de mensagens e botão **Limpar conversa**

## Pré-requisitos

| Item | Observação |
|------|------------|
| Python | 3.9 ou superior |
| Streamlit | Versão recente, com `st.write_stream` (1.31 ou superior) |
| openai | SDK v1 ou superior |
| Chave de API | Gemini API key, gerada no Google AI Studio |

## Instalação

```bash
cd python_ia
python -m venv .venv
.\.venv\Scripts\Activate.ps1      # Windows
# source .venv/bin/activate      # Linux / macOS
pip install -r requirements.txt
```

## Configuração da chave

Crie o arquivo `python_ia/.streamlit/secrets.toml`:

```toml
GEMINI_API_KEY = "sua-chave-aqui"
```

> ⚠️ Esse arquivo está no `.gitignore` e **não deve ser versionado**. Se uma chave for publicada por engano, revogue-a no Google AI Studio e gere outra.

## Execução

```bash
python -m streamlit run chatbot.py
```

Acesse: <http://localhost:8501>

> Execute o comando **de dentro da pasta `python_ia`**. O Streamlit procura `.streamlit/secrets.toml` no diretório atual.

## Configuração (`chatbot.py`)

| Constante | Padrão | Descrição |
|-----------|--------|-----------|
| `MODELO` | `gemini-flash-lite-latest` | Modelo usado |
| `MAX_HISTORICO` | `50` | Mensagens enviadas como contexto |
| `SYSTEM_PROMPT` | "Você é um assistente objetivo." | Instrução de sistema |
| `timeout` | `30` s | Timeout das chamadas à API |

## Troubleshooting

| Sintoma | Causa provável | Ação |
|---------|----------------|------|
| "GEMINI_API_KEY não encontrada" | `secrets.toml` ausente ou fora do diretório de execução | Crie o arquivo e rode o comando de dentro de `python_ia` |
| "Falha de conexão com a API" | Rede ou proxy corporativo | Teste o acesso a `generativelanguage.googleapis.com` e configure `HTTPS_PROXY` |
| `Erro na API: 401/403` | Chave inválida ou revogada | Gere outra chave |
| `Erro na API: 429` | Cota excedida | Aguarde ou revise a cota no Google AI Studio |
| `AttributeError: write_stream` | Streamlit antigo | `pip install --upgrade streamlit` |

## Limitações

- O histórico fica só na memória da sessão e se perde ao recarregar a página.
- Não há autenticação. Use só localmente.
