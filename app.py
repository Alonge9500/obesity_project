import streamlit as st
import pickle
import numpy as np


#Load all pickle files 

with open ('encoding_dict.pkl','rb') as encoder_file:
    encoding_dict = pickle.load(encoder_file)

with open ('gradientboosting.pkl','rb') as gradientboosting_file:
    model = pickle.load(gradientboosting_file)

with open ('scaler.pkl','rb') as scaler_file:
    scaler = pickle.load(scaler_file)

#Start Streamlit APP

st.title('Obesity Check')
st.header('Fill in the following details', divider='rainbow')


def key_extractor(column_name):
    """ Extract Keys from Encoding Dictionary
    return: A list of key
    
    """
    return list(encoding_dict[column_name].keys())
def value_extractor(column_name,key_name):
    """ Extract Values from Encoding dictionary
        return: Corresponding value for key
    """
    return encoding_dict[column_name][key_name]


with st.form('obesity_form',clear_on_submit=True):
    age = st.number_input('Input Age')
    gender = st.radio('Whats your gender',key_extractor('Gender'))
    gender = value_extractor('Gender',gender)

    height = st.number_input('Input Your Height in Meters')
    weight = st.number_input('Input Weight in Kg')

    favc_key = st.selectbox('Do you eat high caloric food frequently?',key_extractor('FAVC'))
    favc = value_extractor('FAVC',favc_key)

    fcvc = st.number_input('Do you usually eat vegetables in your meals? Between 1-3')
    ncp = st.number_input('How many main meals do you have daily? Between 1-4')

    scc_key = st.selectbox('Do you usually eat vegetables in your meals?',key_extractor('SCC'))
    scc = value_extractor('SCC',scc_key)

    smoke_key = st.radio('Do you Smoke?',key_extractor('SMOKE'))
    smoke = value_extractor('SMOKE',smoke_key)

    h2o = st.number_input('How much water do you drink daily? In litres Between 1-3')

    family_history_with_overweight_key = st.radio('Do you have family history of obesity',key_extractor('family_history_with_overweight'))
    family_history_with_overweight = value_extractor('family_history_with_overweight',family_history_with_overweight_key)

    faf = st.number_input('How often do you have physical activity? Between 0-3')
    tue = st.number_input('How much time do you use technological devices such as cell phone, videogames, television, computer and others? Between 0-3')

    calc_key = st.selectbox('How often do you drink alcohol?',key_extractor('CALC'))
    calc = value_extractor('CALC',calc_key)

    caec_key = st.selectbox('Do you eat any food between meals?',key_extractor('CAEC'))
    caec = value_extractor('CAEC',caec_key)

    mtrans_key = st.selectbox('Which transportation do you usually use?',key_extractor('MTRANS'))
    mtrans = value_extractor('MTRANS',mtrans_key)


    submit = st.form_submit_button('Submit')

    if submit:
        data = [age,gender,height,weight,favc,fcvc,ncp,scc,smoke,h2o,family_history_with_overweight,faf,tue,calc,caec,mtrans]
        data = np.array(data).reshape(1,-1)
        data = scaler.transform(data)

        def extract_class(value):
            obese_dict = {value:key for key,value in encoding_dict['NObeyesdad'].items()}

            return obese_dict[value]


        prediction = model.predict(data)
        prediction = extract_class(prediction[0])
        proba = model.predict_proba(data)

        st.markdown(f'Your weight classification is {prediction}')
        st.markdown(proba)
        