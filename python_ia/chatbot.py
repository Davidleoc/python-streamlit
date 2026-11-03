# Titulo
# Campo de mensagem (input)
# Quando o usuário enviar a mensagem
    # Mostrar a mensagem na conversa
    # Mandar a mensagem para a IA responder
    # mostrar a resposta da IA na conversa

# Para rodar o chatbot: python -m streamlit run chatbot.py

import streamlit as st
from openai import APIConnectionError, APIError, APITimeoutError, OpenAI

st.set_page_config(page_title="Chatbot IA", page_icon="🤖") # Configurações da página do Streamlit

MODELO = "gemini-flash-lite-latest"
ROLE_USER = "user"           
ROLE_ASSISTANT = "assistant"

MAX_HISTORICO = 50                   # últimas N mensagens enviadas à API
SYSTEM_PROMPT = {"role": "system", "content": "Você é um assistente objetivo."}

@st.cache_resource
def get_client() -> OpenAI:
    return OpenAI(
        api_key=st.secrets["GEMINI_API_KEY"], # Chave de API do Gemini
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        timeout=30,
    )

# Criando uma lista de mensagens para armazenar as mensagens do usuário e da IA
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# TOAST: exibido após o rerun do botão "Limpar"
if st.session_state.pop("conversa_limpa", False):
    st.toast("Conversa limpa.", icon="🗑️")

st.title("🤖 Chatbot de IA")
st.caption("Respostas geradas por IA podem conter erros.")

mensagem_usuario = st.chat_input("Digite sua mensagem aqui...")

if not st.session_state["lista_mensagens"] and not mensagem_usuario:
    st.info("Envie uma mensagem para começar a conversa.", icon="💬")

for mensgem in st.session_state["lista_mensagens"]:
    qm_enviou = mensgem["role"]
    txt_messagem = mensgem["content"]
    st.chat_message(mensgem["role"]).write(mensgem["content"]) # Mostra a mensagem na conversa

if mensagem_usuario: # Verifica se tem algo dentro da variavel
    st.chat_message(ROLE_USER).write(mensagem_usuario) # Mostra a mensagem do usuário na conversa
    mensagem1 = {"role": ROLE_USER, "content": mensagem_usuario}
    historico = st.session_state["lista_mensagens"] + [mensagem1]


    try:
        # === ST.SPINNER: enquanto aguarda o início da resposta ===
        with st.spinner("Pensando..."):
            stream = get_client().chat.completions.create(
                model=MODELO,
                messages=[SYSTEM_PROMPT] + historico[-MAX_HISTORICO:],
                stream=True,
            )

        # === ST.WRITE_STREAM: resposta em tempo real ===
        with st.chat_message(ROLE_ASSISTANT):
            resposta_ia = st.write_stream(stream)

    # === ST.ERROR / ST.WARNING: erros amigáveis ===
    except KeyError:
        st.error("GEMINI_API_KEY não encontrada em .streamlit/secrets.toml.")
        st.stop()
    except APITimeoutError:
        st.warning("A IA demorou demais para responder. Tente novamente.")
        st.stop()
    except APIConnectionError:
        st.error("Falha de conexão com a API. Verifique rede ou proxy.")
        st.stop()
    except APIError as e:
        st.error(f"Erro na API: {e}")
        st.stop()

    if not resposta_ia: 
        st.warning("O modelo retornou uma resposta vazia.")
        st.stop()
    # Grava o turno completo só após sucesso.
    mensagem2 = {"role": ROLE_ASSISTANT, "content": resposta_ia}
    st.session_state["lista_mensagens"] = historico + [mensagem2]

# ST.SIDEBAR: no final do script, para o contador já incluir o turno atual
with st.sidebar:
    st.header("⚙️ Configurações")
    st.caption(f"Modelo: `{MODELO}`")
    st.caption(f"Mensagens na conversa: {len(st.session_state['lista_mensagens'])}")
    st.caption(f"Histórico enviado à API: últimas {MAX_HISTORICO}")

    if st.button("🗑️ Limpar conversa"):
        st.session_state["lista_mensagens"] = []
        st.session_state["conversa_limpa"] = True  # sinaliza o toast após o rerun
        st.rerun()
