# IMPORT LIBRARY
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# FUNCTIONS
def jarak(x_1, x_2, metode="eucledian"):
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
    if metode=="eucledian":
        hasil = np.sqrt(np.sum((x_1 - x_2)**2))
    elif metode=="manhattan":
        hasil = np.sqrt(np.sum(np.abs(x_1 - x_2)))

    return hasil

def knnClassification(X_train, y_train, X_test, k):
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
    m = X_train.shape[1]    # Banyak Fitur data training
    p = X_test.shape[0]     # Banyak data testing

    # Mencari tetangga k terdekat
    # untuk setiap data test
    list_prediction = np.zeros(p)
    for i in range(p):

        # kita cari tetangga terdekatnya
        list_jarak = np.zeros(n)
        for j in range(n):
            # pencarian jarak menggunakan eucledian
            jarak_ = jarak(X_test[i, :], X_train[j, :], metode="eucledian")   
            list_jarak[j] = jarak_

        # Cari k tetangga terdekat
        index_tetangga = list_jarak.argsort()[:k]

        # Cek tetangga lebih banyak kelas apa?
        output_tetangga = [y_train[ii] for ii in index_tetangga]
        list_prediction[i] = max(set(output_tetangga), key=output_tetangga.count)

    return list_prediction

def execute():
    # Load data
    df = pd.read_csv("dummy_data.csv")

    # Pisahkan data training
    X_train = df.values[:, :2]
    y_train = df.values[:, -1]

    # Buat data testing
    X_test = np.array([[2.78, 1.47],
                       [2.55, 2.36]])
    
    # Plot
    """
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8,8), dpi=100)

    for i in range(X_train.shape[0]):
        if y_train[i] == 0:
            ax.scatter(X_train[i, 0], X_train[i, 1], c="red", marker="^")
        else:
            ax.scatter(X_train[i, 0], X_train[i, 1], c="blue", marker="o")

    ax.scatter([], [], c="red", marker="^", label="Class-0")
    ax.scatter([], [], c="blue", marker="o", label="Class-1")
    ax.scatter(X_test[:, 0], X_test[:, 1], c="green", marker="x", label="uncategorized")

    ax.set_xlabel("fitur 1")
    ax.set_ylabel("fitur 2")
    ax.grid(linestyle="--")
    ax.legend()
    plt.show()
    """

    # Predict
    y_test = knnClassification(X_train, y_train, X_test, k=5)
    
    print("Hasil prediksi:")
    print(y_test)


# EXECUTE
if __name__ == "__main__":
    execute()
