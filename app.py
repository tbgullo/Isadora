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
# CSS ESTILIZADO E TRAVA DE ROLAGEM
# -----------------------------
st.markdown(f"""
<style>
    /* Trava total contra rolagem */
    html, body, [data-testid="stAppViewContainer"], .main {{
        overflow: hidden !important;
        height: 100vh !important;
        width: 100vw !important;
        position: fixed;
    }}

    [data-testid="stAppViewContainer"] {{
        background: linear-gradient(135deg, #fff5f7 0%, #ffe4e1 100%);
    }}
    
    .main .block-container {{
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 0 !important;
    }}

    #MainMenu, footer, header {{visibility: hidden;}}

    h1, h2, h3 {{
        color: #d63384 !important;
        font-family: 'Segoe UI', Arial, sans-serif;
    }}

    /* Botões Sim e Voltar */
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
        margin: 0 auto;
    }}

    /* Animação das fotos orbitando */
    @keyframes moveClockwise {{
        0%   {{ top: 15px; left: 15px; }}
        25%  {{ top: 15px; left: calc(100vw - 100px); }}
        50%  {{ top: calc(100vh - 100px); left: calc(100vw - 100px); }}
        75%  {{ top: calc(100vh - 100px); left: 15px; }}
        100% {{ top: 15px; left: 15px; }}
    }}

    .moving-img {{
        position: fixed;
        width: 80px;
        z-index: 999;
        border-radius: 50%;
        border: 3px solid white;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        animation: moveClockwise 30s linear infinite;
    }}

    .img-1 {{ animation-delay: 0s; }}
    .img-2 {{ animation-delay: -7.5s; }}
    .img-3 {{ animation-delay: -15s; }}
    .img-4 {{ animation-delay: -22.5s; }}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# TELA INICIAL
# -----------------------------
if st.session_state.page == "home":
    
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 10px;">
            <div style="display: inline-block; padding: 10px; background: white; border-radius: 30px; box-shadow: 0 10px 25px rgba(0,0,0,0.05);">
                <img src="data:image/jpg;base64,{img_home}" width="220" style="border-radius: 20px;">
            </div>
            <h2 style="margin-top: 15px;">Aceitas sair comigo na Sexta? 💖</h2>
        </div>
    """, unsafe_allow_html=True)

    col_vazia1, col_sim, col_nao, col_vazia2 = st.columns([2, 1, 1, 2])
    
    with col_sim:
        if st.button("Sim 💘"):
            st.session_state.page = "sim"
            st.rerun()

    with col_nao:
        # Script inteligente para fuga do botão "Não"
        html_nao = f"""
        <html>
        <body style="background:transparent; margin:0; overflow:hidden; width: 100vw; height: 100vh;">
            <button id="nao" style="
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
                box-shadow: 0 4px 10px rgba(0,0,0,0.05);
                position: absolute;
                left: 0; top: 0;
            ">Não 😢</button>

            <script>
                const btn = document.getElementById("nao");
                
                btn.addEventListener("mouseover", () => {{
                    // Pega o tamanho da janela
                    const winW = window.innerWidth;
                    const winH = window.innerHeight;
                    
                    // Define áreas seguras (longe do centro onde está a imagem e o botão Sim)
                    // O botão vai fugir para as extremidades da tela
                    let newX, newY;
                    
                    // Lógica: Se estiver no meio, foge para os cantos aleatoriamente
                    const side = Math.floor(Math.random() * 4);
                    
                    if(side === 0) {{ // Canto superior
                        newX = Math.random() * (winW - 150);
                        newY = Math.random() * (winH * 0.2);
                    }} else if(side === 1) {{ // Canto inferior
                        newX = Math.random() * (winW - 150);
                        newY = winH - 60 - (Math.random() * (winH * 0.2));
                    }} else if(side === 2) {{ // Lateral esquerda
                        newX = Math.random() * (winW * 0.2);
                        newY = Math.random() * (winH - 60);
                    }} else {{ // Lateral direita
                        newX = winW - 150 - (Math.random() * (winW * 0.2));
                        newY = Math.random() * (winH - 60);
                    }}

                    btn.style.position = "fixed";
                    btn.style.left = newX + "px";
                    btn.style.top = newY + "px";
                }});
            </script>
        </body>
        </html>
        """
        # O iframe do botão Não agora ocupa a tela toda para ele poder fugir para qualquer lugar
        # mas sem interferir no clique do botão Sim
        st.components.v1.html(html_nao, height=60)

# -----------------------------
# TELA DO SIM
# -----------------------------
elif st.session_state.page == "sim":
    
    st.markdown(f"""
        <div style="text-align: center;">
            <div style="display: inline-block; padding: 10px; background: white; border-radius: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                <img src="data:image/jpg;base64,{img_sim}" width="320" style="border-radius: 20px;">
            </div>
            <h1 style="margin-top: 20px;">Vai ser uma noite memorável! ✨</h1>
            <h3 style="color: #666; margin-bottom: 10px;">Para você nunca se esquecer de mim ❤️</h3>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        if st.button("Voltar"):
            st.session_state.page = "home"
            st.rerun()

    # Imagens Orbitais
    st.markdown(f"""
        <img src="data:image/jpg;base64,{img1}" class="moving-img img-1">
        <img src="data:image/jpg;base64,{img2}" class="moving-img img-2">
        <img src="data:image/jpg;base64,{img3}" class="moving-img img-3">
        <img src="data:image/jpg;base64,{img4}" class="moving-img img-4">
    """, unsafe_allow_html=True)