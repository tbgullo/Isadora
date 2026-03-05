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
    /* Trava total contra rolagem */
    html, body, [data-testid="stAppViewContainer"], .main, .block-container {{
        overflow: hidden !important;
        height: 100vh !important;
        width: 100vw !important;
        margin: 0 !important;
        padding: 0 !important;
        position: fixed !important;
    }}

    [data-testid="stAppViewContainer"] {{
        background: linear-gradient(135deg, #fff5f7 0%, #ffe4e1 100%);
    }}
    
    /* Centralização Real do Conteúdo */
    .main .block-container {{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }}

    #MainMenu, footer, header {{visibility: hidden;}}

    h1, h2, h3 {{
        color: #d63384 !important;
        font-family: 'Segoe UI', Arial, sans-serif;
        text-align: center;
    }}

    /* Estilo do Botão Sim (Streamlit) */
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
        transition: 0.3s;
        /* Removemos o translate para ele ficar no centro exato */
    }}

    /* Fotos orbitando (Tela do Sim) */
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
</style>
""", unsafe_allow_html=True)

# -----------------------------
# TELA INICIAL
# -----------------------------
if st.session_state.page == "home":
    
    # Imagem e Texto Centralizados
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 25px;">
            <div style="display: inline-block; padding: 10px; background: white; border-radius: 30px; box-shadow: 0 10px 25px rgba(0,0,0,0.05);">
                <img src="data:image/jpg;base64,{img_home}" width="220" style="border-radius: 20px;">
            </div>
            <h2 style="margin-top: 15px;">Aceitas sair comigo na Sexta? 💖</h2>
        </div>
    """, unsafe_allow_html=True)

    # Botão Sim (Centralizado pelo layout do Streamlit)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Sim 💘"):
            st.session_state.page = "sim"
            st.rerun()

    # Botão "Não" que nasce ao lado do Sim e foge por toda a tela
    html_nao_global = f"""
    <div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: 9999;">
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
            /* Posicionamento Inicial ao lado do botão Sim */
            left: calc(50% + 80px); 
            top: 72%; 
            transform: translateY(-50%);
            transition: top 0.1s ease, left 0.1s ease;
        ">Não 😢</button>
    </div>

    <script>
        const btn = document.getElementById("nao");
        
        btn.addEventListener("mouseover", () => {{
            const winW = window.innerWidth;
            const winH = window.innerHeight;
            const btnW = 140;
            const btnH = 45;

            // Gera posição aleatória na tela toda
            let newX = Math.random() * (winW - btnW - 40) + 20;
            let newY = Math.random() * (winH - btnH - 40) + 20;

            // Evita parar em cima da imagem central
            if (newX > winW * 0.3 && newX < winW * 0.7 && newY > winH * 0.3 && newY < winH * 0.7) {{
                newX = newX < winW * 0.5 ? 50 : winW - btnW - 50;
                newY = newY < winH * 0.5 ? 50 : winH - btnH - 50;
            }}

            btn.style.left = newX + "px";
            btn.style.top = newY + "px";
        }});
    </script>
    """
    components.html(html_nao_global, height=0)

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
            <h3 style="color: #666;">Para você nunca se esquecer de mim ❤️</h3>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Voltar"):
            st.session_state.page = "home"
            st.rerun()

    # Imagens Orbitais
    st.markdown(f"""
        <img src="data:image/jpg;base64,{img1}" class="moving-img" style="animation-delay: 0s;">
        <img src="data:image/jpg;base64,{img2}" class="moving-img" style="animation-delay: -7.5s;">
        <img src="data:image/jpg;base64,{img3}" class="moving-img" style="animation-delay: -15s;">
        <img src="data:image/jpg;base64,{img4}" class="moving-img" style="animation-delay: -22.5s;">
    """, unsafe_allow_html=True)