Aplikasi Prediksi Gagal Jantung berdasarkan indikator-indikator penyakit jantung.

Dibuat berdasarkan permasalahan tingginya kematian akan gagal jantung bahkan mencapai penyebab no 1
kematian di seluruh dunia.

Data untuk perlatihan dibuat menggunakan dataset dari Kaagle:
https://www.kaggle.com/andrewmvd/heart-failure-clinical-data

Algoritma yang digunakan dalam training model : Logistic Regression 

Dalam melakukan prediksi dibutuhkan 5 indikator yaitu:
- Age - Umur.
- Ejection Fraction - Berapa persen jumlah kadar darah yang keluar dari jantung per satu kontraksi.
- Serum Creatinine - Kadar zat kreatine pada darah (mg/dL).
- Serum Sodium - Kadar zat garam/sodium pada darah (mEq/L).
- Time - Berapa lama pasien sudah terdiagnosa mempunyai penyakit jantung.

Hasil prediksi akan menghasilkan 2 hasil: 
- Berpotensi Gagal Jantung - Heart Attack 
- Tidak berpotensi Gagal Jantung - Heart Attack 

Menggunakan Library :
- Matplotlib - Untuk visualisasi data untuk analisis di jupyter notebook
- Seaborn - Untuk visualisasi data untuk analisis di jupyter notebook
- Pandas - Untuk pengolahan data menjadi dataframe
- Numpy - Berhubungdan dalam mengolah array pada data
- Scikit Learn - Untuk membantu dalam memberikan Classification Report, Model Algoritma, Conffusion Matrix
- Joblib - Untuk mengimport dan meneksport model
- Flask - Untuk menampilkan dashboard visualisasi data dan untuk melakukan Prediksi

Step penggunaan:
1. Pertama kita perlu menginstall library dan framework yang diperlukan dengan cara:
    1. Membuat virtual environtments
    - python3 -m pip install --user pipenv
    - python3 -m venv heartattack
    - source heartattack/bin/activate
    - pip install -r requirements.txt

2. Setelah semua library dan framework yang diperlukan sudah terinstall
3. Anda bisa melihat isi dari jupyter notebook dengan cara membuka terminal atau cmd
    1. Membuka Jupyter Notebook
        - jupyter notebook --> Mengetik ini di command line
        - Lalu membuka Ip: host jupyter notebook di browser anda seperti localhost:8888
        - lalu cari heart.ipynb
        - Jupyter notebook telah terbuka disini anda bisa melihat bagaimana dilakukannya visualisasi data,
        pembersihan data, pembuatan model, dan evaluasi.
    2. Membuka Dashboard Flask
        - Dengan cara megetik "flask run" di command line.
	    - Link : http://127.0.0.1:5000
        - Disini anda bisa melihat visualisasi data, maupun melakukan prediksi data.
