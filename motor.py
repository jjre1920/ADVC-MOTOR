import streamlit as st
import pandas as pd

st.set_page_config(page_title="ADVANCE - Realty Portal", layout="wide", page_icon="🏘️")

def principal():
    st.title("⚡ ADVANCE GLOBAL - Intelligence & Logistics")
    
    # --- PESTAÑAS DE OPERACIÓN ---
    tab1, tab2 = st.tabs(["🛰️ Radar Global", "🏘️ Registro de Realties"])

    with tab2:
        st.header("📝 Registro de Nueva Propiedad")
        st.write("Ingrese los datos para vincular la propiedad al radar de ADVANCE.")
        
        with st.form("realty_form", clear_on_submit=True):
            col_a, col_b = st.columns(2)
            with col_a:
                realty_name = st.text_input("Nombre de la Inmobiliaria")
                propiedad_titulo = st.text_input("Título de la Propiedad (Ej. Casa Vista Mar)")
                tipo = st.selectbox("Tipo de Activo", ["Residencial VIP", "Terreno Comercial", "Hacienda", "Otro"])
            with col_b:
                precio_realty = st.number_input("Precio de Lista (USD)", min_value=0)
                contacto = st.text_input("WhatsApp de Contacto")
                ubicacion_txt = st.text_input("Referencia de Ubicación (Ej. Sector Bahía)")

            st.write("📍 **Coordenadas para el Radar**")
            c_lat, c_lon = st.columns(2)
            lat_in = c_lat.number_input("Latitud Exacta", value=27.9500, format="%.6f")
            lon_in = c_lon.number_input("Longitud Exacta", value=-111.0500, format="%.6f")
            
            descripcion = st.text_area("Descripción de la Propiedad")
            
            submit = st.form_submit_button("🚀 Subir al Radar ADVANCE")

            if submit:
                st.success(f"✅ ¡{propiedad_titulo} ha sido vinculada con éxito por {realty_name}!")
                st.balloons()

    with tab1:
        st.subheader("🛰️ Monitoreo de Nodos y Activos VIP")
        # Aquí se mostrarán los activos subidos
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Unidades en Puente", "385", "Activas")
        col2.metric("Propiedades Online", "25", "+1")
        col3.metric("Flujo de Datos", "1.2 GB/s", "Estable")
        col4.metric("Seguridad", "Encriptado", "AES-256")
        
        # Mapa que muestra la última propiedad registrada o base
        mapa_data = pd.DataFrame({'lat': [27.95, 27.92, 28.00], 'lon': [-111.05, -110.90, -110.95]})
        st.map(mapa_data)

if __name__ == "__main__":
    principal()
