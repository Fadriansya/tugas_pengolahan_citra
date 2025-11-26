# Tugas Pengolahan Citra

## 1. Deskripsi Singkat

Aplikasi ini merupakan **toolkit pemrosesan citra** berbasis Python yang dilengkapi antarmuka GUI menggunakan **Tkinter**. Program ini mampu melakukan:

- Preprocessing gambar (Gaussian, Median, Bilateral Filter)
- Segmentasi berbasis **HSV** dan **K-Means Clustering**
- Perhitungan metrik evaluasi segmentasi (IoU, Dice, Precision, Recall)
- Penyimpanan otomatis hasil ke dalam folder `hasil/`

Toolkit ini cocok digunakan untuk tugas kuliah, eksperimen segmentasi, maupun demonstrasi konsep pengolahan citra.

---

## 2. Fitur Utama

### ✔ Preprocessing

- Gaussian blur
- Median filter
- Bilateral filter

### ✔ Segmentasi

- **HSV Thresholding**
- **K-Means Clustering (K=3)**

### ✔ Evaluasi dengan Ground Truth (GT)

Metrik yang dihitung:

- IoU (Intersection over Union)
- Dice Coefficient
- Precision
- Recall
  Hasil ditampilkan dalam bentuk **grafik bar** dan disimpan otomatis.

### ✔ GUI (Tkinter)

- Browse file input
- Browse file ground truth
- Tombol proses gambar
- Tombol hitung metrik
- Tampilan status

---

## 3. Struktur Folder

```
project_folder/
│-- main.py
│-- hasil/
│     ├── original.png
│     ├── gaussian.png
│     ├── median.png
│     ├── bilateral.png
│     ├── mask_hsv.png
│     ├── segment_hsv.png
│     ├── mask_kmeans.png
│     ├── segment_kmeans.png
│     ├── metric_results.png
```

---

## 4. Cara Menjalankan Program

### 1. Install dependency

Pastikan Python sudah terinstall, lalu jalankan:

```
pip install opencv-python numpy matplotlib
```

### 2. Jalankan aplikasi

```
python main.py
```

GUI akan muncul otomatis.

---

## 5. Penjelasan Alur Program

### **A. Pemrosesan Gambar**

1. Membaca gambar input
2. Melakukan preprocessing (Gaussian, Median, Bilateral)
3. Konversi ke ruang warna HSV → threshold → segmentasi
4. Melakukan K-Means clustering → memilih klaster target → mask
5. Menyimpan semua hasil ke folder `hasil/`

### **B. Evaluasi Metrik**

1. Membaca mask hasil segmentasi dan GT
2. Binarisasi GT
3. Menghitung:

   - TP, FP, FN
   - IoU = TP / Union
   - Dice = 2TP / (Pred + GT)
   - Precision = TP / (TP + FP)
   - Recall = TP / (TP + FN)

4. Menampilkan grafik bar dan menyimpannya ke `hasil/`

---

## 6. Kode Utama

Kode lengkap program berada pada file `main.py` dan berisi:

- Fungsi preprocessing
- Fungsi segmentasi HSV dan K-Means
- Fungsi perhitungan metrik
- Fungsi plotting metrik
- GUI Tkinter

---

## 7. Catatan Penting

- Folder `hasil/` dibuat otomatis saat program dijalankan.
- Ground Truth harus berupa gambar biner (0 dan 255). Program sudah menyediakan threshold otomatis.
- Jika ingin mengubah parameter (misalnya K pada K-Means), bisa disesuaikan pada bagian kode terkait.

---

## 8. Lisensi

Proyek ini bebas digunakan untuk kebutuhan akademik, tugas kuliah, atau pengembangan lebih lanjut.

---

Jika ingin menambahkan screenshot GUI atau ingin dibuatkan versi dokumentasi PDF, cukup beri tahu saya.
