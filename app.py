import streamlit as st
import base64
import random
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# -----------------------------
# Função para converter imagem
# -----------------------------
def get_base64_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Converter imagens
img_home = get_base64_image("Image.jpg")
img_sim = get_base64_image("ImageSim.jpg")
img1 = get_base64_image("Image1.jpg")
img2 = get_base64_image("Image2.jpg")
img3 = get_base64_image("Image3.jpg")
img4 = get_base64_image("Image4.jpg")

# -----------------------------
# Controle de Página
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# -----------------------------
# TELA INICIAL
# -----------------------------
if st.session_state.page == "home":

    st.markdown(
        f"""
        <div style="text-align:center;">
            <div style="position:relative; display:inline-block;">
                <img src="data:image/jpg;base64,{img_home}" width="300">
                <div style="position:absolute; top:-20px; left:50%;">❤️</div>
                <div style="position:absolute; bottom:-20px; left:50%;">❤️</div>
                <div style="position:absolute; left:-20px; top:50%;">❤️</div>
                <div style="position:absolute; right:-20px; top:50%;">❤️</div>
            </div>
            <h2>Aceitas sair comigo na Sexta para uma noite especial? 💖</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    # BOTÃO SIM (funciona normalmente)
    with col1:
        if st.button("Sim 💘"):
            st.session_state.page = "sim"
            st.rerun()

    # BOTÃO NÃO (HTML + JS + comunica com Python)
    with col2:
        components.html("""
        <div style="position:relative; height:200px;">
            <button id="nao"
                style="position:absolute; padding:12px 20px; font-size:18px; cursor:pointer;">
                Não 😢
            </button>
        </div>

        <script>
        const btn = document.getElementById("nao");

        function mover() {
            const maxX = window.innerWidth - btn.offsetWidth - 50;
            const maxY = window.innerHeight - btn.offsetHeight - 50;

            const x = Math.random() * maxX;
            const y = Math.random() * maxY;

            btn.style.left = x + "px";
            btn.style.top = y + "px";
        }

        btn.addEventListener("mouseover", mover);

        btn.addEventListener("click", function(){
            window.parent.postMessage({type: "nao_clicked"}, "*");
        });
        </script>
        """, height=200)

    # Detectar clique do NÃO
    event = components.html("""
    <script>
    window.addEventListener("message", (event) => {
        if (event.data.type === "nao_clicked") {
            window.parent.postMessage("streamlit:setComponentValue:nao", "*");
        }
    });
    </script>
    """, height=0)

# -----------------------------
# TELA DO SIM
# -----------------------------
elif st.session_state.page == "sim":

    st.markdown(
        f"""
        <div style="text-align:center;">
            <img src="data:image/jpg;base64,{img_sim}" width="400">
            <h2>Uma noite especial está por vir ✨</h2>
            <h3>Porque ao seu lado qualquer sexta vira mágica ❤️</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Imagens girando
    components.html(f"""
    <style>
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
    </style>

    <img src="data:image/jpg;base64,{img1}" class="spin spin1">
    <img src="data:image/jpg;base64,{img2}" class="spin spin2">
    <img src="data:image/jpg;base64,{img3}" class="spin spin3">
    <img src="data:image/jpg;base64,{img4}" class="spin spin4">
    """, height=0)

    if st.button("Voltar"):
        st.session_state.page = "home"
        st.rerun()