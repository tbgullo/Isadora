import streamlit as st
import base64
import streamlit.components.v1 as components

# Configuração da página - Essencial para remover margens padrão
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
# CSS PARA TRAVAR A TELA E ANIMAR
# -----------------------------
st.markdown(f"""
<style>
    /* Remove header, footer e trava o scroll completamente */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    /* Trava o Streamlit para não permitir rolagem em nenhuma circunstância */
    html, body, [data-testid="stAppViewContainer"] {{
        overflow: hidden !important;
        height: 100vh !important;
        margin: 0;
        padding: 0;
        background-color: #fff0f5;
    }}

    .stApp {{
        height: 100vh;
        overflow: hidden;
    }}

    /* Estilo do botão Sim (Nativo) */
    .stButton > button {{
        background-color: #ff4d6d !important;
        color: white !important;
        border-radius: 12px !important;
        padding: 15px 35px !important;
        font-size: 20px !important;
        border: none !important;
        display: block;
        margin: 30px auto 0 auto !important; /* Margem maior no topo para descer o botão */
        transition: 0.4s;
        box-shadow: 0px 4px 10px rgba(255, 77, 109, 0.3);
    }}
    
    .stButton > button:hover {{
        background-color: #e63950 !important;
        transform: scale(1.1);
    }}

    /* Animação das fotos orbitando a tela (Sentido Horário) */
    @keyframes orbit {{
        0%   {{ top: 15px; left: 15px; }}
        25%  {{ top: 15px; left: calc(100vw - 95px); }}
        50%  {{ top: calc(100vh - 95px); left: calc(100vw - 95px); }}
        75%  {{ top: calc(100vh - 95px); left: 15px; }}
        100% {{ top: 15px; left: 15px; }}
    }}

    .moving-img {{
        position: fixed;
        width: 80px; /* Tamanho reduzido como solicitado */
        z-index: 9999;
        border-radius: 50%; /* Deixa as fotos redondinhas para um visual mais delicado */
        border: 3px solid #ff4d6d;
        animation: orbit 30s linear infinite; /* Velocidade bem reduzida */
    }}

    /* Delay para distribuir as fotos nos 4 cantos */
    .img-1 {{ animation-delay: 0s; }}
    .img-2 {{ animation-delay: -7.5s; }}
    .img-3 {{ animation-delay: -15s; }}
    .img-4 {{ animation-delay: -22.5s; }}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# TELA INICIAL
# -----------------------------
if st.session_state.page == "home":
    
    # Container centralizado
    st.markdown(f"""
        <div style="text-align: center; margin-top: 8vh;">
            <img src="data:image/jpg;base64,{img_home}" width="280" style="border-radius: 30px; box-shadow: 0px 10px 30px rgba(0,0,0,0.1);">
            <h1 style="color: #ff4d6d; font-family: 'Segoe UI', Arial; margin-top: 20px;">Aceitas sair comigo na Sexta? 💖</h1>
        </div>
    """, unsafe_allow_html=True)

    # Botão Sim (Posicionado mais abaixo via CSS margin-top)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        if st.button("Sim 💘"):
            st.session_state.page = "sim"
            st.rerun()

    # Botão "Não" (Iframe separado para não quebrar o layout)
    html_nao = f"""
    <style>
        .btn-nao {{
            background-color: #ff4d6d; color: white; padding: 12px 28px;
            font-size: 18px; border-radius: 10px; border: none;
            cursor: pointer; position: fixed; z-index: 10000; font-family: Arial;
        }}
    </style>
    <button id="nao" class="btn-nao" style="top: 75%; left: 50%; transform: translateX(-50%);">Não 😢</button>
    <script>
        const btn = document.getElementById("nao");
        btn.addEventListener("mouseover", () => {{
            const x = Math.random() * (window.innerWidth - 120);
            const y = Math.random() * (window.innerHeight - 60);
            btn.style.left = x + "px";
            btn.style.top = y + "px";
            btn.style.transform = "none";
        }});
    </script>
    """
    components.html(html_nao, height=300)

# -----------------------------
# TELA DO SIM
# -----------------------------
elif st.session_state.page == "sim":
    
    st.markdown(f"""
        <div style="text-align: center; margin-top: 10vh;">
            <img src="data:image/jpg;base64,{img_sim}" width="380" style="border-radius: 30px;">
            <h1 style="color: #ff4d6d; margin-top: 20px;">Uma noite especial está por vir! ✨</h1>
            <h3 style="color: #444;">Mal posso esperar para te ver ❤️</h3>
        </div>
    """, unsafe_allow_html=True)

    # Botão Voltar Centralizado
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        st.write("<br>", unsafe_allow_html=True)
        if st.button("Voltar"):
            st.session_state.page = "home"
            st.rerun()

    # Imagens Orbitando (Fixas na tela inicial do dispositivo)
    st.markdown(f"""
        <img src="data:image/jpg;base64,{img1}" class="moving-img img-1">
        <img src="data:image/jpg;base64,{img2}" class="moving-img img-2">
        <img src="data:image/jpg;base64,{img3}" class="moving-img img-3">
        <img src="data:image/jpg;base64,{img4}" class="moving-img img-4">
    """, unsafe_allow_html=True)