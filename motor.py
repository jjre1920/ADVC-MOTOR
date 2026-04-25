import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="ADVANCE - Data Center", layout="wide", page_icon="🗄️")

# --- CONFIGURACIÓN DE BASE DE DATOS ---
DB_FILE = "ADVANCE_DATABASE.xlsx"

def principal():
    st.title("⚡ ADVANCE GLOBAL - Intelligence & Logistics")
    
    tab1, tab2 = st.tabs(["🛰️ Radar de Activos", "📝 Registro de Propiedades"])

    with tab2:
        st.header("🗄️ Portal de Captura Permanente")
        st.write("Ingrese los datos para actualizar la base de datos maestra.")
        
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
                    'Inmobiliaria': realty,
                    'Activo': titulo,
                    'Valor': valor,
                    'Contacto': contacto,
                    'Latitud': lat,
                    'Longitud': lon
                }
                
                # Proceso de Guardado Real
                try:
                    df = pd.read_excel(DB_FILE)
                    df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True)
                    df.to_excel(DB_FILE, index=False)
                    st.success(f"✅ {titulo} ha sido guardado permanentemente en la base de datos.")
                    st.balloons()
                except Exception as e:
                    st.error(f"Error en la base de datos: {e}")

    with tab1:
        st.subheader("🛰️ Monitoreo de Nodos Registrados")
        try:
            df_mapa = pd.read_excel(DB_FILE)
            if not df_mapa.empty:
                st.metric("Propiedades en Base de Datos", len(df_mapa), "+1")
                st.map(df_mapa[['Latitud', 'Longitud']].rename(columns={'Latitud': 'lat', 'Longitud': 'lon'}))
                st.dataframe(df_mapa) # Tabla para ver los datos guardados
            else:
                st.info("No hay activos registrados aún.")
        except:
            st.warning("Esperando sincronización de archivo...")

if __name__ == "__main__":
    principal()
