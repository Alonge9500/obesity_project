import streamlit as st

st.title('Obesity Check')
st.header('Fill in the following details', divider='rainbow')

with st.form('obesity_form',clear_on_submit=True):
    age = st.number_input('Input Age')
    gender = st.radio('Whats your gender',['Female','Male'])
    gender_dictionary = {'Female':0,'Male':1}
    gender = gender_dictionary[gender]

    submit = st.form_submit_button('Submit')

    if submit:
        st.write("Successful")
        st.write(gender)
        st.write(gender_dictionary.items())