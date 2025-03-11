import streamlit as st
import pandas as pd
import openpyxl as opxl

header = st.container()
dataset = st.container()
features = st.container()

with header:
    st.title("User Data")


with dataset:
    st.header("Infor LN user dataset")
    st.text("More information about users")
    #userData = opxl.open('UsersData05032025.xlsx')
    userData = pd.read_csv('UsersData05032025.csv')
    st.write(userData.head())
    

with features:
    st.header("Features")
    st.text("Select information important to you")


