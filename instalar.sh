#!/bin/bash
echo "--- INICIANDO INSTALACION EN MACBOOK ---"
sudo apt update && sudo apt install python3-pip python3-venv libgl1-mesa-glx libglib2.0-0 -y
python3 -m venv venv
source venv/bin/activate
pip install streamlit opencv-python numpy
echo "--- INSTALACION COMPLETA. ARRANCANDO ---"
streamlit run main.py
