import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background:white; border-left: 8px solid #EB459E; padding:25px; border-radius: 20px; border: 1px solid black; margin-bottom:20px;">
        <h3 style="margin:0; color: #1e293b; font-size: 1.5rem ">{name}</h3>
        <p style="color:#64748b; margin:10px 0;">Code : <span style="background:#E0E3FF; color:#5865F2; padding:2px 8px; border-radius:5px;">{code} </span> | Section : {section}</p>
        
        """
    
    if stats:
        html += """
        <div style="display:flex; gap:10px; flex-wrap:wrap; margin-top:12px;">
        """
        for icon, label, value in stats:
            html += f'<div style="background: #FCE7F3; color: #831843; padding: 6px 14px; border-radius: 12px; font-size: 0.92rem; font-weight: 600; display: flex; align-items: center; gap: 4px;"><span>{icon}</span> <b style="color: #9D174D;">{value}</b> <span>{label}</span></div>'
        
        html += "</div>"

    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
