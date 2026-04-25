import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="ADVANCE GLOBAL - EliteConnect", layout="wide", page_icon="💎")

# --- BASES DE DATOS ---
DB_FILE = "ADVANCE_DATABASE.xlsx"
LEADS_FILE = "ADVANCE_LEADS.xlsx"

def cargar_datos():
    if not os.path.exists(DB_FILE):
        columnas = ['Fecha', 'Inmobiliaria', 'Activo', 'Valor', 'Contacto', 'Latitud', 'Longitud', 'Imagen_URL']
        datos = [
            ["2026-04-25", "ADVANCE Elite", "Penthouse Burj Khalifa", "15,000,000", "971", 25.1972, 55.2744, "https://images.unsplash.com/photo-1597659840241-37e2b9c2f55f?q=80&w=600"],
            ["2026-04-25", "ADVANCE Elite", "Villa Mar de Cortés", "2,500,000", "52", 27.9455, -111.0422, "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?q=80&w=600"],
            ["2026-04-25", "ADVANCE Elite", "Loft Manhattan Central Park", "8,200,000", "1", 40.7831, -73.9712, "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?q=80&w=600"],
            ["2026-04-25", "ADVANCE Elite", "Mansión en Mónaco", "45,000,000", "377", 43.7384, 7.4246, "https://images.unsplash.com/photo-1613490493576-7fde63acd811?q=80&w=600"]
        ]
        df = pd.DataFrame(datos, columns=columnas)
        df.to_excel(DB_FILE, index=False, engine='openpyxl')
    return pd.read_excel(DB_FILE, engine='openpyxl')

def principal():
    st.title("⚡ ADVANCE GLOBAL - Intelligence & Logistics")
    df_activos = cargar_datos()

    tab1, tab2 = st.tabs(["🛰️ Radar & Galería", "🤝 Formulario de Interés"])

    with tab1:
        st.subheader("🛰️ Ubicación Táctica de Activos")
        st.map(df_activos.rename(columns={'Latitud': 'lat', 'Longitud': 'lon'}))
        
        st.write("---")
        st.subheader("🖼️ Catálogo de Activos VIP")
        cols = st.columns(2)
        for i, row in df_activos.iterrows():
            with cols[i % 2]:
                st.image(row['Imagen_URL'], use_container_width=True)
                st.markdown(f"### {row['Activo']}")
                st.write(f"💰 **Valor:**  USD | 🏢 **Agencia:** {row['Inmobiliaria']}")
                if st.button(f"Me interesa {row['Activo']}", key=f"btn_{i}"):
                    st.session_state.interes = row['Activo']
                    st.info("Desplázate a la pestaña 'Interés' para dejar tus datos.")

    with tab2:
        st.header("🤝 Captura de Prospecto (Lead)")
        with st.form("leads_form", clear_on_submit=True):
            propiedad_previa = st.session_state.get('interes', df_activos['Activo'].iloc[0])
            propiedad = st.selectbox("Activo de Interés", df_activos['Activo'].tolist(), index=list(df_activos['Activo']).index(propiedad_previa))
            nombre = st.text_input("Nombre Completo del Inversionista")
            tel = st.text_input("WhatsApp (con código de área)")
            
            if st.form_submit_button("🚀 Enviar Señal al Comandante"):
                nuevo_lead = {'Fecha': datetime.now().strftime("%Y-%m-%d %H:%M"),
                              'Activo_Interes': propiedad, 'Nombre_Cliente': nombre, 'WhatsApp': tel}
                if not os.path.exists(LEADS_FILE):
                    pd.DataFrame([nuevo_lead]).to_excel(LEADS_FILE, index=False, engine='openpyxl')
                else:
                    df_l = pd.read_excel(LEADS_FILE, engine='openpyxl')
                    pd.concat([df_l, pd.DataFrame([nuevo_lead])], ignore_index=True).to_excel(LEADS_FILE, index=False, engine='openpyxl')
                st.success(f"Señal recibida. El Comandante contactará a {nombre} para el activo {propiedad}.")

if __name__ == "__main__":
    principal()
