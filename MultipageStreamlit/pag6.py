import streamlit as st
import pandas as pd

def main():
    st.button("Re-run")
    st.title("Questa è la seconda :sunglasses:")
    x1 = st.slider('Please inserisci lato1 cubo', 0, 100, 25)
    x2 = st.slider('Please inserisci lato2 cubo', 0, 100, 35)
    x3 = st.slider('Please inserisci lato3 cubo', 0, 100, 15)
    
    def area(l1:float,l2:float,l3:float):
        a = l1*l2*l3/10000
        return a 
    st.write("l'area cubo è ", area(x1,x2,x3),'metri quadrati')
 
if __name__ == "__main__":
    main()