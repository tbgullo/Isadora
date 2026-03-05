import streamlit as st
import base64
import streamlit.components.v1 as components

# Configuração da página
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

# Controle de estado
if "page" not in st.session_state:
    st.session_state.page = "home"

# -----------------------------
# CSS GLOBAL E ESTILIZAÇÃO
# -----------------------------
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .main {
        background-color: #fff0f5;
    }
    
    /* Estilo dos botões nativos do Streamlit */
    .stButton > button {
        background-color: #ff4d6d !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 12px 28px !important;
        font-size: 18px !important;
        border: none !important;
        display: block;
        margin: 0 auto;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background-color: #e63950 !important;
        transform: scale(1.05);
    }

    /* Animação das fotos no sentido horário */
    @keyframes moveClockwise {
        0%   { top: 20px; left: 20px; }
        25%  { top: 20px; left: calc(100vw - 170px); }
        50%  { top: calc(100vh - 170px); left: calc(100vw - 170px); }
        75%  { top: calc(100vh - 170px); left: 20px; }
        100% { top: 20px; left: 20px; }
    }

    .moving-img {
        position: fixed;
        width: 150px;
        z-index: 999;
        border-radius: 15px;
        border: 3px solid #ff4d6d;
        animation: moveClockwise 12s linear infinite;
    }

    /* Diferentes delays para as imagens não ficarem uma em cima da outra */
    .img-1 { animation-delay: 0s; }
    .img-2 { animation-delay: -3s; }
    .img-3 { animation-delay: -6s; }
    .img-4 { animation-delay: -9s; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# TELA INICIAL
# -----------------------------
if st.session_state.page == "home":
    
    st.markdown(f"""
        <div style="text-align: center; padding-top: 50px;">
            <img src="data:image/jpg;base64,{img_home}" width="300" style="border-radius: 20px; box-shadow: 0px 4px 15px rgba(0,0,0,0.1);">
            <h2 style="color: #ff4d6d; font-family: Arial;">Aceitas sair comigo na Sexta para uma noite especial? 💖</h2>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        if st.button("Sim 💘"):
            st.session_state.page = "sim"
            st.rerun()

    # Componente HTML para o botão "Não" fugitivo
    html_nao = f"""
    <html>
    <head>
    <style>
        .btn-nao {{
            background-color: #ff4d6d;
            color: white;
            padding: 12px 28px;
            font-size: 18px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
            position: fixed;
            z-index: 1000;
            font-family: Arial;
            transition: 0.1s;
        }}
    </style>
    </head>
    <body>
        <button id="nao" class="btn-nao" style="top: 70%; left: 50%; transform: translateX(-50%);">Não 😢</button>

        <script>
            const btnNao = document.getElementById("nao");
            
            btnNao.addEventListener("mouseover", () => {{
                // Calcula limites para o botão não sair da tela (viewport)
                const padding = 20;
                const maxX = window.innerWidth - btnNao.offsetWidth - padding;
                const maxY = window.innerHeight - btnNao.offsetHeight - padding;

                const newX = Math.max(padding, Math.random() * maxX);
                const newY = Math.max(padding, Math.random() * maxY);

                btnNao.style.left = newX + "px";
                btnNao.style.top = newY + "px";
                btnNao.style.transform = "none"; // Remove a centralização inicial após o primeiro movimento
            }});
        </script>
    </body>
    </html>
    """
    components.html(html_nao, height=500)

# -----------------------------
# TELA DO SIM
# -----------------------------
elif st.session_state.page == "sim":
    
    st.markdown(f"""
        <div style="text-align: center; padding-top: 50px; margin-bottom: 20px;">
            <img src="data:image/jpg;base64,{img_sim}" width="400" style="border-radius: 20px;">
            <h1 style="color: #ff4d6d;">Uma noite especial está por vir ✨</h1>
            <h3 style="color: #333;">Porque ao seu lado qualquer sexta vira mágica ❤️</h3>
        </div>
    """, unsafe_allow_html=True)

    # Botão voltar centralizado
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        if st.button("Voltar"):
            st.session_state.page = "home"
            st.rerun()

    # Imagens animadas em sentido horário
    st.markdown(f"""
        <img src="data:image/jpg;base64,{img1}" class="moving-img img-1">
        <img src="data:image/jpg;base64,{img2}" class="moving-img img-2">
        <img src="data:image/jpg;base64,{img3}" class="moving-img img-3">
        <img src="data:image/jpg;base64,{img4}" class="moving-img img-4">
    """, unsafe_allow_html=True)