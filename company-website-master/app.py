import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import os

# Cargar la imagen del favicon
img = Image.open("images/LogoLuci.ico")
img_favicon = img.resize((32, 32))
img_favicon.save("favicon.ico", format="ICO")

# Configurar la página
st.set_page_config(page_title="Luci Lashes", page_icon="favicon.ico", layout="wide")

# Función para cargar archivos Lottie
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Cargar el CSS local
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# Ruta a la imagen del logo
logo_path = "company-website-master/images/LogoLuci.png"  # Asegúrate de que esta ruta sea correcta

# Barra de navegación con estilo
st.markdown(f"""
    <nav style="display: flex; align-items: center; justify-content: space-between; background-color: #c6d1d5; padding: 25px; position: fixed; top: 0; left: 0; right: 0; width: 100%; z-index: 1000;">
        <div class="nav-links" style="display: flex; gap: 15px;">
            <div class="nav-item"><a href="#inicio" class="nav-link">Inicio</a></div>
            <div class="nav-item"><a href="#servicios" class="nav-link">Servicios</a></div>
            <div class="nav-item"><a href="#cita" class="nav-link">Agendar Cita</a></div>
            <div class="nav-item"><a href="#contacto" class="nav-link">Contacto</a></div>
        </div>
    </nav>

    <style>
        nav {{
            background-color: #c6d1d5; /* Color de fondo */
            padding: 25px;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            width: 100%;
            z-index: 1000;
            display: flex;
            align-items: center;
            justify-content: space-between; /* Espacio entre logo y enlaces */
        }}

        .nav-links {{
            display: flex;
            gap: 15px; /* Espacio entre los enlaces */
            justify-content: center; /* Centrar los enlaces */
            flex-grow: 1; /* Permitir que ocupe todo el espacio disponible */
        }}

        .nav-item {{
            background-color: transparent; /* Fondo transparente */
            padding: 15px 50px; /* Tamaño del botón */
            border-radius: 5px; /* Bordes redondeados */
            transition: background-color 0.3s; /* Transición suave */
        }}

        .nav-link {{
            color: #93a3b2; /* Color del texto */
            text-decoration: none; /* Sin subrayado */
            font-size: 18px; /* Aumentar el tamaño del texto */
            font-family: 'Montserrat', sans-serif; /* Aplicar la fuente Montserrat */
            font-weight: 500; /* Peso de la fuente */
        }}

        .nav-link:hover {{
            color: white; /* Cambiar a blanco al pasar el mouse */
        }}
    </style>
""", unsafe_allow_html=True)

# Verificar si la imagen existe
if os.path.exists(logo_path):
    st.image(logo_path, caption="Logo de Luci Lashes", width=200)
else:
    st.error(f"No se encontró la imagen en la ruta: {logo_path}")

# Resto del contenido
st.container()  # Puedes agregar más contenido aquí









# Lottie Animation
#lottie_file = "https://lottie.host/15d3805b-5762-42a4-a1c0-08cb8cdb315b/kv21az63uF.json"

with st.container():
    st.subheader("Hola, somos Luci Lashes")
    st.title("Tu Belleza es Nuestra Pasión")
    st.write("Explora nuestros servicios de pestañas y más.")
    st.write("[Saber más >](https://www.instagram.com/lashesx.lulu/profilecard/?igsh=MXR6b3BsODNjZ2xwOQ==)")


