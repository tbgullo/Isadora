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
# CSS GLOBAL ROMÂNTICO
# -----------------------------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

body {
    background: linear-gradient(135deg, #ffe6f0, #ffc2d1, #ff8fab);
    overflow: hidden;
}

.main .block-container {
    padding-top: 2rem;
    padding-bottom: 0rem;
    height: 100vh;
    overflow: hidden;
}

/* Botões */
.stButton > button {
    background: linear-gradient(45deg, #ff4d6d, #ff8fab) !important;
    color: white !important;
    border-radius: 30px !important;
    padding: 14px 35px !important;
    font-size: 20px !important;
    border: none !important;
    display: block;
    margin: 0 auto;
    box-shadow: 0px 6px 15px rgba(255, 77, 109, 0.4);
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.08);
    box-shadow: 0px 8px 20px rgba(255, 77, 109, 0.6);
}

/* Animação fotos */
@keyframes moveClockwise {
    0%   { top: 10px; left: 10px; }
    25%  { top: 10px; left: calc(100vw - 110px); }
    50%  { top: calc(100vh - 110px); left: calc(100vw - 110px); }
    75%  { top: calc(100vh - 110px); left: 10px; }
    100% { top: 10px; left: 10px; }
}

.moving-img {
    position: fixed;
    width: 100px;
    z-index: 999;
    border-radius: 18px;
    border: 3px solid white;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.2);
    animation: moveClockwise 25s linear infinite;
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
        <div style="text-align: center; height: 60vh; display: flex; flex-direction: column; justify-content: center; align-items: center;">
            <img src="data:image/jpg;base64,{img_home}" width="260"
                 style="border-radius: 25px; box-shadow: 0px 8px 25px rgba(0,0,0,0.2);">
            <h2 style="color: white; font-family: 'Trebuchet MS';
                       margin-top: 25px; font-size: 34px;
                       text-shadow: 2px 2px 8px rgba(0,0,0,0.3);">
                Aceitas sair comigo na Sexta? 💖
            </h2>
        </div>
    """, unsafe_allow_html=True)

    # Botão Sim mais abaixo
    st.write("")
    st.write("")
    st.write("")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        if st.button("Sim 💘"):
            st.session_state.page = "sim"
            st.rerun()

    # Botão "Não" fugindo
    html_nao = """
    <html>
    <head>
    <style>
        .btn-nao {
            background: linear-gradient(45deg, #ff4d6d, #ff8fab);
            color: white;
            padding: 12px 28px;
            font-size: 18px;
            border-radius: 30px;
            border: none;
            cursor: pointer;
            position: fixed;
            z-index: 1000;
            font-family: Arial;
            box-shadow: 0px 6px 15px rgba(255, 77, 109, 0.4);
        }
    </style>
    </head>
    <body>
        <button id="nao" class="btn-nao"
            style="top: 75%; left: 50%; transform: translateX(-50%);">
            Não 😢
        </button>

        <script>
            const btnNao = document.getElementById("nao");

            btnNao.addEventListener("mouseover", () => {
                const margin = 40;
                const maxX = window.innerWidth - btnNao.offsetWidth - margin;
                const maxY = window.innerHeight - btnNao.offsetHeight - margin;

                const newX = Math.max(margin, Math.random() * maxX);
                const newY = Math.max(margin, Math.random() * maxY);

                btnNao.style.left = newX + "px";
                btnNao.style.top = newY + "px";
                btnNao.style.transform = "none";
            });
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
        <div style="text-align: center; padding-top: 8vh;">
            <img src="data:image/jpg;base64,{img_sim}" width="350"
                 style="border-radius: 25px; box-shadow: 0px 8px 25px rgba(0,0,0,0.2);">
            <h1 style="color: white; font-family: 'Trebuchet MS';
                       text-shadow: 2px 2px 10px rgba(0,0,0,0.4);">
                Vai ser uma noite cheia de surpresas! ✨
            </h1>
            <h3 style="color: white;">
                Para você não se esquecer da gente 💕
            </h3>
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        if st.button("Voltar 💌"):
            st.session_state.page = "home"
            st.rerun()

    # Fotos animadas
    st.markdown(f"""
        <img src="data:image/jpg;base64,{img1}" class="moving-img img-1">
        <img src="data:image/jpg;base64,{img2}" class="moving-img img-2">
        <img src="data:image/jpg;base64,{img3}" class="moving-img img-3">
        <img src="data:image/jpg;base64,{img4}" class="moving-img img-4">
    """, unsafe_allow_html=True)