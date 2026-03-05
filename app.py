import streamlit as st
import random
import base64

st.set_page_config(layout="wide")

# -----------------------------
# Função para converter imagem em base64
# -----------------------------
def get_base64_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()

img_home = get_base64_image("Image.jpg")
img_sim = get_base64_image("ImageSim.jpg")

# -----------------------------
# Estado da aplicação
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "nao_x" not in st.session_state:
    st.session_state.nao_x = 40
    st.session_state.nao_y = 60

# -----------------------------
# CSS GLOBAL
# -----------------------------
st.markdown(f"""
<style>

body {{
    background-color: #fff0f5;
}}

.center {{
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
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

.no-button {{
    position: fixed;
    left: {st.session_state.nao_x}%;
    top: {st.session_state.nao_y}%;
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

</style>
""", unsafe_allow_html=True)

# -----------------------------
# TELA INICIAL
# -----------------------------
if st.session_state.page == "home":

    st.markdown('<div class="center">', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="heart-wrapper">
        <img src="data:image/jpg;base64,{img_home}" width="300">
        <div class="heart" style="top:-20px; left:50%;">❤️</div>
        <div class="heart" style="bottom:-20px; left:50%;">❤️</div>
        <div class="heart" style="left:-20px; top:50%;">❤️</div>
        <div class="heart" style="right:-20px; top:50%;">❤️</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## Aceitas sair comigo na Sexta para uma noite especial? 💖")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Sim 💘"):
            st.session_state.page = "sim"
            st.rerun()

    # BOTÃO NÃO FUGINDO
    st.markdown('<div class="no-button">', unsafe_allow_html=True)
    if st.button("Não 😢"):
        st.session_state.nao_x = random.randint(5, 85)
        st.session_state.nao_y = random.randint(5, 85)
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # SCRIPT PARA FAZER O BOTÃO FUGIR AO PASSAR O MOUSE
    st.markdown("""
    <script>
    const btn = window.parent.document.querySelectorAll('button');
    btn.forEach(b => {
        if (b.innerText.includes("Não")) {
            b.onmouseover = function() {
                const x = Math.floor(Math.random() * 80);
                const y = Math.floor(Math.random() * 80);
                b.parentElement.style.left = x + "%";
                b.parentElement.style.top = y + "%";
            }
        }
    });
    </script>
    """, unsafe_allow_html=True)


# -----------------------------
# TELA DO SIM
# -----------------------------
elif st.session_state.page == "sim":

    st.markdown('<div class="center">', unsafe_allow_html=True)

    st.markdown(f"""
        <img src="data:image/jpg;base64,{img_sim}" width="400">
    """, unsafe_allow_html=True)

    st.markdown("## Uma noite especial está por vir ✨")
    st.markdown("### Porque ao seu lado qualquer sexta vira mágica ❤️")

    if st.button("Voltar"):
        st.session_state.page = "home"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

    # Imagens girando
    st.markdown("""
        <img src="Image1.jpg" class="spin spin1">
        <img src="Image2.jpg" class="spin spin2">
        <img src="Image3.jpg" class="spin spin3">
        <img src="Image4.jpg" class="spin spin4">
    """, unsafe_allow_html=True)