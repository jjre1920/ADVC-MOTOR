import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Configuración de Marca ADVANCE
st.set_page_config(page_title="ADVANCE GLOBAL - EliteConnect", layout="wide", page_icon="💎")

DB_FILE = "ADVANCE_DATABASE.xlsx"
LEADS_FILE = "ADVANCE_LEADS.xlsx"

def verificar_integridad():
    # Estructura Maestra de Propiedades
    cols_prop = ['Fecha', 'Inmobiliaria', 'Activo', 'Valor', 'Contacto', 'Latitud', 'Longitud', 'Imagen_URL']
    if not os.path.exists(DB_FILE):
        # Datos iniciales con imágenes de alta calidad
        datos = [
            [datetime.now().strftime("%Y-%m-%d"), "ADVANCE Elite", "Penthouse Burj Khalifa", "15,000,000", "971", 25.1972, 55.2744, "https://images.unsplash.com/photo-1597659840241-37e2b9c2f55f?auto=format&fit=crop&w=800&q=80"],
            [datetime.now().strftime("%Y-%m-%d"), "ADVANCE Elite", "Villa Mar de Cortés", "2,500,000", "52", 27.9455, -111.0422, "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=800&q=80"],
            [datetime.now().strftime("%Y-%m-%d"), "ADVANCE Elite", "Mansión en Mónaco", "45,000,000", "377", 43.7384, 7.4246, "https://images.unsplash.com/photo-1613490493576-7fde63acd811?auto=format&fit=crop&w=800&q=80"]
        ]
        pd.DataFrame(datos, columns=cols_prop).to_excel(DB_FILE, index=False, engine='openpyxl')
    
    # Estructura de Inversionistas (Leads)
    if not os.path.exists(LEADS_FILE):
        pd.DataFrame(columns=['Fecha', 'Activo_Interes', 'Nombre_Cliente', 'WhatsApp']).to_excel(LEADS_FILE, index=False, engine='openpyxl')

def principal():
    verificar_integridad()
    st.title("⚡ ADVANCE GLOBAL - Intelligence & Logistics")
    
    tab1, tab2, tab3 = st.tabs(["🛰️ Radar & Galería VIP", "🤝 Registro de Inversionistas", "📊 Base de Datos Interna"])

    df_activos = pd.read_excel(DB_FILE, engine='openpyxl')

    with tab1:
        st.subheader("🛰️ Localización Táctica de Activos")
        st.map(df_activos.rename(columns={'Latitud': 'lat', 'Longitud': 'lon'}))
        
        st.write("---")
        st.subheader("🖼️ Galería de Activos de Alto Perfil")
        cols = st.columns(len(df_activos))
        for i, (idx, row) in enumerate(df_activos.iterrows()):
            with cols[i]:
                st.image(row['Imagen_URL'], use_container_width=True)
                st.markdown(f"**{row['Activo']}**")
                st.caption(f"Valor:  USD")
                if st.button(f"Seleccionar {row['Activo']}", key=f"sel_{i}"):
                    st.session_state.interes = row['Activo']
                    st.toast(f"Activo {row['Activo']} seleccionado")

    with tab2:
        st.header("🤝 Captura de Prospecto")
        with st.form("leads_form", clear_on_submit=True):
            prop_sel = st.session_state.get('interes', df_activos['Activo'].iloc[0])
            st.info(f"Interés actual: **{prop_sel}**")
            nombre = st.text_input("Nombre del Inversionista")
            wa = st.text_input("WhatsApp")
            
            if st.form_submit_button("🚀 Enviar al Comandante"):
                nuevo = {'Fecha': datetime.now().strftime("%Y-%m-%d %H:%M"),
                         'Activo_Interes': prop_sel, 'Nombre_Cliente': nombre, 'WhatsApp': wa}
                df_l = pd.read_excel(LEADS_FILE, engine='openpyxl')
                pd.concat([df_l, pd.DataFrame([nuevo])], ignore_index=True).to_excel(LEADS_FILE, index=False, engine='openpyxl')
                st.success("✅ Registro de inversionista completado.")

    with tab3:
        st.subheader("📁 Monitoreo de Archivos")
        st.write("Datos de Activos:")
        st.dataframe(df_activos)
        if os.path.exists(LEADS_FILE):
            st.write("Últimos Inversionistas Registrados:")
            st.dataframe(pd.read_excel(LEADS_FILE, engine='openpyxl'))

if __name__ == "__main__":
    principal()
