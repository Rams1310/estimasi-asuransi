import pickle
import streamlit as st
import numpy as np

model = pickle.load (open('estimasi_asuransi.sav', 'rb'))

st.title('estimasi biaya asuransi kesehatan')
st.write('masukkan parameter di bawah ini untuk menghitung estimasi biaya asuransi.')

age = st.number_input('Input Usia (Tahun)', min_value=18, max_value=100, value=30)
bmi = st.number_input('Input BMI (Indeks Massa Tubuh)', min_value=10.0, max_value=60.0, value=28.5)
children = st.number_input('Input Jumlah Anak / Tanggungan', min_value=0, max_value=10, value=1)
smoker_option = st.selectbox('Apakah Perokok?', ('Tidak', 'Ya'))

smoker = 1 if smoker_option == 'Ya' else 0

if st.button('Estimasi Biaya'):
    input_data = np.array([[age, bmi, children, smoker]])
    prediction = model.predict(input_data)
    
    usd = prediction[0]
    idr = usd * 18000  
    
    st.success(f'Estimasi Biaya Asuransi (USD): $ {usd:,.2f}')
    st.info(f'Estimasi Biaya Asuransi (IDR): Rp {idr:,.0f}')
    