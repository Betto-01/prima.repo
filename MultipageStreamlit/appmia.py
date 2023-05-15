import streamlit as st
from pag5 import main as  pag5
from pag6 import main as  pag6
from pag7 import main as  pag7
from pag8 import main as  pag8

def main():
	################ load image from web #########################
	from PIL import Image
	import requests
	from io import BytesIO
	st.title("My multipage APP")

				
	pag_name = ["pag5","pag6","pag7","pag8"]
	
	OPTIONS = pag_name
	sim_selection = st.selectbox('Seleziona la pagina', OPTIONS)

	if sim_selection == pag_name[0]:
		pag5()
	elif sim_selection == pag_name[1]:
		pag6()
	elif sim_selection == pag_name[2]:
		pag7()
	elif sim_selection == pag_name[3]:
		pag8()
	else:
		st.markdown("Something went wrong. We are looking into it.")


if __name__ == '__main__':
	main()