# 🚲 Bike Sharing Interactive Dashboard

Bike Sharing Interactive Dashboard merupakan proyek analisis data yang bertujuan untuk memahami pola penggunaan sepeda berdasarkan **waktu**, **jenis hari**, **kondisi cuaca**, dan **tipe pengguna**.  
Proyek ini menyajikan hasil **Exploratory Data Analysis (EDA)** dalam bentuk dashboard interaktif menggunakan **Streamlit**, sehingga insight dapat dipahami dengan lebih mudah dan visual.

---

## 📊 Dataset

Dataset yang digunakan adalah **Bike Sharing Dataset**, yang terdiri dari dua file utama:

- `hour.csv` → Data penyewaan sepeda per jam  
- `day.csv` → Data penyewaan sepeda per hari  

Beberapa variabel penting dalam dataset:
- `cnt` : total jumlah penyewaan sepeda  
- `casual` : jumlah pengguna tidak terdaftar  
- `registered` : jumlah pengguna terdaftar  
- Variabel waktu (jam, hari, bulan)
- Variabel kondisi cuaca dan jenis hari

---

## 🛠️ Setup Environment

### Setup Environment - Anaconda
```
conda create --name bike-sharing-ds python=3.10
conda activate bike-sharing-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```
## Run steamlit app
```
streamlit run dashboard/dashboard.py
```

