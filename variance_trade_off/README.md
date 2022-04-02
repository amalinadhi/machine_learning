Notebook ini berisi contoh bagaimana model dengan kompleksitas tinggi (model yang fleksibel) menyebabkan terjadi-nya variance yang besar apabila data training sampelnya diubah.

![image](https://user-images.githubusercontent.com/34134391/161360271-952b0d26-19df-4a56-bdd1-4eaabc840cc4.png)

Terlihat bahwa
- terjadi perubahan drastis pada nilai $\hat{f}$ (model) antara sampel 1 & 2 pada model complex (ordo tinggi - ordo 12), dibanding model dengan ordo kecil (less complex model)
- perubahan drastis ini mengakibatkan variance antar model meningkat
- Hal ini yang ingin dihindari agar model tidak over fitting
