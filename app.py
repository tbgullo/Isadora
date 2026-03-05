import streamlit as st
import base64
import streamlit.components.v1 as components

# Configuração da página
st.set_page_config(layout="wide", page_title="Convite Especial 💖")

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
# CSS ESTILIZADO E ROMÂNTICO
# -----------------------------
st.markdown(f"""
<style>
    /* 1. Trava total do Viewport e Fundo Gradiente Romântico */
    [data-testid="stAppViewContainer"] {{
        background: linear-gradient(135deg, #fff5f7 0%, #ffe4e1 100%);
        overflow: hidden !important;
    }}
    
    .main .block-container {{
        height: 100vh;
        max-height: 100vh;
        overflow: hidden !important;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding-top: 0rem;
    }}

    #MainMenu, footer, header {{visibility: hidden;}}

    /* 2. Estilização dos Títulos */
    h1, h2, h3 {{
        color: #d63384 !important;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.05);
    }}

    /* 3. Botão SIM (Nativo do Streamlit) */
    /* Ajustando posição Y (margin-top maior) e Estética */
    .stButton > button {{
        background: linear-gradient(90deg, #ff4d6d, #ff758c) !important;
        color: white !important;
        border-radius: 50px !important;
        padding: 15px 45px !important;
        font-size: 22px !important;
        font-weight: bold !important;
        border: none !important;
        box-shadow: 0 8px 15px rgba(255, 77, 109, 0.4) !important;
        margin-top: 100px !important; /* ALTERAÇÃO DA POSIÇÃO Y */
        transition: all 0.3s ease !important;
    }}
    
    .stButton > button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 12px 20px rgba(255, 77, 109, 0.6) !important;
    }}

    /* 4. Animação das fotos orbitando */
    @keyframes moveClockwise {{
        0%   {{ top: 20px; left: 20px; }}
        25%  {{ top: 20px; left: calc(100vw - 120px); }}
        50%  {{ top: calc(100vh - 120px); left: calc(100vw - 120px); }}
        75%  {{ top: calc(100vh - 120px); left: 20px; }}
        100% {{ top: 20px; left: 20px; }}
    }}

    .moving-img {{
        position: fixed;
        width: 90px;
        z-index: 999;
        border-radius: 50%;
        border: 4px solid white;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        animation: moveClockwise 30s linear infinite;
    }}

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
    
    # Conteúdo central
    st.markdown(f"""
        <div style="text-align: center;">
            <div style="display: inline-block; padding: 10px; background: white; border-radius: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                <img src="data:image/jpg;base64,{img_home}" width="280" style="border-radius: 20px;">
            </div>
            <h1 style="margin-top: 25px; font-size: 2.5rem;">Aceitas sair comigo na Sexta? 💖</h1>
        </div>
    """, unsafe_allow_html=True)

    # Botão Sim
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        if st.button("Sim 💘"):
            st.session_state.page = "sim"
            st.rerun()

    # Botão "Não" que foge
    html_nao = f"""
    <html>
    <body style="background:transparent;">
        <button id="nao" style="
            background-color: #ff8fa3;
            color: white;
            padding: 10px 25px;
            font-size: 16px;
            border-radius: 50px;
            border: 2px solid white;
            cursor: pointer;
            position: fixed;
            z-index: 1000;
            font-family: Arial;
            font-weight: bold;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            top: 75%; left: 50%; transform: translateX(-50%);
        ">Não 😢</button>

        <script>
            const btn = document.getElementById("nao");
            btn.addEventListener("mouseover", () => {{
                const margin = 10;
                const maxX = window.innerWidth - btn.offsetWidth - margin;
                const maxY = window.innerHeight - btn.offsetHeight - margin - 50;
                btn.style.left = Math.max(margin, Math.random() * maxX) + "px";
                btn.style.top = Math.max(margin, Math.random() * maxY) + "px";
                btn.style.transform = "none";
            }});
        </script>
    </body>
    </html>
    """
    components.html(html_nao, height=200)

# -----------------------------
# TELA DO SIM
# -----------------------------
elif st.session_state.page == "sim":
    
    st.markdown(f"""
        <div style="text-align: center;">
            <div style="display: inline-block; padding: 10px; background: white; border-radius: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                <img src="data:image/jpg;base64,{img_sim}" width="380" style="border-radius: 20px;">
            </div>
            <h1 style="margin-top: 30px;">Combinado! ✨</h1>
            <h3 style="color: #666;">Prepare-se para uma noite inesquecível ❤️</h3>
        </div>
    """, unsafe_allow_html=True)

    # Botão Voltar (também seguindo o estilo mas sem o margin-top gigante)
    st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        if st.button("Voltar"):
            st.session_state.page = "home"
            st.rerun()

    # Imagens Orbitais (Sentido horário, presas à tela)
    st.markdown(f"""
        <img src="data:image/jpg;base64,{img1}" class="moving-img img-1">
        <img src="data:image/jpg;base64,{img2}" class="moving-img img-2">
        <img src="data:image/jpg;base64,{img3}" class="moving-img img-3">
        <img src="data:image/jpg;base64,{img4}" class="moving-img img-4">
    """, unsafe_allow_html=True)