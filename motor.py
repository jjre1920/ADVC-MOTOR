import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Identidad Visual ADVANCE GLOBAL
st.set_page_config(page_title="ADVANCE GLOBAL - EliteConnect", layout="wide", page_icon="💎")

DB_FILE = "ADVANCE_DATABASE.xlsx"
LEADS_FILE = "ADVANCE_LEADS.xlsx"

def verificar_sistemas():
    if not os.path.exists(DB_FILE):
        cols = ['Fecha', 'Inmobiliaria', 'Activo', 'Valor', 'Contacto', 'Latitud', 'Longitud', 'Imagen_URL']
        pd.DataFrame(columns=cols).to_excel(DB_FILE, index=False, engine='openpyxl')
    if not os.path.exists(LEADS_FILE):
        pd.DataFrame(columns=['Fecha', 'Activo_Interes', 'Nombre_Cliente', 'WhatsApp']).to_excel(LEADS_FILE, index=False, engine='openpyxl')

def principal():
    verificar_sistemas()
    
    # --- AVISO DE DESARROLLO ---
    st.warning("⚠️ **SISTEMA EN DESARROLLO:** La plataforma ADVANCE se encuentra en fase de pruebas técnicas y expansión de nodos.")
    
    st.title("⚡ ADVANCE GLOBAL - Intelligence & Logistics")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "🛰️ Radar & Galería", 
        "🤝 Registro de Inversionistas", 
        "📝 Alta de Propiedades",
        "📊 Monitor de Datos"
    ])

    df_activos = pd.read_excel(DB_FILE, engine='openpyxl')

    # --- TAB 1: RADAR ---
    with tab1:
        if not df_activos.empty:
            st.map(df_activos.rename(columns={'Latitud': 'lat', 'Longitud': 'lon'}))
            st.write("---")
            cols = st.columns(3)
            for i, (idx, row) in enumerate(df_activos.iterrows()):
                with cols[i % 3]:
                    st.image(row['Imagen_URL'], use_container_width=True)
                    st.markdown(f"**{row['Activo']}**")
                    st.caption(f"Valor:  USD")
                    if st.button(f"Seleccionar {row['Activo']}", key=f"sel_{i}"):
                        st.session_state.interes = row['Activo']
                        st.toast("Activo seleccionado")

    # --- TAB 2: INVERSIONISTAS ---
    with tab2:
        st.header("🤝 Captura de Leads")
        with st.form("leads_form", clear_on_submit=True):
            prop_sel = st.session_state.get('interes', "Ninguno")
            st.info(f"Interés en: **{prop_sel}**")
            nombre = st.text_input("Nombre del Cliente")
            wa = st.text_input("WhatsApp")
            if st.form_submit_button("🚀 Enviar Señal"):
                nuevo = {'Fecha': datetime.now().strftime("%Y-%m-%d %H:%M"),
                         'Activo_Interes': prop_sel, 'Nombre_Cliente': nombre, 'WhatsApp': wa}
                df_l = pd.read_excel(LEADS_FILE, engine='openpyxl')
                pd.concat([df_l, pd.DataFrame([nuevo])], ignore_index=True).to_excel(LEADS_FILE, index=False, engine='openpyxl')
                st.success("Señal de inversionista registrada.")

    # --- TAB 3: CARGA DE PROPIEDADES ---
    with tab3:
        st.header("📝 Alta de Nuevos Activos")
        with st.form("form_alta", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                f_realty = st.text_input("Inmobiliaria/Agente")
                f_activo = st.text_input("Nombre del Activo")
                f_valor = st.text_input("Valor (USD)")
            with c2:
                f_wa = st.text_input("WhatsApp de Contacto")
                f_lat = st.number_input("Latitud", value=27.9400, format="%.6f")
                f_lon = st.number_input("Longitud", value=-111.0400, format="%.6f")
            f_img = st.text_input("URL de la Imagen")
            if st.form_submit_button("🛰️ Publicar"):
                nueva = {'Fecha': datetime.now().strftime("%Y-%m-%d"), 'Inmobiliaria': f_realty, 
                         'Activo': f_activo, 'Valor': f_valor, 'Contacto': f_wa, 
                         'Latitud': f_lat, 'Longitud': f_lon, 'Imagen_URL': f_img}
                df_updated = pd.concat([df_activos, pd.DataFrame([nueva])], ignore_index=True)
                df_updated.to_excel(DB_FILE, index=False, engine='openpyxl')
                st.success("Activo inyectado.")
                st.rerun()

    # --- TAB 4: MONITOR ---
    with tab4:
        st.subheader("📊 Base de Datos Activa")
        st.dataframe(df_activos)

if __name__ == "__main__":
    principal()
