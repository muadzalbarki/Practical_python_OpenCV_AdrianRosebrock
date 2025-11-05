# Practical Python OpenCV — Adrian Rosebrock

Repo ini berisi kumpulan skrip Python berdasarkan buku *Practical Python & OpenCV* oleh Adrian Rosebrock.
Skrip‑skrip ini digunakan sebagai latihan untuk memahami dasar‑dasar Computer Vision menggunakan OpenCV.

---

## 🚀 Status & Informasi

![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-brightgreen)


---

## 📂 Struktur Folder

```
/ (root)
│
├ image/                   # Contoh gambar
├ arithmetic.py            # Operasi aritmetika gambar
├ bitwise.py               # Operasi bitwise
├ blurring.py              # Blurring / smoothing
├ color_histogram.py       # Histogram warna
├ colorspaces.py           # Konversi ruang warna
├ crop.py                  # Cropping gambar
├ drawing.py               # Menggambar bentuk/geometri
├ equalize.py              # Equalisasi histogram
├ flipping.py              # Flip gambar (horizontal/vertikal)
├ grayscalehisto.py        # Histogram grayscale
├ histomask.py             # Masking & histogram
├ masking.py               # Masking gambar
├ resized.py               # Resize gambar
├ rotated.py               # Rotasi gambar
├ setting.py               # Translasi gambar
├ splittingandmerging.py   # Pembagian dan penggabungan channel
└ ...                      # Skrip lain sesuai latihan
```

---

## 🛠 Instalasi

Pastikan Python sudah terinstall.

Install dependensi:

```bash
pip install opencv-python imutils
```

---

## ▶️ Cara Menjalankan

Contoh menjalankan skrip translasi gambar:

```bash
python3 setting.py -i image/image.jpg
```

Gantilah nama file dan path gambar sesuai kebutuhan.

---

## 🔍 Penjelasan Singkat

| Operasi | Fungsi |
|--------|--------|
| Translasi | Menggeser posisi gambar |
| Rotasi | Memutar gambar berdasarkan sudut tertentu |
| Resize | Mengubah ukuran gambar tanpa merusak aspek rasio |
| Masking | Menonjolkan bagian tertentu dari gambar |
| Histogram | Menampilkan distribusi intensitas / warna |

---

## 📘 Referensi

- Buku: *Practical Python & OpenCV* — Adrian Rosebrock
- Dokumentasi OpenCV: https://opencv.org/
- Library bantuan: https://github.com/jrosebr1/imutils

---

## 🤝 Kontribusi

Silahkan fork, edit, dan lakukan pull request jika ingin berkontribusi.

---

