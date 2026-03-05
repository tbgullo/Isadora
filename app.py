import streamlit as st
import random
import time

st.set_page_config(layout="wide")

# -----------------------------
# Estado da aplicação
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "nao_x" not in st.session_state:
    st.session_state.nao_x = 50
    st.session_state.nao_y = 50


# -----------------------------
# CSS PERSONALIZADO
# -----------------------------
st.markdown("""
<style>

body {
    background-color: #fff0f5;
}

/* Centralizar conteúdo */
.center {
    text-align: center;
}

/* Corações decorativos */
.heart-container {
    position: relative;
    display: inline-block;
}

.heart-decor {
    position: absolute;
    font-size: 25px;
    color: red;
}

/* Imagens girando */
.spin1 {
    position: fixed;
    top: 10%;
    left: 5%;
    width: 120px;
    animation: spin 6s linear infinite;
}

.spin2 {
    position: fixed;
    top: 10%;
    right: 5%;
    width: 120px;
    animation: spin 8s linear infinite;
}

.spin3 {
    position: fixed;
    bottom: 10%;
    left: 5%;
    width: 120px;
    animation: spin 7s linear infinite;
}

.spin4 {
    position: fixed;
    bottom: 10%;
    right: 5%;
    width: 120px;
    animation: spin 9s linear infinite;
}

@keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

/* Botão Não flutuante */
.no-button {
    position: fixed;
    left: """ + str(st.session_state.nao_x) + """%;
    top: """ + str(st.session_state.nao_y) + """%;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# TELA INICIAL
# -----------------------------
if st.session_state.page == "home":

    st.markdown('<div class="center">', unsafe_allow_html=True)

    # Corações ao redor da imagem
    st.markdown("""
    <div class="heart-container">
        <img src="data:image/jpg;base64,{}" width="300">
        <div class="heart-decor" style="top:-20px; left:50%;">❤️</div>
        <div class="heart-decor" style="bottom:-20px; left:50%;">❤️</div>
        <div class="heart-decor" style="left:-20px; top:50%;">❤️</div>
        <div class="heart-decor" style="right:-20px; top:50%;">❤️</div>
    </div>
    """.format(st.image("Image.jpg", width=300)), unsafe_allow_html=True)

    st.markdown("## Aceitas sair comigo na Sexta para uma noite especial? 💖")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Sim 💘"):
            st.session_state.page = "sim"
            st.rerun()

    with col2:
        # Botão Não com posição dinâmica
        st.markdown('<div class="no-button">', unsafe_allow_html=True)
        if st.button("Não 😢"):
            st.session_state.nao_x = random.randint(5, 80)
            st.session_state.nao_y = random.randint(5, 80)
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------
# TELA DO SIM
# -----------------------------
elif st.session_state.page == "sim":

    st.image("ImageSim.jpg", width=400)

    # Imagens girando
    st.markdown("""
    <img src="Image1.jpeg" class="spin1">
    <img src="Image2.jpeg" class="spin2">
    <img src="Image3.jpeg" class="spin3">
    <img src="Image4.jpeg" class="spin4">
    """, unsafe_allow_html=True)

    st.markdown("## Uma noite especial está por vir ✨")
    st.markdown("### Porque ao seu lado qualquer sexta vira a melhor da minha vida ❤️")

    if st.button("Voltar"):
        st.session_state.page = "home"
        st.rerun()