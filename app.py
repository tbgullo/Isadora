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
# CSS PARA DEIXAR TUDO BONITO
# -----------------------------
st.markdown("""
<style>
    /* Esconde o menu do Streamlit e o rodapé */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .main {
        background-color: #fff0f5;
    }
    
    /* Centraliza o botão Sim do Streamlit */
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
</style>
""", unsafe_allow_html=True)

# -----------------------------
# TELA INICIAL
# -----------------------------
if st.session_state.page == "home":
    
    # Título e Imagem central
    st.markdown(f"""
        <div style="text-align: center; padding-top: 50px;">
            <img src="data:image/jpg;base64,{img_home}" width="300" style="border-radius: 20px; box-shadow: 0px 4px 15px rgba(0,0,0,0.1);">
            <h2 style="color: #ff4d6d; font-family: Arial;">Aceitas sair comigo na Sexta para uma noite especial? 💖</h2>
        </div>
    """, unsafe_allow_html=True)

    # Layout de colunas para os botões
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col3:
        # BOTÃO SIM (NATIVO STREAMLIT)
        if st.button("Sim 💘"):
            st.session_state.page = "sim"
            st.rerun()

    # O componente HTML apenas para o botão "Não" que foge
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
            z-index: 999;
            font-family: Arial;
        }}
    </style>
    </head>
    <body>
        <button id="nao" class="btn-nao" style="top: 70%; left: 55%;">Não 😢</button>

        <script>
            const btnNao = document.getElementById("nao");
            btnNao.addEventListener("mouseover", () => {{
                const x = Math.random() * (window.innerWidth - 150);
                const y = Math.random() * (window.innerHeight - 50);
                btnNao.style.left = x + "px";
                btnNao.style.top = y + "px";
            }});
        </script>
    </body>
    </html>
    """
    components.html(html_nao, height=400)

# -----------------------------
# TELA DO SIM
# -----------------------------
elif st.session_state.page == "sim":
    
    st.markdown(f"""
        <div style="text-align: center; padding-top: 50px;">
            <img src="data:image/jpg;base64,{img_sim}" width="450" style="border-radius: 20px;">
            <h1 style="color: #ff4d6d;">Uma noite especial está por vir ✨</h1>
            <h3 style="color: #333;">Porque ao seu lado qualquer sexta vira mágica ❤️</h3>
        </div>
    """, unsafe_allow_html=True)

    if st.button("Voltar"):
        st.session_state.page = "home"
        st.rerun()

    # Fotos nos cantos
    st.markdown(f"""
    <style>
        .corner-img {{ position: fixed; width: 150px; z-index: 999; border-radius: 15px; border: 3px solid #ff4d6d; }}
        .top-left {{ top: 20px; left: 20px; }}
        .top-right {{ top: 20px; right: 20px; }}
        .bottom-left {{ bottom: 20px; left: 20px; }}
        .bottom-right {{ bottom: 20px; right: 20px; }}
    </style>
    <img src="data:image/jpg;base64,{img1}" class="corner-img top-left">
    <img src="data:image/jpg;base64,{img2}" class="corner-img top-right">
    <img src="data:image/jpg;base64,{img3}" class="corner-img bottom-left">
    <img src="data:image/jpg;base64,{img4}" class="corner-img bottom-right">
    """, unsafe_allow_html=True)