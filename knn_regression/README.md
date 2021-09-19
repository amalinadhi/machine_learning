# **Apa ini?**

- Intuisi, apabila kamu berada di sekitar kumpulan suatu kelompok, kamu dapat dikenali dengan mengenali karakteristik kelompok tersebut.
- *k-nearest neighbor* (K-NN) bekerja dengan cara yang sama dengan hal di atas.
- Untuk memprediksi nilai suatu observasi data, Anda dapat me-rata-rata-kan nilai dari tetangga terdekatnya.

<p align="center">
    <img src="https://miro.medium.com/max/1400/1*9mN0mO61lmoj0-95i-vV7A.png"/>
    <a href="https://towardsdatascience.com/how-to-build-knn-from-scratch-in-python-5e22b8920bd2">
    2-d Regression using KNN when k=3
    </a>
</p>

- Dari gambar di atas, nilai ("+") didapat dengan merata-ratakan nilai dari 3 observasi data dalam lingkaran (tetangga terdekat)

# **Bagaimana mencari tetangga terdekat?**
- Anda dapat menggunakan fungsi jarak untuk mencarinya.
- Ada banyak fungsi jarak seperti:
    - Euclidean
    - Manhattan
    - Minkowski

# **Cara Jalankan?**
- Install library yang dibutuhkan
   - Matplotlib
   - Numpy
   - Pandas
- Kemudian jalankan `python -B run.py`


# **Cara mengatur fungsi jarak**
- Pada code ini, disediakan fungsi jarak yang dapat Anda ubah-ubah.
- Untuk mengubah perhitungan jarak, Anda dapat masuk ke dalam fungsi `knnRegression`, kemudian cari line `60` 


```python 
jarak_ = jarak(X_test[i], X_train[j], metode="euclidean")
```
- Anda dapat mengubah nilai argumen `metode` menjadi `euclidean` atau `manhattan` (saat ini hanya tersedia 2 metode)
- Apabila **ingin menambahkan fungsi jarak**, Anda dapat menambahkannya pada fungsi `jarak` (lihat line `8` - `26`)

# **Cara mengatur jumlah tetangga**
- Anda dapat mengatur k (jumlah tetangga) pada line `98` --> `y_test = knnClassification(X_train, y_train, X_test, k=3)`



# **Hasil**
- Kita akan bermain dengan data BMD (Bone Mass Density)
![](https://github.com/amalinadhi/machine_learning/blob/main/knn_regression/hasil/gambar_data_bmd.png)

- Selanjutnya, kita ingin memprediksi `bmd` berdasarkan fitur `age`.
- Kita memiliki gambaran observasi datanya sebagai berikut.
![](https://github.com/amalinadhi/machine_learning/blob/main/knn_regression/hasil/initial_gambar.png)

- Data terlihat sedikit aneh, karena `age` nya bersifat kontinu (?), maksudnya ada `age` yang bernilai rasional, seperti: 45.2 tahun.
- Tapi gak masalah, kita cuman nyoba saja.
- Kita coba prediksi data test mengikuti data training yang tersedia. Anda dapat mengatur data test Anda pada line `98`.
- Setelah program dijalankan, didapatkan hasil sebagai berikut.
![](https://github.com/amalinadhi/machine_learning/blob/main/knn_regression/hasil/final_gambar_k=3.png)
- Cukup overfit nampaknya, karena kita pakai `k=3`. Selanjutnya kita coba `k=15`, berikut hasilnya.
![](https://github.com/amalinadhi/machine_learning/blob/main/knn_regression/hasil/final_gambar_k=15.png)
- Terlihat lebih "generalized"
- Disini terlihat adanya beda "skala" antara `age` dengan `bmd`.
- Apa perlu di skala-kan? :smile:
