import streamlit as st
import pandas as pd

def main():
    st.button("Re-run")
    st.title("Questa è la quarta")
    if st.button('check this out', help="Click here"):
        st.write("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
if __name__ == "__main__":
    main()