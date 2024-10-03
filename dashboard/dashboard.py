import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set layout wide
st.set_page_config(layout="wide")

# Fungsi untuk membaca CSV
def load_data(csv_file):
    data = pd.read_csv(csv_file)
    return data

# Sidebar (Bagian kiri)
with st.sidebar:
    st.subheader("Nama: Revan Vio Endriansyah")
    st.subheader("ID Dicoding: revan_vio_endriansyah_TO2K")

# Bagian kanan (konten utama)
st.title("Dicoding Dashboard ✨")

# Menampilkan Data Order
st.subheader("Bike Sharing Dataset")

# Data CSV
csv_file = "../dashboard/all_data.csv"
df_day = load_data(csv_file)

# Membuat layout kolom untuk grafik dan insight
def create_graph_with_insight(graph_func, insight_text):
    col1, col2 = st.columns([1, 1])
    with col1:
        graph_func()
    with col2:
        st.write(insight_text)

# Grafik Distribusi Penyewaan Harian
def plot_distribution():
    plt.figure(figsize=(4, 3))
    sns.histplot(df_day['cnt'], bins=30, kde=True)
    plt.xlabel('Jumlah Penyewaan')
    plt.ylabel('Frekuensi')
    st.pyplot(plt)

insight_distribution = """
Insight dari Histogram Distribusi Jumlah Penyewaan Sepeda\n
    Pola Distribusi:\n
    Terlihat bahwa distribusi jumlah penyewaan sepeda mengikuti bentuk seperti 
    lonceng (bell-shaped), yang menunjukkan bahwa jumlah penyewaan umumnya 
    berkisar pada nilai tengah (sekitar 4000-6000). Terdapat dua puncak yang 
    mungkin mengindikasikan ada hari-hari tertentu dalam seminggu atau bulan 
    ketika jumlah penyewaan lebih tinggi, mungkin pada akhir pekan atau saat 
    cuaca baik.\n
    Frekuensi:\n
    Frekuensi tertinggi terlihat pada jumlah penyewaan antara 3000 hingga 6000, 
    yang menunjukkan bahwa kebanyakan hari memiliki jumlah penyewaan di kisaran 
    tersebut.\n
    Outlier:\n
    Jika ada beberapa bar yang menunjukkan frekuensi tinggi di luar kisaran 
    normal (misalnya, di atas 8000), itu bisa jadi hari-hari spesial atau hari 
    libur di mana penyewaan sepeda meningkat drastis.
"""

create_graph_with_insight(plot_distribution, insight_distribution)

# Grafik Pengaruh Hari Libur
def plot_holiday_effect():
    plt.figure(figsize=(4, 3))
    sns.boxplot(data=df_day, x='holiday', y='cnt', palette='Set2')
    plt.xlabel('Hari Libur Nasional')
    plt.ylabel('Jumlah Penyewaan')
    st.pyplot(plt)

insight_holiday_effect = """
Insight dari Rata-rata Jumlah Penyewaan Sepeda dengan Hari\n
    Rata-rata penyewaan pada Hari Libur: 3735.00\n
    Rata-rata penyewaan sepeda pada hari libur nasional relatif lebih rendah 
    dibandingkan dengan hari biasa. Ini menunjukkan bahwa meskipun hari libur 
    mungkin memiliki lebih banyak waktu luang untuk beraktivitas, mungkin 
    terdapat faktor lain yang memengaruhi jumlah penyewaan sepeda, seperti 
    cuaca, perayaan, atau pilihan transportasi alternatif yang lebih populer 
    saat libur.
    
    Rata-rata Penyewaan pada Hari Biasa: 4527.10\n
    Rata-rata penyewaan sepeda pada hari biasa lebih tinggi, yang mungkin
    menunjukkan bahwa sepeda sering digunakan sebagai alat transportasi untuk
    keperluan sehari-hari, seperti pergi bekerja atau bersekolah. Hal ini 
    menunjukkan bahwa sepeda lebih banyak digunakan dalam rutinitas sehari-hari 
    dibandingkan pada hari libur.
"""

create_graph_with_insight(plot_holiday_effect, insight_holiday_effect)

# Grafik Hubungan antara Suhu dan Penyewaan
def plot_temperature_effect():
    plt.figure(figsize=(4, 3))
    sns.scatterplot(data=df_day, x='temp', y='cnt', hue='weathersit', palette='viridis')
    plt.xlabel('Suhu (Normalized)')
    plt.ylabel('Jumlah Penyewaan')
    st.pyplot(plt)

insight_temperature_effect = """
Insight dari Rata-rata Jumlah Penyewaan Sepeda dengan Suhu\n
    Hubungan Positif Antara Suhu dan Penyewaan: \n
    Terlihat ada korelasi positif antara suhu (sumbu X) dan jumlah penyewaan 
    sepeda (sumbu Y). Semakin tinggi suhu, semakin banyak sepeda yang disewa. 
    Ini mungkin karena cuaca yang lebih hangat membuat aktivitas luar ruangan 
    lebih menyenangkan.
    
    Pengaruh Kondisi Cuaca (weathersit):\n
    Warna ungu (label 1) yang mewakili kondisi cuaca yang baik (umumnya cerah 
    atau sedikit berawan) mendominasi jumlah penyewaan yang tinggi, menunjukkan 
    bahwa kondisi cuaca yang baik sangat berpengaruh pada jumlah penyewaan.Warna
    hijau (label 2) yang mewakili cuaca sedang (berawan atau kondisi mendung ringan)
    juga menunjukkan jumlah penyewaan yang relatif signifikan, tetapi tidak sebanyak
    cuaca cerah.Warna kuning (label 3) yang menunjukkan cuaca buruk (hujan atau kondisi 
    ekstrem) memiliki jumlah penyewaan yang paling rendah. Ini menunjukkan bahwa kondisi 
    cuaca buruk sangat menurunkan minat untuk menyewa sepeda.
    
    Penyewaan Maksimal pada Suhu Optimal: 
    Meski ada korelasi positif, tampaknya ada batas optimal pada suhu sekitar 0.6-0.7 
    (setelah dinormalisasi). Pada suhu yang lebih tinggi dari ini, jumlah penyewaan mulai
    menurun. Hal ini mungkin disebabkan oleh suhu yang terlalu panas, yang membuat orang 
    enggan beraktivitas di luar.
"""

create_graph_with_insight(plot_temperature_effect, insight_temperature_effect)

