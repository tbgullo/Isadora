import streamlit as st
import base64

# Configuração da página
st.set_page_config(layout="wide", page_title="Convite Especial 💖")

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
# CSS E LOGICA DE FUGA (JS)
# -----------------------------
st.markdown("""
<style>
    /* Reset básico */
    html, body, [data-testid="stAppViewContainer"] {
        overflow: hidden !important;
        height: 100vh;
        width: 100vw;
    }

    /* Estilo do Botão Não */
    #btn-nao {
        position: fixed;
        left: 55vw;
        top: 65vh;
        background-color: #6c757d;
        color: white;
        border: none;
        padding: 12px 35px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 50px;
        cursor: pointer;
        z-index: 1000000;
        transition: 0.1s ease;
        touch-action: none; /* Impede zoom no mobile ao tocar rápido */
    }

    /* Estilo do Botão Sim do Streamlit */
    .stButton > button {
        background: linear-gradient(90deg, #ff4d6d, #ff758c) !important;
        color: white !important;
        border-radius: 50px !important;
        padding: 10px 30px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        border: none !important;
        width: 140px;
    }
</style>

<script>
    function foge() {
        const btn = document.getElementById('btn-nao');
        if (!btn) return;

        // Largura e altura da tela disponível
        const width = window.innerWidth;
        const height = window.innerHeight;

        // Calcula novas posições (mantendo margem de 100px para não sumir da borda)
        const newX = Math.random() * (width - 150);
        const newY = Math.random() * (height - 100);

        btn.style.left = newX + 'px';
        btn.style.top = newY + 'px';
    }

    // Tenta garantir que o botão exista antes de anexar eventos se necessário
    document.addEventListener('mouseover', function(e) {
        if(e.target.id === 'btn-nao') foge();
    });
</script>
""", unsafe_allow_html=True)

# -----------------------------
# TELA INICIAL
# -----------------------------
if st.session_state.page == "home":
    
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 25px;">
            <div style="display: inline-block; padding: 10px; background: white; border-radius: 30px; box-shadow: 0 10px 25px rgba(0,0,0,0.05);">
                <img src="data:image/jpg;base64,{img_home}" width="220" style="border-radius: 20px;">
            </div>
            <h2 style="color: #d63384; font-family: sans-serif; margin-top: 15px;">Aceitas sair comigo na Sexta? 💖</h2>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        # Botão Sim que funciona no Streamlit
        if st.button("Sim 💘"):
            st.session_state.page = "sim"
            st.rerun()

    # Botão Não injetado via HTML puro com gatilhos forçados
    st.markdown("""
        <button id="btn-nao" 
            onmouseover="foge()" 
            onclick="foge()" 
            ontouchstart="foge()">
            Não 😢
        </button>
    """, unsafe_allow_html=True)

# -----------------------------
# TELA DO SIM
# -----------------------------
elif st.session_state.page == "sim":
    st.markdown(f"""
        <div style="text-align: center;">
            <div style="display: inline-block; padding: 10px; background: white; border-radius: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                <img src="data:image/jpg;base64,{img_sim}" width="320" style="border-radius: 20px;">
            </div>
            <h1 style="color: #d63384; margin-top: 20px;">Vai ser uma noite memorável! ✨</h1>
            <h3 style="color: #666;">Para você nunca se esquecer de mim ❤️</h3>
        </div>
    """, unsafe_allow_html=True)

    if st.button("Voltar"):
        st.session_state.page = "home"
        st.rerun()