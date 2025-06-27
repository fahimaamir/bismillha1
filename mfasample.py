import streamlit.components.v1 as components
import pandas as pd
import streamlit as st
from pivottablejs import pivot_ui
if 'newrecord' not in st.session_state:
    st.session_state.newrecord = 0


st.set_page_config(layout="wide")



#url12 = "https://docs.google.com/spreadsheets/d/1TrljfQUEw2cEiYUOyXXfH7u0VF0IDARZ/edit?usp=sharing&ouid=105182257404870437876&rtpof=true&sd=true"
#url12 = "https://docs.google.com/spreadsheets/d/1j4zRBnAb1nXi4NMMC8NEnEZMBVTW2oje/edit?usp=sharing&ouid=105182257404870437876&rtpof=true&sd=true"
url12 = "https://docs.google.com/spreadsheets/d/1j4zRBnAb1nXi4NMMC8NEnEZMBVTW2oje/edit?pli=1&gid=92713901#gid=92713901"
file_id122 = url12.split("/")[-2]
path1122 = "https://drive.google.com/uc?export=download&id=" + file_id122
            #sce = pd.read_excel(path1)
iqradata = pd.read_excel(path1122)

        #st.write(st.session_state.df92 )
        #datag = st.session_state.df92


#@st.cache_data()
def load_data():
    #data = pd.read_excel("C:/mfa/exportpv.xlsx")
    #data = pd.read_excel('c:\mfa\iqradata.xlsx')
    data= iqradata
    #data = pd.read_csv("./data.csv", parse_dates=["referenceDate"])
    return data

data = load_data()



#tab1, tab2, tab3, tab4 = st.tabs(["View-1", "View-2", "View-3", "View-4"])


t = pivot_ui(data)

with open(t.src) as t:
        components.html(t.read(), width=900, height=1000, scrolling=True)


