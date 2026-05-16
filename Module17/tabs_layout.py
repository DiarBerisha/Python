import streamlit as st

tab1, tab2, tab3 = st.tabs(["Tab1", "Tab2", "Tab 3"])

with tab1:
    st.header("Content for Tab 1")
    st.write("Text for Tab 1")

with tab2:
    st.header("Content for Tab 2")
    st.write("Text for Tab 2")

with tab3:
    st.header("Content for Tab 3")
    st.write("Text for Tab 3")