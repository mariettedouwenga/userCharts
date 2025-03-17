import streamlit as st
import pandas as pd
import openpyxl as opxl
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import datetime as dt

header = st.container()
dataset = st.container()

#print(userData.info())
#print(userData.duplicated())

@st.cache_data
def getData(filename):
    userData = pd.read_excel(filename)
    return userData

@st.cache_data
def getLoginCreateData(filename):
    userLoginCreate = pd.read_excel(filename)
    return userLoginCreate

@st.cache_data
def getLogin(filename):
    userLogin = pd.read_excel(filename)
    return userLogin

@st.cache_data
def getCreate(filename):
    userCreate = pd.read_excel(filename)
    return userCreate

@st.cache_data
def getLoginDept(filename):
    deptLogin = pd.read_excel(filename)
    return deptLogin

with header:
    st.title("Infor LN User Data")

with dataset:
    #st.header("Infor LN user dataset")
    st.text("Data exported from OS -> Security -> Admin long running actions")
    st.text("The information provided includes data spanning from 2024 to 2025. Upon review, it was evident that the data required significant cleanup.")
    st.divider()

    userData = getData("UsersData05032025.xlsx")

    #Adding colums for Creation Date (year, month, day) to the userData dataframe
    #Add column cYear to the userData table to extract the year from the Created Date column
    userData.loc[:,"cYear"] = userData["Created Date"].dt.year
    #Add column lYear to the userData table to extract the year form the LastLogin Date column
    userData.loc[:,"lYear"] = userData["LastLogin Date"].dt.year
    st.divider

#New dataset USER LOGIN per day
    userLogin = getCreate("UserLogin.xlsx")    

    #Adding colums for Creation Date (year, month, day) to the userData dataframe
    userLogin.loc[:,"ulYear"] = userLogin["LoginDate"].dt.year

    print(userLogin.columns.tolist())
    print(userLogin.info())
    #st.write(userLogin)

    #Filter by year and show how many users login per day
    st.subheader("Infor LN users login per day")
    
    ulyear_options = userLogin["ulYear"].unique().tolist()
    ulyear = st.selectbox('Which year would you like to see?', ulyear_options, 0, key="loggers")

    #Filter the dataset 
    userLogin = userLogin[userLogin["ulYear"] == ulyear]

    fig_ulYear = px.line(userLogin, y="UsersLoggedIn", x="LoginDate", range_y=[0,200])
    fig_ulYear.update_layout(width=800)
    st.write(fig_ulYear)
    st.divider

#New dataset USER CREATED per day
    userCreate = getCreate("UserCreate.xlsx")    

    #Adding colums for Creation Date (year, month, day) to the userData dataframe
    userCreate.loc[:,"cdYear"] = userCreate["CreateDate"].dt.year

    print(userCreate.columns.tolist())
    print(userCreate.info())
    #st.write(userCreate)

    #Filter by year and show how many users login per day
    st.subheader("Infor LN users created per day")
    cdyear_options = userCreate["cdYear"].unique().tolist()
    cdyear = st.selectbox('Which year would you like to see?', cdyear_options, 0, key="created#")

    #Filter the dataset 
    userCreate = userCreate[userCreate["cdYear"] == cdyear]

    fig3_cdYear = px.line(userCreate, y="UserCreated", x="CreateDate", range_y=[0,350])

    fig3_cdYear.update_layout(width=800)
    st.write(fig3_cdYear)

    st.text("On July 18, 2024, an outlier of 1,553 users was recorded, and on March 21, 2024, another outlier of 2,520 users was observed. These figures are not depicted in the graphic for visualization purposes.")
    st.text("An average of 7 users were created per day in 2024")
    st.divider
    
#Active USERS PER DEPARTMENT according to created date
    deptLogin = getLoginDept("Department.xlsx")
    deptLogin.loc[:,"ldeptYear"] = deptLogin["CreatedDateOnly"].dt.year

    #st.write(deptLogin)

    #Filter by year and show how many users login per day
    st.subheader("Infor LN Active Users per Department")
    ldDept_options = deptLogin["ldeptYear"].unique().tolist()

    ldDept = st.selectbox('Which year would you like to see?', ldDept_options, 0, key="Department")

    #Filter the dataset 
    deptLogin = deptLogin[deptLogin["ldeptYear"] == ldDept]

    fig_Dept = px.bar(deptLogin, y="DeptCount", x="DeptFinal", range_y=[0,100])

    fig_Dept.update_layout(width=800)
    st.write(fig_Dept)

        