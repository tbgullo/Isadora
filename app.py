import streamlit as st
import random
import base64
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# -----------------------------
# Função para converter imagem em base64
# -----------------------------
def get_base64_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_home = get_base64_image("Image.jpg")
img_sim = get_base64_image("ImageSim.jpg")
img1 = get_base64_image("Image1.jpg")
img2 = get_base64_image("Image2.jpg")
img3 = get_base64_image("Image3.jpg")
img4 = get_base64_image("Image4.jpg")

# -----------------------------
# Estado
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# -----------------------------
# TELA INICIAL
# -----------------------------
if st.session_state.page == "home":

    html_code = f"""
    <html>
    <head>
    <style>
        body {{
            background-color: #fff0f5;
            text-align: center;
            overflow: hidden;
        }}

        .container {{
            margin-top: 50px;
        }}

        .heart-wrapper {{
            position: relative;
            display: inline-block;
        }}

        .heart {{
            position: absolute;
            font-size: 28px;
            color: red;
        }}

        button {{
            padding: 12px 25px;
            font-size: 18px;
            margin: 20px;
            cursor: pointer;
        }}

        #nao {{
            position: absolute;
        }}
    </style>
    </head>

    <body>
        <div class="container">
            <div class="heart-wrapper">
                <img src="data:image/jpg;base64,{img_home}" width="300">
                <div class="heart" style="top:-20px; left:50%;">❤️</div>
                <div class="heart" style="bottom:-20px; left:50%;">❤️</div>
                <div class="heart" style="left:-20px; top:50%;">❤️</div>
                <div class="heart" style="right:-20px; top:50%;">❤️</div>
            </div>

            <h2>Aceitas sair comigo na Sexta para uma noite especial? 💖</h2>

            <button onclick="window.parent.postMessage('sim','*')">Sim 💘</button>
            <button id="nao">Não 😢</button>
        </div>

        <script>
            const nao = document.getElementById("nao");

            nao.addEventListener("mouseover", function() {{
                const x = Math.random() * window.innerWidth * 0.8;
                const y = Math.random() * window.innerHeight * 0.8;
                nao.style.left = x + "px";
                nao.style.top = y + "px";
            }});
        </script>
    </body>
    </html>
    """

    components.html(html_code, height=700)

    # Escuta clique no botão Sim
    if st.button("HiddenSim", key="hidden", help=""):
        pass

    # Captura mensagem do botão Sim
    query = st.query_params
    if "sim" in query:
        st.session_state.page = "sim"
        st.rerun()

# -----------------------------
# TELA DO SIM
# -----------------------------
elif st.session_state.page == "sim":

    html_code = f"""
    <html>
    <head>
    <style>
        body {{
            background-color: #fff0f5;
            text-align: center;
            overflow: hidden;
        }}

        .spin {{
            position: fixed;
            width: 120px;
            animation: spin 6s linear infinite;
        }}

        .spin1 {{ top: 5%; left: 5%; }}
        .spin2 {{ top: 5%; right: 5%; }}
        .spin3 {{ bottom: 5%; left: 5%; }}
        .spin4 {{ bottom: 5%; right: 5%; }}

        @keyframes spin {{
            from {{ transform: rotate(0deg); }}
            to {{ transform: rotate(360deg); }}
        }}

        button {{
            padding: 12px 25px;
            font-size: 18px;
            margin-top: 20px;
            cursor: pointer;
        }}
    </style>
    </head>

    <body>

        <img src="data:image/jpg;base64,{img_sim}" width="400">

        <h2>Uma noite especial está por vir ✨</h2>
        <h3>Porque ao seu lado qualquer sexta vira mágica ❤️</h3>

        <button onclick="window.parent.postMessage('voltar','*')">Voltar</button>

        <img src="data:image/jpg;base64,{img1}" class="spin spin1">
        <img src="data:image/jpg;base64,{img2}" class="spin spin2">
        <img src="data:image/jpg;base64,{img3}" class="spin spin3">
        <img src="data:image/jpg;base64,{img4}" class="spin spin4">

    </body>
    </html>
    """

    components.html(html_code, height=800)

    query = st.query_params
    if "voltar" in query:
        st.session_state.page = "home"
        st.rerun()