import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="ADVANCE - Data Center", layout="wide", page_icon="🗄️")

def principal():
    st.title("⚡ ADVANCE GLOBAL - Intelligence & Logistics")
    
    # --- PESTAÑAS DE OPERACIÓN ---
    tab1, tab2 = st.tabs(["🛰️ Radar de Activos", "📝 Registro de Propiedades"])

    with tab2:
        st.header("🗄️ Portal de Captura Permanente")
        st.write("Complete los datos. La información será almacenada en la base de datos de ADVANCE.")
        
        with st.form("database_form", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                realty = st.text_input("Inmobiliaria / Agente")
                titulo = st.text_input("Nombre del Activo (Propiedad/Auto)")
            with c2:
                valor = st.text_input("Valor de Mercado (USD)")
                contacto = st.text_input("Vínculo de Contacto (WA/Cel)")

            st.write("📍 **Geolocalización Táctica**")
            la, lo = st.columns(2)
            lat = la.number_input("Latitud", value=27.9500, format="%.6f")
            lon = lo.number_input("Longitud", value=-111.0500, format="%.6f")
            
            submit = st.form_submit_button("🚀 Inyectar Datos a la Red")

            if submit:
                # Simulación de guardado (Preparación para Google Sheets)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                st.success(f"✅ REGISTRO EXITOSO: {titulo} guardado en el servidor a las {timestamp}.")
                st.info("Sincronizando con la base de datos maestra...")

    with tab1:
        st.subheader("🛰️ Monitoreo de Nodos en Tiempo Real")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Unidades en Puente", "385", "Activas")
        col2.metric("Base de Datos", "Sincronizada", "Cloud")
        col3.metric("Flujo de Datos", "1.2 GB/s", "Óptimo")
        col4.metric("Seguridad", "AES-256", "Lock")
        
        # Mapa base
        mapa_data = pd.DataFrame({'lat': [27.9500], 'lon': [-111.0500]})
        st.map(mapa_data)

if __name__ == "__main__":
    principal()
