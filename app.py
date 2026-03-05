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
# CSS ESTILIZADO E TRAVA DE ROLAGEM
# -----------------------------
st.markdown(f"""
<style>
    /* Trava total contra rolagem e fixa o viewport */
    html, body, [data-testid="stAppViewContainer"], .main {{
        overflow: hidden !important;
        height: 100vh !important;
        width: 100vw !important;
        position: fixed;
        margin: 0;
        padding: 0;
    }}

    [data-testid="stAppViewContainer"] {{
        background: linear-gradient(135deg, #fff5f7 0%, #ffe4e1 100%);
    }}
    
    .main .block-container {{
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 0 !important;
        max-width: 100%;
    }}

    #MainMenu, footer, header {{visibility: hidden;}}

    h1, h2, h3 {{
        color: #d63384 !important;
        font-family: 'Segoe UI', Arial, sans-serif;
        text-align: center;
    }}

    /* Botões Sim e Voltar */
    .stButton > button {{
        background: linear-gradient(90deg, #ff4d6d, #ff758c) !important;
        color: white !important;
        border-radius: 50px !important;
        padding: 10px 30px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        border: none !important;
        box-shadow: 0 4px 10px rgba(255, 77, 109, 0.3) !important;
        width: 140px;
        display: block;
        margin: 0 auto;
    }}

    /* Animação das fotos orbitando */
    @keyframes moveClockwise {{
        0%   {{ top: 15px; left: 15px; }}
        25%  {{ top: 15px; left: calc(100vw - 100px); }}
        50%  {{ top: calc(100vh - 100px); left: calc(100vw - 100px); }}
        75%  {{ top: calc(100vh - 100px); left: 15px; }}
        100% {{ top: 15px; left: 15px; }}
    }}

    .moving-img {{
        position: fixed;
        width: 80px;
        z-index: 99;
        border-radius: 50%;
        border: 3px solid white;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
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
    
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 20px;">
            <div style="display: inline-block; padding: 10px; background: white; border-radius: 30px; box-shadow: 0 10px 25px rgba(0,0,0,0.05);">
                <img src="data:image/jpg;base64,{img_home}" width="220" style="border-radius: 20px;">
            </div>
            <h2 style="margin-top: 15px;">Aceitas sair comigo na Sexta? 💖</h2>
        </div>
    """, unsafe_allow_html=True)

    # Colunas apenas para centralizar o Sim (o Não será injetado via HTML global)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Sim 💘"):
            st.session_state.page = "sim"
            st.rerun()

    # Injeção do botão "Não" de forma GLOBAL na página
    html_nao_global = f"""
    <div id="container-nao" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: 9999;">
        <button id="nao" style="
            pointer-events: auto;
            background-color: #ffb6c1;
            color: white;
            padding: 10px 0;
            width: 140px;
            font-size: 18px;
            border-radius: 50px;
            border: 2px solid white;
            cursor: pointer;
            font-family: Arial;
            font-weight: bold;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            position: absolute;
            left: 55%; /* Começa ao lado do botão sim */
            top: 70%; /* Alinhado verticalmente com o botão sim */
            transform: translateX(20px);
            transition: 0.1s ease;
        ">Não 😢</button>
    </div>

    <script>
        const btn = document.getElementById("nao");
        
        btn.addEventListener("mouseover", () => {{
            const winW = window.innerWidth;
            const winH = window.innerHeight;
            
            // Define o tamanho do botão para não vazar
            const btnW = 140;
            const btnH = 45;

            // Gera posições aleatórias dentro de TODA a tela
            let newX = Math.random() * (winW - btnW - 20);
            let newY = Math.random() * (winH - btnH - 20);

            // Evita que ele fique exatamente no meio (onde está o Sim e a Imagem)
            // Se as coordenadas caírem no centro, empurramos para as bordas
            if (newX > winW * 0.3 && newX < winW * 0.7 && newY > winH * 0.3 && newY < winH * 0.7) {{
                newX = newX < winW * 0.5 ? 50 : winW - btnW - 50;
                newY = newY < winH * 0.5 ? 50 : winH - btnH - 50;
            }}

            btn.style.left = newX + "px";
            btn.style.top = newY + "px";
            btn.style.transform = "none";
        }});
    </script>
    """
    # Usamos o components.html mas com altura 0 ou ocupando a tela toda de forma invisível
    components.html(html_nao_global, height=1000)

# -----------------------------
# TELA DO SIM
# -----------------------------
elif st.session_state.page == "sim":
    
    st.markdown(f"""
        <div style="text-align: center;">
            <div style="display: inline-block; padding: 10px; background: white; border-radius: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                <img src="data:image/jpg;base64,{img_sim}" width="320" style="border-radius: 20px;">
            </div>
            <h1 style="margin-top: 20px;">Vai ser uma noite memorável! ✨</h1>
            <h3 style="color: #666; margin-bottom: 10px;">Para você nunca se esquecer de mim ❤️</h3>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Voltar"):
            st.session_state.page = "home"
            st.rerun()

    # Imagens Orbitais
    st.markdown(f"""
        <img src="data:image/jpg;base64,{img1}" class="moving-img img-1">
        <img src="data:image/jpg;base64,{img2}" class="moving-img img-2">
        <img src="data:image/jpg;base64,{img3}" class="moving-img img-3">
        <img src="data:image/jpg;base64,{img4}" class="moving-img img-4">
    """, unsafe_allow_html=True)