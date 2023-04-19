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
font_size=30
font_color="blue"
st.subheader('The Largest Number is :')
if(df['NUMBER1'][0]>df['NUMBER2'][0] and df['NUMBER1'][0]>df['NUMBER3'][0]):
    html_str = f"""<style>p.a {{color: {font_color};font: bold {font_size}px Courier;}}</style><p class="a">{df['NUMBER1'][0]}</p>"""
    st.markdown(html_str, unsafe_allow_html=True)
if(df['NUMBER2'][0]>df['NUMBER1'][0] and df['NUMBER2'][0]>df['NUMBER3'][0]):
    html_str = f"""<style>p.a {{color: {font_color};font: bold {font_size}px Courier;}}</style><p class="a">{df['NUMBER2'][0]}</p>"""
    st.markdown(html_str, unsafe_allow_html=True)
if(df['NUMBER3'][0]>df['NUMBER2'][0] and df['NUMBER3'][0]>df['NUMBER1'][0]):
    html_str = f"""<style>p.a {{color: {font_color};font: bold {font_size}px Courier;}}</style><p class="a">{df['NUMBER3'][0]}</p>"""
    st.markdown(html_str, unsafe_allow_html=True)
    
if(df['NUMBER1'][0]==df['NUMBER2'][0] and df['NUMBER1'][0]>df['NUMBER3'][0]):
    html_str = f"""<style>p.a {{color: {font_color};font: bold {font_size}px Courier;}}</style><p class="a">{df['NUMBER1'][0]}</p>"""
    st.markdown(html_str, unsafe_allow_html=True)
elif(df['NUMBER1'][0]==df['NUMBER2'][0] and df['NUMBER1'][0]<df['NUMBER3'][0]):
    html_str = f"""<style>p.a {{color: {font_color};font: bold {font_size}px Courier;}}</style><p class="a">{df['NUMBER3'][0]}</p>"""
    st.markdown(html_str, unsafe_allow_html=True)
elif(df['NUMBER1'][0]==df['NUMBER3'][0] and df['NUMBER1'][0]>df['NUMBER2'][0]):
    html_str = f"""<style>p.a {{color: {font_color};font: bold {font_size}px Courier;}}</style><p class="a">{df['NUMBER1'][0]}</p>"""
    st.markdown(html_str, unsafe_allow_html=True)
elif(df['NUMBER1'][0]==df['NUMBER3'][0] and df['NUMBER1'][0]<df['NUMBER2'][0]):
    html_str = f"""<style>p.a {{color: {font_color};font: bold {font_size}px Courier;}}</style><p class="a">{df['NUMBER2'][0]}</p>"""
    st.markdown(html_str, unsafe_allow_html=True)
elif(df['NUMBER1'][0]==df['NUMBER3'][0] and df['NUMBER1'][0]==df['NUMBER2'][0]):
    html_str = f"""<style>p.a {{color: {font_color};font: bold {font_size}px Courier;}}</style><p class="a">{df['NUMBER1'][0]}</p>"""
    st.markdown(html_str, unsafe_allow_html=True)

