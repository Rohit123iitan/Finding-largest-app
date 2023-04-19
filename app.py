import streamlit as st
import pandas as pd
import pickle

st.write("""
# Finding largest no App

""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    Number1 = st.number_input("NUMBER1",min_value=-20000,max_value=400000 )
    Number2 = st.number_input("NUMBER2",min_value=-20000,max_value=400000 )
    Number3 = st.number_input("NUMBER3",min_value=-20000,max_value=400000 )
    

    data = {'NUMBER1': Number1,
            'NUMBER2': Number2,
            'NUMBER3': Number3,
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())

#Preprocessing

continous_features = ['NUMBER1','NUMBER2','NUMBER3']

if(df['NUMBER1']>df['NUMBER2'] and df['NUMBER1']>df['NUMBER3']):
    st.write(df['NUMBER1'])
if(df['NUMBER2']>df['NUMBER1'] and df['NUMBER2']>df['NUMBER3']):
    st.write(df['NUMBER2'])
if(df['NUMBER3']>df['NUMBER2'] and df['NUMBER3']>df['NUMBER1']):
    st.write(df['NUMBER3'])
