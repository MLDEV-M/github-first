# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 12:22:18 2025

@author: mcharalambous35

streamlit run streamlit.py
"""
#pip install streamlit

import streamlit as st
import pandas as pd


st.title("my best week")
st.write("My weekly program")

# buton
if st.button('click me'):
    st.write('gdfgdfg')

# text input
name = st.text_input('enter name:')
st.write(f"hsdfd {name}")

# slider start point = 5
age = st.slider('select age',0,100,5)
st.write(f'dfsf {age}')

# select option
option = st.selectbox("sfdrgdfg a s",{1,5,66,435})
st.write(option)

agree = st.checkbox('i agree')
if agree:
    st.write('procees')

data = pd.DataFrame({
    'A':[1,2,3],
    'B':[4,5,6]}
)
st.write(data)