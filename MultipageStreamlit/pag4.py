import streamlit as st
import pandas as pd


def show_footer():
    st.markdown("*ciao*")


def main():
    st.button("Re-run")
    st.title("Questa è nuova")

    ###### footer #####################################
    show_footer()

if __name__ == "__main__":
    main()