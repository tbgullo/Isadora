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

img_home = get_base64_image("Image.jpg")
img_sim = get_base64_image("ImageSim.jpg")
img1 = get_base64_image("Image1.jpg")
img2 = get_base64_image("Image2.jpg")
img3 = get_base64_image("Image3.jpg")
img4 = get_base64_image("Image4.jpg")

if "page" not in st.session_state:
    st.session_state.page = "home"

# -----------------------------
# CSS 
# -----------------------------
st.markdown(f"""
<style>
    html, body, [data-testid="stAppViewContainer"], .main, .block-container {{
        overflow: hidden !important;
        height: 100vh !important;
        width: 100vw !important;
        margin: 0 !important;
        padding: 0 !important;
    }}

    [data-testid="stAppViewContainer"] {{
        background: linear-gradient(135deg, #fff5f7 0%, #ffe4e1 100%);
    }}
    
    .main .block-container {{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }}

    #MainMenu, footer, header {{visibility: hidden;}}

    h1, h2, h3 {{
        color: #d63384 !important;
        font-family: 'Segoe UI', Arial, sans-serif;
    }}

    .stButton > button {{
        background: linear-gradient(90deg, #ff4d6d, #ff758c) !important;
        color: white !important;
        border-radius: 50px !important;
        padding: 10px 30px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        border: none !important;
        box-shadow: 0 4px 10px rgba(255, 77, 109, 0.3) !important;
        width: 140px;
        z-index: 10;
    }}

    #nao-button {{
        position: fixed;
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
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        z-index: 999999;
        left: calc(50% + 15px);
        top: 72%;
        transform: translateY(-50%);
        /* Transição rápida para a fuga parecer natural */
        transition: left 0.1s ease, top 0.1s ease;
    }}

    .moving-img {{
        position: fixed;
        width: 80px;
        z-index: 99;
        border-radius: 50%;
        border: 3px solid white;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        animation: moveClockwise 30s linear infinite;
    }}

    @keyframes moveClockwise {{
        0%   {{ top: 15px; left: 15px; }}
        25%  {{ top: 15px; left: calc(100vw - 100px); }}
        50%  {{ top: calc(100vh - 100px); left: calc(100vw - 100px); }}
        75%  {{ top: calc(100vh - 100px); left: 15px; }}
        100% {{ top: 15px; left: 15px; }}
    }}
</style>
""", unsafe_allow_html=True)

if st.session_state.page == "home":
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 25px;">
            <div style="display: inline-block; padding: 10px; background: white; border-radius: 30px; box-shadow: 0 10px 25px rgba(0,0,0,0.05);">
                <img src="data:image/jpg;base64,{img_home}" width="220" style="border-radius: 20px;">
            </div>
            <h2 style="margin-top: 15px;">Aceitas sair comigo na Sexta? 💖</h2>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown('<div style="transform: translateX(-80px);">', unsafe_allow_html=True)
        if st.button("Sim 💘"):
            st.session_state.page = "sim"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # BOTÃO NÃO COM FOCO EXCLUSIVO NO CONTATO (MOUSEOVER)
    st.markdown("""
        <button id="nao-button">Não 😢</button>
        
        <script>
        (function() {
            function setup() {
                const btn = document.getElementById("nao-button");
                if (!btn) {
                    setTimeout(setup, 100);
                    return;
                }

                const foge = () => {
                    // Tamanho da janela
                    const winW = window.innerWidth;
                    const winH = window.innerHeight;
                    
                    // Tamanho do botão
                    const btnW = 140;
                    const btnH = 45;

                    // Margem de segurança
                    const margem = 30;

                    // Gera nova posição aleatória dentro da tela
                    const newX = Math.random() * (winW - btnW - (margem * 2)) + margem;
                    const newY = Math.random() * (winH - btnH - (margem * 2)) + margem;

                    btn.style.left = newX + "px";
                    btn.style.top = newY + "px";
                };

                // DISPARA AO ENCOSTAR O MOUSE
                btn.addEventListener("mouseover", foge);
                
                // DISPARA AO CLICAR (CASO O MOUSEOVER FALHE EM ALTA VELOCIDADE)
                btn.addEventListener("click", (e) => {
                    e.preventDefault();
                    foge();
                });

                // DISPARA NO TOUCH (MOBILE)
                btn.addEventListener("touchstart", (e) => {
                    e.preventDefault();
                    foge();
                });
            }
            setup();
        })();
        </script>
    """, unsafe_allow_html=True)

elif st.session_state.page == "sim":
    # (O restante do código da tela do Sim permanece igual)
    st.markdown(f"""
        <div style="text-align: center;">
            <div style="display: inline-block; padding: 10px; background: white; border-radius: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                <img src="data:image/jpg;base64,{img_sim}" width="320" style="border-radius: 20px;">
            </div>
            <h1 style="margin-top: 20px;">Vai ser uma noite memorável! ✨</h1>
            <h3 style="color: #666;">Para você nunca se esquecer de mim ❤️</h3>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Voltar"):
            st.session_state.page = "home"
            st.rerun()

    st.markdown(f"""
        <img src="data:image/jpg;base64,{img1}" class="moving-img" style="animation-delay: 0s;">
        <img src="data:image/jpg;base64,{img2}" class="moving-img" style="animation-delay: -7.5s;">
        <img src="data:image/jpg;base64,{img3}" class="moving-img" style="animation-delay: -15s;">
        <img src="data:image/jpg;base64,{img4}" class="moving-img" style="animation-delay: -22.5s;">
    """, unsafe_allow_html=True)