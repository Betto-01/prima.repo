import streamlit as st
import pandas as pd

def main():
    st.button("Re-run")
    st.title("Questa è la prima")
    st.markdown('Streamlit is _really_ **cool**.')
    st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
    st.markdown(":green[$\sqrt{x^3+y^2}=1$] is a Pythagorean identity. :pencil:")

if __name__ == "__main__":
    main()