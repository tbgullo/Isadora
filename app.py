import streamlit as st
import base64
import streamlit.components.v1 as components

# Configuração da página para evitar margens laterais
st.set_page_config(layout="wide", page_title="Convite Especial")

# -----------------------------
# Função para converter imagem
# -----------------------------
def get_base64_image(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

# Carregando imagens
img_home = get_base64_image("Image.jpg")
img_sim = get_base64_image("ImageSim.jpg")
img1 = get_base64_image("Image1.jpg")
img2 = get_base64_image("Image2.jpg")
img3 = get_base64_image("Image3.jpg")
img4 = get_base64_image("Image4.jpg")

if "page" not in st.session_state:
    st.session_state.page = "home"

# -----------------------------
# CSS PARA FIXAR O TAMANHO DA TELA (VIEWPORT)
# -----------------------------
st.markdown("""
<style>
    /* Esconde elementos padrão do Streamlit e trava o scroll */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Força a página a ocupar exatamente o tamanho da tela do dispositivo */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 0rem;
        height: 100vh;
        overflow: hidden;
    }

    body {
        overflow: hidden;
        background-color: #fff0f5;
    }

    /* Estilo dos botões nativos */
    .stButton > button {
        background-color: #ff4d6d !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 10px 25px !important;
        font-size: 18px !important;
        border: none !important;
        display: block;
        margin: 0 auto;
        transition: 0.3s;
    }

    /* Animação das fotos (Sentido Horário Suave) */
    @keyframes moveClockwise {
        0%   { top: 10px; left: 10px; }
        25%  { top: 10px; left: calc(100vw - 110px); }
        50%  { top: calc(100vh - 110px); left: calc(100vw - 110px); }
        75%  { top: calc(100vh - 110px); left: 10px; }
        100% { top: 10px; left: 10px; }
    }

    .moving-img {
        position: fixed;
        width: 100px; /* Tamanho reduzido */
        z-index: 999;
        border-radius: 12px;
        border: 2px solid #ff4d6d;
        animation: moveClockwise 25s linear infinite; /* Velocidade menor */
    }

    .img-1 { animation-delay: 0s; }
    .img-2 { animation-delay: -6.25s; }
    .img-3 { animation-delay: -12.5s; }
    .img-4 { animation-delay: -18.75s; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# TELA INICIAL
# -----------------------------
if st.session_state.page == "home":
    
    st.markdown(f"""
        <div style="text-align: center; height: 40vh; display: flex; flex-direction: column; justify-content: center; align-items: center;">
            <img src="data:image/jpg;base64,{img_home}" width="250" style="border-radius: 20px; box-shadow: 0px 4px 15px rgba(0,0,0,0.1);">
            <h2 style="color: #ff4d6d; font-family: Arial; margin-top: 20px;">Aceitas sair comigo na Sexta? 💖</h2>
        </div>
    """, unsafe_allow_html=True)

    # Botão Sim Centralizado
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        if st.button("Sim 💘"):
            st.session_state.page = "sim"
            st.rerun()

    # Botão "Não" que foge dentro da tela visível
    html_nao = f"""
    <html>
    <head>
    <style>
        .btn-nao {{
            background-color: #ff4d6d;
            color: white;
            padding: 10px 25px;
            font-size: 18px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
            position: fixed;
            z-index: 1000;
            font-family: Arial;
        }}
    </style>
    </head>
    <body>
        <button id="nao" class="btn-nao" style="top: 65%; left: 50%; transform: translateX(-50%);">Não 😢</button>

        <script>
            const btnNao = document.getElementById("nao");
            
            btnNao.addEventListener("mouseover", () => {{
                // Usa window.innerWidth/Height para garantir o limite da tela atual
                const margin = 30;
                const maxX = window.innerWidth - btnNao.offsetWidth - margin;
                const maxY = window.innerHeight - btnNao.offsetHeight - margin;

                const newX = Math.max(margin, Math.random() * maxX);
                const newY = Math.max(margin, Math.random() * maxY);

                btnNao.style.left = newX + "px";
                btnNao.style.top = newY + "px";
                btnNao.style.transform = "none";
            }});
        </script>
    </body>
    </html>
    """
    components.html(html_nao, height=200) # Componente menor para não criar scroll

# -----------------------------
# TELA DO SIM
# -----------------------------
elif st.session_state.page == "sim":
    
    st.markdown(f"""
        <div style="text-align: center; padding-top: 5vh;">
            <img src="data:image/jpg;base64,{img_sim}" width="350" style="border-radius: 20px;">
            <h1 style="color: #ff4d6d;">Vai ser uma noite cheia de surpresas! ✨</h1>
            <h3 style="color: #333;">Para você não se esquecer da gente</h3>
        </div>
    """, unsafe_allow_html=True)

    # Botão Voltar centralizado
    st.write("") # Espaçamento
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        if st.button("Voltar"):
            st.session_state.page = "home"
            st.rerun()

    # Imagens rodando sincronizadas com o tamanho da tela
    st.markdown(f"""
        <img src="data:image/jpg;base64,{img1}" class="moving-img img-1">
        <img src="data:image/jpg;base64,{img2}" class="moving-img img-2">
        <img src="data:image/jpg;base64,{img3}" class="moving-img img-3">
        <img src="data:image/jpg;base64,{img4}" class="moving-img img-4">
    """, unsafe_allow_html=True)