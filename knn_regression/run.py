# IMPORT LIBRARY
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# FUNCTIONS
def jarak(x_1, x_2, metode="euclidean"):
    """
    Fungsi untuk menghitung jarak antara 2 titik observasi x_1 dan x_2

    Input:
        x_1     (n-vektor)  : vektor observasi 1
        x_2     (n-vektor)  : vektor observasi 2
        metode  (list)      : metode perhitungan jarak
                              eucledian (default), manhattan
                
    Output:
        hasil   (float)     : jarak antara 2 titik observasi
    """
    if metode=="euclidean":
        hasil = np.sqrt(np.sum((x_1 - x_2)**2))
    elif metode=="manhattan":
        hasil = np.sqrt(np.sum(np.abs(x_1 - x_2)))

    return hasil

def knnRegression(X_train, y_train, X_test, k):
    """
    Fungsi untuk melakukan klasifikasi menggunakan k-NN
    
    Input:
        X_train         (list)  : Input data training - (n, m)
        y_train         (list)  : Input target training - (n, 1)
        X_test          (list)  : Input data test/predict - (p, m)
                                    dengan
                                        n = jumlah data training
                                        m = jumlah fitur
                                        p = jumlah data test/predict

        k               (int)   : jumlah tetangga terdekat

    Output:
        list_prediction (list)  : Hasil prediksi - (p, 1)
    """
    # Ekstrak info
    n = X_train.shape[0]    # Banyak data training
    #m = X_train.shape[1]    # Banyak Fitur data training
    p = X_test.shape[0]     # Banyak data testing

    # Mencari tetangga k terdekat
    # untuk setiap data test
    list_prediction = np.zeros(p)
    for i in range(p):

        # kita cari tetangga terdekatnya
        list_jarak = np.zeros(n)
        for j in range(n):
            # pencarian jarak menggunakan eucledian
            jarak_ = jarak(X_test[i], X_train[j], metode="euclidean")   
            list_jarak[j] = jarak_

        # Cari k tetangga terdekat
        index_tetangga = list_jarak.argsort()[:k]

        # Rata-ratakan seluruh tetangga terdekat untuk mendapatkan nilai
        output_tetangga = [y_train[ii] for ii in index_tetangga]
        list_prediction[i] = np.mean(output_tetangga)

    return list_prediction

def execute():
    # Load data
    df = pd.read_csv("bmd.csv")

    # Pisahkan data training
    X_train = df["age"]
    y_train = df["bmd"]

    # Buat data testing
    X_test = X_train.copy()

    # Plot
    """
    fig, ax = plt.subplots(nrows=1, ncols=1, constrained_layout=True, dpi=100)

    ax.scatter(X_train, y_train, c="none", edgecolors='grey', label="observed data")

    ax.legend()
    ax.grid(linestyle="--")
    ax.set_xlabel("Age")
    ax.set_ylabel("BMD")

    plt.show()
    """

    # Prediksi
    y_test = knnRegression(X_train, y_train, X_test, k=3)
    
    # Cari RMSE
    rmse = np.linalg.norm(y_train - y_test)
    print(f"RMSE : {rmse:.4f}")

    # Plot hasil
    """
    fig, ax = plt.subplots(nrows=1, ncols=1, constrained_layout=True, dpi=100)

    ax.scatter(X_train, y_train, c="none", edgecolors='grey', label="observed data")

    idx_sort = np.argsort(X_test)
    X_test_sorted = X_test[idx_sort]
    y_test_sorted = y_test[idx_sort]
    ax.plot(X_test_sorted, y_test_sorted, c='b', label="prediksi")

    ax.legend()
    ax.grid(linestyle="--")
    ax.set_xlabel("Age")
    ax.set_ylabel("BMD")

    plt.show()
    """


# EXECUTE
if __name__ == "__main__":
    execute()

