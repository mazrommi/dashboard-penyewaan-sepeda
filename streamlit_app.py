import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Sidebar
st.sidebar.image("/Penyewaan Sepeda.png", use_container_width=True)
st.sidebar.title("Pilih Pertanyaan")
# Placeholder untuk dropdown
option = st.sidebar.selectbox(
    "Pilih pertanyaan untuk analisis:",
    options=["Pilih pertanyaan..."] + [
        "Bagaimana pengaruh musim terhadap jumlah penyewaan sepeda?",
        "Bagaimana kondisi cuaca memengaruhi jumlah penyewaan sepeda?"
    ]
)

# Judul aplikasi
st.markdown("""
    <h2 style="text-align: center;">Aplikasi Laporan Penyewaan Sepeda</h2>
    """,unsafe_allow_html=True)
st.markdown("""
    <h4 style="text-align: center;">Aplikasi ini menganalisis pengaruh musim dan kondisi cuaca terhadap jumlah penyewaan sepeda.</h4>
    """,unsafe_allow_html=True)

# Memuat data dari file di direktori
file_path = 'cleaned_day_data.csv'
cleaned_day_data = pd.read_csv(file_path)

# Menampilkan data
st.write("")
st.write("### Dataset : Bike Sharing Dataset")
st.write(cleaned_day_data.head())

#lakukan konversi kolom 'dteday' menjadi tipe data datetime
cleaned_day_data['dteday'] = pd.to_datetime(cleaned_day_data['dteday'])

# Visualisasi tren waktu berdasarkan kolom 'dteday' (bulanan)
cleaned_day_data['month'] = cleaned_day_data['dteday'].dt.to_period('M')
monthly_data = cleaned_day_data.groupby('month')['cnt'].sum().reset_index()

