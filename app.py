import streamlit as st
import base64
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# -----------------------------
# Converter imagem para base64
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
# Controle de página
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
            font-family: Arial, sans-serif;
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

        .btn {{
            padding: 12px 28px;
            font-size: 18px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
            transition: 0.3s;
            margin: 15px;
        }}

        .btn-sim {{
            background-color: #ff4d6d;
            color: white;
        }}

        .btn-sim:hover {{
            background-color: #e63950;
        }}

        .btn-nao {{
            background-color: #ff4d6d;
            color: white;
            position: absolute;
        }}

        .btn-nao:hover {{
            background-color: #e63950;
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

            <button class="btn btn-sim" onclick="window.location.search='?choice=sim'">
                Sim 💘
            </button>

            <button id="nao" class="btn btn-nao">
                Não 😢
            </button>

        </div>

        <script>
            const btnNao = document.getElementById("nao");

            function mover() {{
                const maxX = window.innerWidth - btnNao.offsetWidth - 20;
                const maxY = window.innerHeight - btnNao.offsetHeight - 20;

                const x = Math.random() * maxX;
                const y = Math.random() * maxY;

                btnNao.style.left = x + "px";
                btnNao.style.top = y + "px";
            }}

            btnNao.addEventListener("mouseover", mover);

            btnNao.addEventListener("click", function() {{
                window.location.search='?choice=nao';
            }});
        </script>

    </body>
    </html>
    """

    components.html(html_code, height=700)

    # Detecta clique via query param
    params = st.query_params
    if "choice" in params:
        if params["choice"] == "sim":
            st.session_state.page = "sim"
            st.query_params.clear()
            st.rerun()

        if params["choice"] == "nao":
            st.warning("Nem pensar 😅 Tenta de novo!")
            st.query_params.clear()

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
            font-family: Arial, sans-serif;
        }}

        .btn {{
            padding: 12px 28px;
            font-size: 18px;
            border-radius: 10px;
            border: none;
            background-color: #ff4d6d;
            color: white;
            cursor: pointer;
            margin-top: 20px;
        }}

        .btn:hover {{
            background-color: #e63950;
        }}
    </style>
    </head>

    <body>

        <img src="data:image/jpg;base64,{img_sim}" width="400">

        <h2>Uma noite especial está por vir ✨</h2>
        <h3>Porque ao seu lado qualquer sexta vira mágica ❤️</h3>

        <button class="btn" onclick="window.location.search='?choice=voltar'">
            Voltar
        </button>

    </body>
    </html>
    """

    components.html(html_code, height=600)

    # 🔥 IMAGENS FIXAS NOS CANTOS DA TELA REAL
    st.markdown(f"""
    <style>
        .corner-img {{
            position: fixed;
            width: 120px;
            z-index: 999;
        }}

        .top-left {{ top: 10px; left: 10px; }}
        .top-right {{ top: 10px; right: 10px; }}
        .bottom-left {{ bottom: 10px; left: 10px; }}
        .bottom-right {{ bottom: 10px; right: 10px; }}
    </style>

    <img src="data:image/jpg;base64,{img1}" class="corner-img top-left">
    <img src="data:image/jpg;base64,{img2}" class="corner-img top-right">
    <img src="data:image/jpg;base64,{img3}" class="corner-img bottom-left">
    <img src="data:image/jpg;base64,{img4}" class="corner-img bottom-right">
    """, unsafe_allow_html=True)

    params = st.query_params
    if "choice" in params and params["choice"] == "voltar":
        st.session_state.page = "home"
        st.query_params.clear()
        st.rerun()