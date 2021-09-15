# Apa ini?
- Kita coba masukkan *error* (<img src="https://render.githubusercontent.com/render/math?math=\epsilon">) ke dalam model linear yang menghubungkan antara <img src="https://render.githubusercontent.com/render/math?math=x"> dan <img src="https://render.githubusercontent.com/render/math?math=y">.
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Cdpi%7B120%7D%20y%20%3D%20%5Ctheta_%7B1%7D%20x%20&plus;%20%5Ctheta_%7B0%7D%20&plus;%20%5Cepsilon">
</p>

- Ada beberapa asumsi yang kita pakai selanjutnya:
   - Distribusi dari <img src="https://render.githubusercontent.com/render/math?math=x"> adalah *arbitrary*
   - <img src="https://latex.codecogs.com/svg.latex?%5Cinline%20%5Cdpi%7B120%7D%20%5Cepsilon%20%5Csim%20N%280%2C%20%5Csigma%5E%7B2%7D%29"> dan independen terhadap <img src="https://render.githubusercontent.com/render/math?math=x">.
   - <img src="https://render.githubusercontent.com/render/math?math=\epsilon"> independen terhadap observasi

- Maka, dalam mencari model, ada 3 parameter yang harus dioptimasi:
   - intercept, <img src="https://latex.codecogs.com/svg.latex?%5Cinline%20%5Cdpi%7B120%7D%20%5Ctheta_%7B0%7D">
   - slope, <img src="https://latex.codecogs.com/svg.latex?%5Cinline%20%5Cdpi%7B120%7D%20%5Ctheta_%7B1%7D">
   - varians dari distribusi error, <img src="https://latex.codecogs.com/svg.latex?%5Cinline%20%5Cdpi%7B120%7D%20%5Csigma%5E%7B2%7D">

# Likelihood function?
- Selanjutnya, kita dapat menuliskan hubungan antara <img src="https://render.githubusercontent.com/render/math?math=x"> dan <img src="https://render.githubusercontent.com/render/math?math=y"> yang baru mengikuti distribusi normal sebagai berikut
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Cinline%20%5Cdpi%7B120%7D%20y%20%5Csim%20N%28%5Ctheta_%7B1%7Dx%20&plus;%20%5Ctheta_%7B0%7D%2C%20%5Csigma%5E%7B2%7D%29">
</p>

- Kemudian, setiap titik memiliki PDF, <img src="https://latex.codecogs.com/svg.latex?%5Cinline%20%5Cdpi%7B120%7D%20P%28%5Ctext%7Bdata%7D%20%7C%20%5Ctext%7Bparameter%7D%29">, mengikuti distribusi normal sebagai berikut
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Cinline%20%5Cdpi%7B120%7D%20P%28y_%7Bi%7D%20%7C%20x_%7Bi%7D%3B%20%5Ctheta_%7B0%7D%2C%20%5Ctheta_%7B1%7D%2C%20%5Csigma%5E%7B2%7D%29%20%3D%20%5Cfrac%7B1%7D%7B%5Csqrt%7B2%5Cpi%5Csigma%5E%7B2%7D%7D%7D%20%5Cexp%20%5Cleft%20%28%20-%20%5Cfrac%7B1%7D%7B2%5Csigma%5E%7B2%7D%7D%20%5Cleft%28%20y_%7Bi%7D%20-%20%28%5Ctheta_%7B1%7Dx_%7Bi%7D%20&plus;%20%5Ctheta_%7B0%7D%29%20%5Cright%29%5E%7B2%7D%20%5Cright%20%29">
</p>

- Mengingat tiap titik adalah *independent and indentical distributed* (iid), kita dapat menentukan *likelihood*, dalam bentuk <img src="https://latex.codecogs.com/svg.latex?L%28%5Ctext%7Bparameter%7D%20%7C%20%5Ctext%7Bdata%7D%29"> sebagai *joint distribution*:
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Cinline%20%5Cdpi%7B120%7D%20L%28%5Ctext%7Bparameter%7D%20%7C%20%5Ctext%7Bdata%7D%29%20%3D%20%5Cprod_%7Bi%7D%20P%28%5Ctext%7Bdata%7D_%7Bi%7D%20%7C%20%5Ctext%7Bparameters%7D%29"> 
</p>

- Selanjutnya kita mencari parameter yang dapat memaksimalkan likelihood
- Untuk mempermudah, kita dapat mencari log-likelihood.
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Cbegin%7Balign*%7D%20%5Clog%20%5Cleft%5B%20L%28%5Ctheta_%7B0%7D%2C%20%5Ctheta_%7B1%7D%2C%20%5Csigma%5E%7B2%7D%29%20%5Cright%5D%20%26%3D%20%5Clog%20%5Cleft%5B%20%5Cprod_%7Bi%3D1%7D%5E%7Bn%7D%20P%28y_%7Bi%7D%7Cx_%7Bi%7D%3B%5Ctheta_%7B0%7D%2C%20%5Ctheta_%7B1%7D%2C%20%5Csigma%5E%7B2%7D%29%20%5Cright%5D%5C%5C%20%26%3D%20%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20%5Ctext%7Blog%7D%20%5Cleft%5B%20P%28y_%7Bi%7D%7Cx_%7Bi%7D%3B%5Ctheta_%7B0%7D%2C%20%5Ctheta_%7B1%7D%2C%20%5Csigma%5E%7B2%7D%29%20%5Cright%5D%5C%5C%20%26%3D%20-%5Cfrac%7Bn%7D%7B2%7D%5Clog%7B2%5Cpi%7D%20-%20n%5Clog%7B%5Csigma%7D%20-%20%5Cfrac%7B1%7D%7B2%5Csigma%5E%7B2%7D%7D%20%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20%5Cleft%28%20y_%7Bi%7D%20-%20%28%5Ctheta_%7B1%7Dx_%7Bi%7D%20&plus;%20%5Ctheta_%7B0%7D%29%20%5Cright%29%5E%7B2%7D%20%5Cend%7Balign*%7D">
</p>

- Meminimalkan fungsi di atas sama seperti meminimalkan suku ke-3 dari persamaan.
- Dengan kata lain, kita menyelesaikan normal equations seperti pada least squares problems.
- Maka didapat:
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ctheta%20%3D%20%5Cleft%28%20X%5E%7BT%7D%20X%20%5Cright%29%5E%7B-1%7D%20X%5E%7BT%7D%20y">
</p>

- dengan
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?X%20%3D%20%5Cbegin%7Bbmatrix%7D%20%5Cvdots%20%26%20%5Cvdots%20%5C%5C%201%20%26%20x%20%5C%5C%20%5Cvdots%20%26%20%5Cvdots%20%5Cend%7Bbmatrix%7D">
</p>

# Cara Jalankan?
- Install library yang dibutuhkan
   - Matplotlib
   - Numpy
- Kemudian jalankan `python -B run.py`

# Hasil
<p align="center">
  <img src="https://github.com/amalinadhi/machine_learning/blob/main/mle_linear_regression/results.png"/>
  <br>
  Garis biru mengindikasikan MLE Linear Regression. Kok gak fit (?) Haha :smile:
</p>
