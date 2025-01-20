import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("cleaned_day_data.csv")

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

# Visualisasi rata-rata penyewaan berdasarkan filter
st.subheader("Rata-rata Penyewaan Berdasarkan Musim dan Kondisi Cuaca")
if not filtered_data.empty:
    average_rentals = filtered_data.groupby('season')['cnt'].mean()
    fig, ax = plt.subplots()
    sns.barplot(x=average_rentals.index, y=average_rentals.values, ax=ax)
    ax.set_title("Rata-rata Penyewaan Sepeda per Musim (Filter: Kondisi Cuaca)")
    ax.set_xlabel("Musim")
    ax.set_ylabel("Rata-rata Penyewaan")
    st.pyplot(fig)
else:
    st.write("Tidak ada data yang sesuai dengan filter.")

# Visualisasi tambahan untuk pertanyaan kedua
st.subheader("Distribusi Penyewaan Sepeda Harian")
fig2, ax2 = plt.subplots()
sns.histplot(data=filtered_data, x='cnt', bins=20, kde=True, ax=ax2)
ax2.set_title("Distribusi Penyewaan Sepeda Harian (Filter Aktif)")
ax2.set_xlabel("Jumlah Penyewaan")
ax2.set_ylabel("Frekuensi")
st.pyplot(fig2)
