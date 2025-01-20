import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("dashboard/cleaned_day_data.csv")

# Dashboard Title
st.title("Dashboard Penyewaan Sepeda")

# Sidebar filters
season = st.sidebar.selectbox("Pilih Musim:", data['season'].unique())
weather = st.sidebar.selectbox("Pilih Kondisi Cuaca:", data['weathersit'].unique())

# Filter data
filtered_data = data[(data['season'] == season) & (data['weathersit'] == weather)]

# Display filtered data
st.write("Data yang difilter berdasarkan pilihan Anda:")
st.dataframe(filtered_data)

# Visualisasi rata-rata penyewaan
st.subheader("Rata-rata Penyewaan Berdasarkan Musim")
average_rentals = data.groupby('season')['cnt'].mean()
fig, ax = plt.subplots()
sns.barplot(x=average_rentals.index, y=average_rentals.values, ax=ax)
ax.set_title("Rata-rata Penyewaan Sepeda per Musim")
ax.set_xlabel("Musim")
ax.set_ylabel("Rata-rata Penyewaan")
st.pyplot(fig)
