import streamlit as st
import pandas as pd
import openpyxl as opxl

header = st.container()
dataset = st.container()
features = st.container()

@st.cache_data
def getData(filename):
    userData = pd.read_excel(filename)
    return userData

with header:
    st.title("User Data")


with dataset:
    st.header("Infor LN user dataset")
    st.text("More information about users")
    userData = getData("UsersData05032025.xlsx")
    st.write(userData.head())

    st.subheader("Active users in Infor LN")
    activeUsers = pd.DataFrame(userData['Status'].value_counts()).head(20)
    st.bar_chart(activeUsers)
    
    st.subheader("User Login")
    userLogin = pd.DataFrame(userData['LastLogin'].value_counts()).head(20)
    st.bar_chart(userLogin)

with features:
    st.header("Features")
    st.text("Select information important to you")


