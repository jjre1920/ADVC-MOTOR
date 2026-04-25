import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="ADVANCE GLOBAL - EliteConnect", layout="wide", page_icon="💎")

DB_FILE = "ADVANCE_DATABASE.xlsx"
LEADS_FILE = "ADVANCE_LEADS.xlsx"

def cargar_y_reparar_db():
    columnas_necesarias = ['Fecha', 'Inmobiliaria', 'Activo', 'Valor', 'Contacto', 'Latitud', 'Longitud', 'Imagen_URL']
    
    # Datos de simulación con imágenes reales
    datos_iniciales = [
        [datetime.now().strftime("%Y-%m-%d"), "ADVANCE Elite", "Penthouse Burj Khalifa", "15,000,000", "971", 25.1972, 55.2744, "https://images.unsplash.com/photo-1582672060674-bc2bd808a8b5?q=80&w=600"],
        [datetime.now().strftime("%Y-%m-%d"), "ADVANCE Elite", "Villa Mar de Cortés", "2,500,000", "52", 27.9455, -111.0422, "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?q=80&w=600"],
        [datetime.now().strftime("%Y-%m-%d"), "ADVANCE Elite", "Loft Manhattan Central Park", "8,200,000", "1", 40.7831, -73.9712, "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?q=80&w=600"],
        [datetime.now().strftime("%Y-%m-%d"), "ADVANCE Elite", "Mansión en Mónaco", "45,000,000", "377", 43.7384, 7.4246, "https://images.unsplash.com/photo-1613490493576-7fde63acd811?q=80&w=600"]
    ]

    if not os.path.exists(DB_FILE):
        df = pd.DataFrame(datos_iniciales, columns=columnas_necesarias)
        df.to_excel(DB_FILE, index=False, engine='openpyxl')
    else:
        df = pd.read_excel(DB_FILE, engine='openpyxl')
        # Si falta la columna de imagen, reiniciamos con datos completos
        if 'Imagen_URL' not in df.columns:
            df = pd.DataFrame(datos_iniciales, columns=columnas_necesarias)
            df.to_excel(DB_FILE, index=False, engine='openpyxl')
    return df

def principal():
    st.title("⚡ ADVANCE GLOBAL - Intelligence & Logistics")
    
    try:
        df_activos = cargar_y_reparar_db()
    except Exception as e:
        st.error(f"Error crítico de base de datos: {e}")
        return

    tab1, tab2 = st.tabs(["🛰️ Radar & Galería", "🤝 Interés de Compra"])

    with tab1:
        st.subheader("🛰️ Ubicación Táctica de Activos")
        st.map(df_activos.rename(columns={'Latitud': 'lat', 'Longitud': 'lon'}))
        
        st.write("---")
        st.subheader("🖼️ Catálogo de Activos VIP")
        cols = st.columns(2)
        for i, row in df_activos.iterrows():
            with cols[i % 2]:
                # Usamos una imagen genérica si el link falla
                img = row['Imagen_URL'] if pd.notnull(row['Imagen_URL']) else "https://via.placeholder.com/400"
                st.image(img, use_container_width=True)
                st.markdown(f"### {row['Activo']}")
                st.write(f"💰 **Valor:**  USD | 🏢 {row['Inmobiliaria']}")
                if st.button(f"Me interesa {row['Activo']}", key=f"btn_{i}"):
                    st.session_state.interes = row['Activo']
                    st.success(f"Seleccionado: {row['Activo']}. Ve a la pestaña de Interés.")

    with tab2:
        st.header("🤝 Registro de Interés Estratégico")
        with st.form("leads_form", clear_on_submit=True):
            propiedad_seleccionada = st.session_state.get('interes', df_activos['Activo'].iloc[0])
            propiedad = st.selectbox("Activo Seleccionado", df_activos['Activo'].tolist(), 
                                     index=list(df_activos['Activo']).index(propiedad_seleccionada))
            nombre = st.text_input("Nombre del Inversionista")
            tel = st.text_input("WhatsApp de Contacto")
            
            if st.form_submit_button("🚀 Enviar Señal al Comandante"):
                nuevo_lead = {'Fecha': datetime.now().strftime("%Y-%m-%d %H:%M"),
                              'Activo_Interes': propiedad, 'Nombre_Cliente': nombre, 'WhatsApp': tel}
                
                if not os.path.exists(LEADS_FILE):
                    pd.DataFrame([nuevo_lead]).to_excel(LEADS_FILE, index=False, engine='openpyxl')
                else:
                    df_l = pd.read_excel(LEADS_FILE, engine='openpyxl')
                    pd.concat([df_l, pd.DataFrame([nuevo_lead])], ignore_index=True).to_excel(LEADS_FILE, index=False, engine='openpyxl')
                st.success(f"Señal registrada. {nombre}, el Comandante ha sido notificado.")

if __name__ == "__main__":
    principal()
