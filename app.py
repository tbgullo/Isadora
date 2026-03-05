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
    [data-testid="stAppViewContainer"] {{
        background: linear-gradient(135deg, #fff5f7 0%, #ffe4e1 100%);
        overflow: hidden !important;
    }}
    
    .main .block-container {{
        height: 100vh;
        overflow: hidden !important;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 0;
    }}

    #MainMenu, footer, header {{visibility: hidden;}}

    h1, h2, h3 {{
        color: #d63384 !important;
        font-family: 'Segoe UI', Arial, sans-serif;
    }}

    /* Estilo dos Botões Streamlit (Sim e Voltar) */
    .stButton > button {{
        background: linear-gradient(90deg, #ff4d6d, #ff758c) !important;
        color: white !important;
        border-radius: 50px !important;
        padding: 10px 30px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        border: none !important;
        box-shadow: 0 4px 10px rgba(255, 77, 109, 0.3) !important;
        transition: 0.3s !important;
        width: 140px;
        margin: 0 auto;
    }}
    
    .stButton > button:hover {{
        transform: scale(1.05);
        box-shadow: 0 6px 15px rgba(255, 77, 109, 0.5) !important;
    }}

    /* Animação das fotos orbitando */
    @keyframes moveClockwise {{
        0%   {{ top: 20px; left: 20px; }}
        25%  {{ top: 20px; left: calc(100vw - 110px); }}
        50%  {{ top: calc(100vh - 110px); left: calc(100vw - 110px); }}
        75%  {{ top: calc(100vh - 110px); left: 20px; }}
        100% {{ top: 20px; left: 20px; }}
    }}

    .moving-img {{
        position: fixed;
        width: 85px;
        z-index: 999;
        border-radius: 50%;
        border: 3px solid white;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        animation: moveClockwise 25s linear infinite;
    }}

    .img-1 {{ animation-delay: 0s; }}
    .img-2 {{ animation-delay: -6.25s; }}
    .img-3 {{ animation-delay: -12.5s; }}
    .img-4 {{ animation-delay: -18.75s; }}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# TELA INICIAL
# -----------------------------
if st.session_state.page == "home":
    
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 20px;">
            <div style="display: inline-block; padding: 10px; background: white; border-radius: 30px; box-shadow: 0 10px 25px rgba(0,0,0,0.05);">
                <img src="data:image/jpg;base64,{img_home}" width="250" style="border-radius: 20px;">
            </div>
            <h2 style="margin-top: 20px;">Aceitas sair comigo na Sexta? 💖</h2>
        </div>
    """, unsafe_allow_html=True)

    # Criando colunas para os botões Sim e Não ficarem lado a lado
    col_vazia1, col_sim, col_nao, col_vazia2 = st.columns([2, 1, 1, 2])
    
    with col_sim:
        if st.button("Sim 💘"):
            st.session_state.page = "sim"
            st.rerun()

    with col_nao:
        # Componente HTML apenas para o botão "Não" para ele poder fugir
        html_nao = f"""
        <html>
        <body style="background:transparent; margin:0; overflow:hidden;">
            <button id="nao" style="
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
                transition: 0.1s;
                box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            ">Não 😢</button>

            <script>
                const btn = document.getElementById("nao");
                btn.addEventListener("mouseover", () => {{
                    // Define limites de fuga baseados na viewport para não sumir
                    const margin = 50;
                    const maxX = window.innerWidth - 150;
                    const maxY = window.innerHeight - 100;
                    
                    btn.style.position = "fixed";
                    btn.style.left = Math.max(margin, Math.random() * maxX) + "px";
                    btn.style.top = Math.max(margin, Math.random() * maxY) + "px";
                }});
            </script>
        </body>
        </html>
        """
        components.html(html_nao, height=50)

# -----------------------------
# TELA DO SIM
# -----------------------------
elif st.session_state.page == "sim":
    
    st.markdown(f"""
        <div style="text-align: center;">
            <div style="display: inline-block; padding: 10px; background: white; border-radius: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                <img src="data:image/jpg;base64,{img_sim}" width="350" style="border-radius: 20px;">
            </div>
            <h1 style="margin-top: 25px;">Vai ser uma noite memorável</h1>
            <h3 style="color: #666; margin-bottom: 5px;">Pra você nunca se esquecer de mim</h3>
        </div>
    """, unsafe_allow_html=True)

    # Botão Voltar logo abaixo
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
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