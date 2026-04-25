import streamlit as st
import pandas as pd

st.set_page_config(page_title="ADVANCE GLOBAL - EliteConnect", layout="wide", page_icon="💎")

def principal():
    st.title("⚡ ADVANCE GLOBAL - Intelligence & Logistics")
    st.markdown("### 🏘️ EliteConnect: Gestión de Propiedades de Alto Perfil")

    # --- BARRA LATERAL: ENTRADA DE DATOS ---
    st.sidebar.header("🛠️ Registro de Activo")
    nombre_casa = st.sidebar.text_input("Nombre de la Propiedad", "Villa Paraíso - San Carlos")
    precio = st.sidebar.text_input("Valor Estimado (USD)", ",250,000")
    lat_casa = st.sidebar.number_input("Latitud", value=27.9455, format="%.4f")
    lon_casa = st.sidebar.number_input("Longitud", value=-111.0422, format="%.4f")

    # --- MÉTRICAS ---
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Unidades en Puente", "385", "Activas")
    col2.metric("Propiedad en Foco", "ACTIVA", "VIP")
    col3.metric("Interés de Compra", "Alta", "+12%")
    col4.metric("Seguridad de Datos", "Encriptado", "AES-256")

    st.write("---")

    # --- VISUALIZADOR DE PROPIEDAD ---
    c1, c2 = st.columns([1, 2])
    
    with c1:
        st.subheader("📋 Ficha Técnica")
        st.info(f"**Nombre:** {nombre_casa}")
        st.success(f"**Precio:** {precio}")
        st.write("**Ubicación:** Sector Privado, San Carlos")
        st.write("**Características:** Vista al mar, 5 Recámaras, Muelle Privado.")
        
    with c2:
        st.subheader("📍 Ubicación en Radar")
        mapa_data = pd.DataFrame({'lat': [lat_casa], 'lon': [lon_casa]})
        st.map(mapa_data)

    if st.button("🛰️ Sincronizar con Compradores VIP"):
        st.toast(f"Conectando {nombre_casa} con inversionistas...", icon="💎")

if __name__ == "__main__":
    principal()
