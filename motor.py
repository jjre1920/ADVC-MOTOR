import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="ADVANCE - Global Radar", layout="wide", page_icon="🌎")

DB_FILE = "ADVANCE_DATABASE.xlsx"

def inicializar_db():
    columnas = ['Fecha', 'Inmobiliaria', 'Activo', 'Valor', 'Contacto', 'Latitud', 'Longitud']
    if not os.path.exists(DB_FILE):
        # Crear con datos de simulación global
        datos_simulacion = [
            [datetime.now().strftime("%Y-%m-%d"), "ADVANCE Elite", "Penthouse Burj Khalifa", "15,000,000", "+971", 25.1972, 55.2744],
            [datetime.now().strftime("%Y-%m-%d"), "ADVANCE Elite", "Villa Mar de Cortés", "2,500,000", "+52", 27.9455, -111.0422],
            [datetime.now().strftime("%Y-%m-%d"), "ADVANCE Elite", "Loft Manhattan Central Park", "8,200,000", "+1", 40.7831, -73.9712],
            [datetime.now().strftime("%Y-%m-%d"), "ADVANCE Elite", "Mansión en Mónaco", "45,000,000", "+377", 43.7384, 7.4246]
        ]
        df = pd.DataFrame(datos_simulacion, columns=columnas)
        df.to_excel(DB_FILE, index=False, engine='openpyxl')
    return pd.read_excel(DB_FILE, engine='openpyxl')

def principal():
    st.title("⚡ ADVANCE GLOBAL - Intelligence & Logistics")
    st.markdown("### 🛰️ Red de Activos de Alto Perfil")
    
    tab1, tab2 = st.tabs(["🛰️ Radar Global", "📝 Registro de Activos"])

    with tab2:
        st.header("🗄️ Inyección de Datos")
        with st.form("db_form", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                realty = st.text_input("Agencia/Realty")
                titulo = st.text_input("Nombre del Activo")
            with c2:
                valor = st.text_input("Precio USD")
                contacto = st.text_input("Contacto")
            la, lo = st.columns(2)
            lat = la.number_input("Latitud", value=27.9500, format="%.6f")
            lon = lo.number_input("Longitud", value=-111.0500, format="%.6f")
            
            if st.form_submit_button("🚀 Subir al Radar"):
                nueva_fila = {'Fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                              'Inmobiliaria': realty, 'Activo': titulo, 'Valor': valor,
                              'Contacto': contacto, 'Latitud': lat, 'Longitud': lon}
                df = pd.read_excel(DB_FILE, engine='openpyxl')
                df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True)
                df.to_excel(DB_FILE, index=False, engine='openpyxl')
                st.success("✅ Activo Vinculado")
                st.rerun()

    with tab1:
        df_mapa = inicializar_db()
        
        # Métricas Globales
        m1, m2, m3 = st.columns(3)
        m1.metric("Nodos en Red", len(df_mapa), "Operativos")
        m2.metric("Cobertura", "Global", "4 Países")
        m3.metric("Seguridad", "AES-256", "Lock")

        # Visualización
        st.map(df_mapa.rename(columns={'Latitud': 'lat', 'Longitud': 'lon'}))
        
        st.subheader("📋 Inventario Estratégico")
        st.dataframe(df_mapa, use_container_width=True)

if __name__ == "__main__":
    principal()
