import streamlit as st

st.set_page_config(page_title="To-Do App", page_icon="NoBatidaoCover.jpg", layout="wide")

st.markdown("""
    <style>
    button, .stButton button, div.stButton > button, button[kind="primary"], button[kind="secondary"] {
        background-color: #444;
        color: #fff;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        cursor: pointer;
        font-weight: 600;
        box-shadow: 0px 0px 0px rgba(0,0,0,0);
        transition: all 0.3s ease;
    }

    button:hover, .stButton button:hover, div.stButton > button:hover,
    button[kind="primary"]:hover, button[kind="secondary"]:hover {
        transform: scale(1.05);
        background-color: red !important;
        color: white !important;
        box-shadow: 8px 8px 25px rgba(255,0,0,0.7);
    }

    button:active, .stButton button:active, div.stButton > button:active,
    button[kind="primary"]:active, button[kind="secondary"]:active {
        transform: scale(0.95);
        box-shadow: 2px 2px 5px rgba(255,0,0,0.2);
        transition: all 1s ease;
    }
    </style>
""", unsafe_allow_html=True)

if "to_do_list" not in st.session_state:
    st.session_state.to_do_list = []

with st.form("add_item_form", clear_on_submit=True):
    new_item = st.text_input("Add An Item")
    add_button = st.form_submit_button("Add")
    if add_button and new_item and new_item not in st.session_state.to_do_list:
        st.session_state.to_do_list.append(new_item)

for item in st.session_state.to_do_list:
    st.checkbox(item, key=item)

st.button("Clear All", on_click=lambda: st.session_state.to_do_list.clear())
st.button("Remove One", on_click=lambda: st.session_state.to_do_list.pop() if st.session_state.to_do_list else None)