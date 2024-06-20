import streamlit as st
import plotly.express as px
import pandas as pd
import seaborn as sns
st.title("Data Analysis")
st.subheader("DA using python and streamline")
st.write("Hello Shubham")
upload = st.file_uploader("Upload your file here")
if upload is not None:
    data = pd.read_csv(upload)

if upload is not None:
    if st.checkbox("Preview data"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())

#check data type of each column
if upload is not None:
    if st.checkbox("data type of each column"):
        st.write(data.dtypes)

#check shape of data set and no of rown and coluns
if upload is not None:
    if st.checkbox("No of rows and columns"):
        st.write("No of rows are", data.shape[0])
        st.write("No of columns are", data.shape[1])


if upload is not None:
    data_shape = st.radio("No of rows and columns",("Rows", "Columns"))
    if data_shape == "Rows":
        st.write("No of rows are", data.shape[0])
        #print(("No of columns are", data.shape[0]))
    if data.shape == "Columns":
        st.write("No of columns are", data.shape[1])
        #print(("No of columns are", data.shape[1]))


if upload is not None:
    test = data.isnull().values.any()
    if test==True:
        if st.checkbox("Null values in dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
            st.set_option('deprecation.showPyplotGlobalUse', False)
    else:
        st.success("No missing value")

#get duplicated values
if upload is not None:
    test = data.duplicated().any()
    if test == True:
        st.warning("This data contain duplicate values")
        dup = st.selectbox("Do you want to remove duplicate", ("Select one", "Yes", "No"))

        if dup == "Yes":
            data= data.drop_duplicates()
            st.text("Duplicate values removed")

        if dup== "No":
            st.text("No worries")
                                                            
#get overall stats
if upload is not None:
    if st.checkbox("Do you want to see overall stat") :
        st.write(data.describe(include="all"))
        
if st.button("About Us"):
    st.text("built with streamlit")

if st.checkbox("By"):
    st.success("Shubham Dalmotra")


        