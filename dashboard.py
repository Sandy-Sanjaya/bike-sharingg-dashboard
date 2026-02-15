import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================
st.set_page_config(
    page_title="Bike Sharing Demand Dashboard",
    layout="wide"
)

st.title("🚴 Bike Sharing Demand Analysis (2011–2012)")
st.markdown(
    "Dashboard ini menampilkan analisis pola penyewaan sepeda "
    "berdasarkan jenis hari, musim, dan tipe pengguna."
)

# =====================================================
# LOAD DATA
# =====================================================
day_df = pd.read_csv("day.csv")
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# =====================================================
# SIDEBAR – DATE FILTER
# =====================================================
st.sidebar.header("📅 Filter Berdasarkan Tanggal")

min_date = day_df['dteday'].min()
max_date = day_df['dteday'].max()

start_date = st.sidebar.date_input(
    "Start Date",
    min_value=min_date,
    max_value=max_date,
    value=min_date
)

end_date = st.sidebar.date_input(
    "End Date",
    min_value=min_date,
    max_value=max_date,
    value=max_date
)

# Filter dataset berdasarkan tanggal
filtered_df = day_df[
    (day_df['dteday'] >= pd.to_datetime(start_date)) &
    (day_df['dteday'] <= pd.to_datetime(end_date))
]

# =====================================================
# DATA MAPPING
# =====================================================
workingday_map = {0: "Akhir Pekan / Libur", 1: "Hari Kerja"}

season_map = {
    1: "Spring",
    2: "Summer",
    3: "Fall",
    4: "Winter"
}

filtered_df['workingday'] = filtered_df['workingday'].map(workingday_map)
filtered_df['season'] = filtered_df['season'].map(season_map)

# =====================================================
# KPI
# =====================================================
st.subheader("📌 Ringkasan Periode Terpilih")

col1, col2 = st.columns(2)

col1.metric("Total Penyewaan", int(filtered_df['cnt'].sum()))
col2.metric("Rata-rata Harian", int(filtered_df['cnt'].mean()))

st.markdown("---")

# =====================================================
# 1️⃣ WORKINGDAY VS WEEKEND
# =====================================================
st.subheader("1️⃣ Perbedaan Rata-rata Penyewaan: Hari Kerja vs Akhir Pekan")

workingday_avg = filtered_df.groupby(
    'workingday', as_index=False
)['cnt'].mean()

fig1 = px.bar(
    workingday_avg,
    x='workingday',
    y='cnt',
    color='workingday',
    labels={'workingday': 'Jenis Hari', 'cnt': 'Rata-rata Penyewaan'},
    title="Rata-rata Penyewaan Berdasarkan Jenis Hari"
)

st.plotly_chart(fig1, use_container_width=True)

st.caption(
    "Insight: Perbandingan ini menunjukkan bagaimana pola permintaan "
    "berbeda antara hari kerja dan akhir pekan."
)

st.markdown("---")

# =====================================================
# 2️⃣ POLA MUSIM
# =====================================================
st.subheader("2️⃣ Pola Rata-rata Penyewaan Berdasarkan Musim")

season_avg = filtered_df.groupby(
    'season', as_index=False
)['cnt'].mean()

fig2 = px.bar(
    season_avg,
    x='season',
    y='cnt',
    color='season',
    labels={'season': 'Musim', 'cnt': 'Rata-rata Penyewaan'},
    title="Rata-rata Penyewaan Berdasarkan Musim"
)

st.plotly_chart(fig2, use_container_width=True)

st.caption(
    "Insight: Visualisasi ini membantu mengidentifikasi musim dengan "
    "permintaan tertinggi dan terendah."
)

st.markdown("---")

# =====================================================
# 3️⃣ CASUAL VS REGISTERED
# =====================================================
st.subheader("3️⃣ Kontribusi Penyewaan: Casual vs Registered")

user_contribution = pd.DataFrame({
    "Tipe Pengguna": ["Casual", "Registered"],
    "Total Penyewaan": [
        filtered_df['casual'].sum(),
        filtered_df['registered'].sum()
    ]
})

fig3 = px.pie(
    user_contribution,
    names="Tipe Pengguna",
    values="Total Penyewaan",
    title="Kontribusi Total Penyewaan Berdasarkan Tipe Pengguna"
)

st.plotly_chart(fig3, use_container_width=True)

st.caption(
    "Insight: Diagram ini menunjukkan tipe pengguna yang mendominasi "
    "total permintaan selama periode terpilih."
)

# =====================================================
# KESIMPULAN
# =====================================================
st.markdown("---")
st.markdown(
    "### 📊 Kesimpulan\n"
    "- Permintaan sepeda menunjukkan perbedaan antara hari kerja dan akhir pekan.\n"
    "- Musim tertentu memiliki tingkat permintaan yang lebih tinggi dibandingkan lainnya.\n"
    "- Pengguna registered cenderung mendominasi total penyewaan.\n\n"
    "Dashboard ini membantu memahami pola permintaan secara lebih fokus dan interaktif."
)
