import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="ADVANCE - Data Center", layout="wide", page_icon="🗄️")

# --- CONFIGURACIÓN DE BASE DE DATOS ---
DB_FILE = "ADVANCE_DATABASE.xlsx"

# Si el archivo no existe en el servidor, lo creamos de inmediato
if not os.path.exists(DB_FILE):
    columnas = ['Fecha', 'Inmobiliaria', 'Activo', 'Valor', 'Contacto', 'Latitud', 'Longitud']
    pd.DataFrame(columns=columnas).to_excel(DB_FILE, index=False)

def principal():
    st.title("⚡ ADVANCE GLOBAL - Intelligence & Logistics")
    
    tab1, tab2 = st.tabs(["🛰️ Radar de Activos", "📝 Registro de Propiedades"])

    with tab2:
        st.header("🗄️ Portal de Captura Permanente")
        with st.form("database_form", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                realty = st.text_input("Inmobiliaria / Agente")
                titulo = st.text_input("Nombre del Activo")
            with c2:
                valor = st.text_input("Valor (USD)")
                contacto = st.text_input("Contacto (WhatsApp)")

            st.write("📍 **Geolocalización**")
            la, lo = st.columns(2)
            lat = la.number_input("Latitud", value=27.9500, format="%.6f")
            lon = lo.number_input("Longitud", value=-111.0500, format="%.6f")
            
            submit = st.form_submit_button("🚀 Inyectar Datos a ADVANCE")

            if submit:
                nueva_fila = {
                    'Fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'Inmobiliaria': realty, 'Activo': titulo, 'Valor': valor,
                    'Contacto': contacto, 'Latitud': lat, 'Longitud': lon
                }
                df = pd.read_excel(DB_FILE)
                df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True)
                df.to_excel(DB_FILE, index=False)
                st.success(f"✅ {titulo} guardado con éxito.")
                st.balloons()

    with tab1:
        st.subheader("🛰️ Monitoreo de Nodos Registrados")
        df_mapa = pd.read_excel(DB_FILE)
        if not df_mapa.empty:
            st.metric("Activos Online", len(df_mapa), "En Red")
            st.map(df_mapa[['Latitud', 'Longitud']].rename(columns={'Latitud': 'lat', 'Longitud': 'lon'}))
            st.dataframe(df_mapa)
        else:
            st.info("Radar a la espera de nuevos registros.")

if __name__ == "__main__":
    principal()