st.write(""" <h3 style="text-align: center;">Tren Penyewaan Sepeda dari Jumlah Total Selama Berbulan-bulan</h3>""",unsafe_allow_html=True)
fig = plt.figure(figsize=(16, 8))  # Ukuran figure diperbesar
plt.plot(monthly_data['month'].astype(str), monthly_data['cnt'], label='Total Count', color='blue', linewidth=2)
plt.title('Time Series Analysis of Total Count Over Months', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Total Count', fontsize=14)

# label sumbu x
ticks = range(0, len(monthly_data), 2)  # Menampilkan label setiap 2 bulan
plt.xticks(ticks=ticks, labels=monthly_data['month'].astype(str)[ticks], rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(alpha=0.5)
plt.legend(fontsize=14)
plt.tight_layout()

# Menampilkan grafik di Streamlit
st.pyplot(fig)
st.write(""" <p style="text-align:justify">- Kenaikan Drastis Terjadi peningkatan besar dari awal 2011 hingga pertengahan tahun 2011 (sekitar Mei-Juni 2011). Ini mungkin menunjukkan adanya musim dengan permintaan tinggi (mungkin musim panas).</p>
        <p style="text-align:justify">- Penurunan Stabil Setelah puncaknya (sekitar pertengahan tahun), total jumlah mulai turun hingga awal 2012.</p>
        <p style="text-align:justify">- Lonjakan Baru pada pertengahan 2012, tetapi tidak sebesar puncak sebelumnya.</p>
        <p style="text-align:justify">- Penurunan Akhir: Penurunan yang cukup signifikan terlihat pada akhir 2012.</p>""",unsafe_allow_html=True)


# Layout visualisasi berdasarkan pertanyaan
if option == "Bagaimana pengaruh musim terhadap jumlah penyewaan sepeda?":
    st.subheader("Pengaruh Musim terhadap Jumlah Penyewaan Sepeda")
    if 'season' in cleaned_day_data.columns and 'cnt' in cleaned_day_data.columns:
        # Visualisasi jumlah penyewaan sepeda berdasarkan musim
        fig1 = plt.figure(figsize=(8, 6))
        sns.barplot(x='season', y='cnt', data=cleaned_day_data, errorbar=None)
        plt.title('Rata-rata Penyewaan Sepeda Berdasarkan Musim')
        plt.xlabel('Musim')
        plt.ylabel('Jumlah Penyewaan Sepeda')
        st.pyplot(fig1)
        st.write(""" <p style="text-align:justify">- Musim Gugur (Fall) Menonjol : Musim gugur memiliki rata-rata penyewaan sepeda tertinggi dibandingkan musim lainnya. Ini menunjukkan bahwa musim gugur adalah musim yang paling populer untuk aktivitas bersepeda. Hal ini mungkin karena suhu yang nyaman dan kondisi cuaca yang relatif stabil.</p>
        <p style="text-align:justify">- Musim Semi (Spring) Terendah : Musim semi memiliki rata-rata penyewaan sepeda terendah. Kemungkinan penyebabnya adalah suhu yang masih dingin di awal musim semi atau kondisi cuaca yang tidak ideal (sering hujan).</p>
        <p style="text-align:justify">- Musim Panas (Summer) dan Musim Dingin (Winter) Stabil : Rata-rata penyewaan sepeda selama musim panas dan musim dingin berada di tengah-tengah, dengan musim panas sedikit lebih tinggi daripada musim dingin. Cuaca yang ekstrem seperti panas tinggi atau dingin yang menusuk dapat memengaruhi keputusan pengguna untuk menyewa sepeda.</p>""",unsafe_allow_html=True)
    else:
        st.write("Kolom 'season' atau 'cnt' tidak ditemukan dalam data.")

elif option == "Bagaimana kondisi cuaca memengaruhi jumlah penyewaan sepeda?":
    st.subheader("Pengaruh Kondisi Cuaca terhadap Jumlah Penyewaan Sepeda")
    if 'weathersit' in cleaned_day_data.columns and 'cnt' in cleaned_day_data.columns:
        # Hubungan antara kondisi cuaca dan jumlah penyewaan sepeda (bar plot)
        fig2 = plt.figure(figsize=(8, 6))
        sns.barplot(x='weathersit', y='cnt', data=cleaned_day_data)
        plt.title('Hubungan Kondisi Cuaca dan Jumlah Penyewaan Sepeda')
        plt.xlabel('Kondisi Cuaca')
        plt.ylabel('Jumlah Penyewaan Sepeda')
        st.pyplot(fig2)
        st.write(""" <p style="text-align:justify">- Cuaca Cerah (Clear) Memiliki Jumlah Penyewaan Tertinggi : Rata-rata penyewaan sepeda tertinggi terjadi saat cuaca cerah, yang mencapai sekitar 5000 penyewaan. Hal ini logis karena cuaca cerah sangat mendukung aktivitas luar ruangan seperti bersepeda.</p>
        <p style="text-align:justify"> - Cuaca Mendung (Cloudy) di Posisi Kedua : Cuaca mendung memiliki rata-rata penyewaan sekitar 4000. Ini menunjukkan bahwa sebagian besar pengguna masih merasa nyaman bersepeda meskipun kondisi cuaca tidak seideal cuaca cerah.</p>
        <p style="text-align:justify">- Cuaca Hujan (Rainy) Memiliki Penyewaan Terendah : Kondisi hujan menunjukkan rata-rata penyewaan paling rendah, sekitar 1800. Hal ini wajar karena hujan cenderung membuat jalan lebih licin dan kurang nyaman untuk bersepeda.</p>
        <p style="text-align:justify"> - Perlu diketahui ada garis Bar Error Menunjukkan Variabilitas, Bar error pada grafik menunjukkan tingkat variabilitas atau penyebaran data penyewaan sepeda untuk setiap kondisi cuaca. Variabilitas ini relatif kecil, menunjukkan pola yang konsisten.</p>""",unsafe_allow_html=True)
    else:
        st.write("Kolom 'weather' atau 'cnt' tidak ditemukan dalam data.")