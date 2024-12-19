import streamlit as st

st.set_page_config(
    page_title = "WineMaps",
    page_icon = '🍷',
    layout = "wide"
)

with open('spainWineMap.html', 'r') as f:
    st.components.v1.html(f.read(), height=800)