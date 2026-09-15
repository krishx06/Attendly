import base64
import streamlit as st


def get_logo_data_url():
    try:
        with open("src/logo/attendly_image.png", "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
            return f"data:image/png;base64,{encoded}"
    except Exception:
        return "https://i.ibb.co/YTYGn5qV/logo.png"


def header_home():
    logo_data_url = get_logo_data_url()
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src='{logo_data_url}' style='height:100px; object-fit:contain;' />
            <h1 style='text-align:center; color:#E0E3FF; font-weight:800; margin-top:10px;'>ATTENDLY</h1>
        </div>   
    """, unsafe_allow_html=True)


def header_dashboard():
    logo_data_url = get_logo_data_url()
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:15px">
            <img src='{logo_data_url}' style='height:85px; object-fit:contain;' />
            <h2 style='text-align:left; color:#5865F2 !important; font-weight:800; margin:0;'>ATTENDLY</h2>
        </div>   
    """, unsafe_allow_html=True)
