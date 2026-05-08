import streamlit as st
import pandas as pd
import joblib

# load model
model = joblib.load("model_laba.pkl")

# judul dashboard
st.title("Dashboard Prediksi LABA")

# input user
pendapatan = st.number_input(
    "Masukkan Pendapatan",
    min_value=0.0
)

biaya = st.number_input(
    "Masukkan Biaya",
    min_value=0.0
)

# tombol prediksi
if st.button("Prediksi"):

    # membuat dataframe baru
    data = pd.DataFrame({
        "PENDAPATAN": [pendapatan],
        "BIAYA": [biaya]
    })

    # prediksi
    hasil = model.predict(data)

    # tampilkan hasil
    st.success(
        f"Prediksi LABA: Rp {hasil[0]:,.0f}"
    )