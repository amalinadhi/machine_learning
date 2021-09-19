# **Apa ini?**

- Salah satu metode klasifikasi yang cukup sederhana.
- Intuisinya adalah mencari "votes" terbanyak dalam <img src="https://render.githubusercontent.com/render/math?math=k"> observasi.
- Kategori/*class* terbanyak dalam <img src="https://render.githubusercontent.com/render/math?math=k"> observasi akan menjadi kategori data yang diinginkan.
- Penentuan <img src="https://render.githubusercontent.com/render/math?math=k"> observasi didapat dari perhitungan jarak terdekat dengan data yang diinginkan.
- **Jarak** sendiri dapat menggunakan *euclidean*, *manhattan* atau lainnya bergantung kebutuhan.

<p align="center">
    <img src="https://miro.medium.com/max/1400/1*9mN0mO61lmoj0-95i-vV7A.png"/>
    <a href="https://towardsdatascience.com/how-to-build-knn-from-scratch-in-python-5e22b8920bd2">
    2-d Classification using KNN when k=3
    </a>
</p>

# **Cara Jalankan?**
- Install library yang dibutuhkan
   - Matplotlib
   - Numpy
   - Pandas
- Kemudian jalankan `python -B run.py`


# **Cara mengatur fungsi jarak**
- Pada code ini, disediakan fungsi jarak yang dapat Anda ubah-ubah.
- Untuk mengubah perhitungan jarak, Anda dapat masuk ke dalam fungsi `knnClassification`, kemudian cari line `60` 


```python 
jarak_ = jarak(X_test[i, :], X_train[j, :], metode="euclidean")
```
- Anda dapat mengubah nilai argumen `metode` menjadi `euclidean` atau `manhattan` (saat ini hanya tersedia 2 metode)
- Apabila **ingin menambahkan fungsi jarak**, Anda dapat menambahkannya pada fungsi `jarak` (lihat line `8` - `26`)

# **Cara mengatur jumlah tetangga**
- Anda dapat mengatur k (jumlah tetangga) pada line `106` --> `y_test = knnClassification(X_train, y_train, X_test, k=5)`



# **Hasil**
![](https://github.com/amalinadhi/machine_learning/blob/main/knn_classification/test.png)
- Kita coba klasifikasikan data test (uncategorized) dari dataset dummy.
- Anda dapat mengatur data test Anda pada line `81-82`.
- Setelah program dijalankan, didapat bahwa kedua data test memiliki kelas 0, sesuai dengan ilustrasi yang diberikan.
- Kalo nilai k kita tingkatkan apa yang terjadi ya (?) Haha :smile:

