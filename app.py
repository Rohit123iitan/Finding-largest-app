import streamlit as st
import pandas as pd
import pickle

st.write("""
# Finding largest no App

""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    Number1 = st.number_input("NUMBER 1",min_value=-20000,max_value=400000 )
    Number2 = st.number_input("NUMBER 2",min_value=-20000,max_value=400000 )
    Number3 = st.number_input("NUMBER 3",min_value=-20000,max_value=400000 )
    

    data = {'NUMBER1': Number1,
            'NUMBER2': Number2,
            'NUMBER3': Number3,
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()


#Preprocessing

continous_features = ['NUMBER1','NUMBER2','NUMBER3']
st.subheader('The Largest Number is :')
if(df['NUMBER1'][0]>df['NUMBER2'][0] and df['NUMBER1'][0]>df['NUMBER3'][0]):
    st.write(df['NUMBER1'][0])
if(df['NUMBER2'][0]>df['NUMBER1'][0] and df['NUMBER2'][0]>df['NUMBER3'][0]):
    st.markdown("**:blue[{df['NUMBER2'][0]}]**" )
if(df['NUMBER3'][0]>df['NUMBER2'][0] and df['NUMBER3'][0]>df['NUMBER1'][0]):
    st.write(df['NUMBER3'][0])
