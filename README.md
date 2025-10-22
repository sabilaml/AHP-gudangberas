# AHP-gudangberas
Kode program AHP untuk menentukan lokasi gudang beras di Jawa Timur
Proyek ini berisi kode Python sederhana untuk menentukan lokasi terbaik gudang beras di Jawa Timur menggunakan metode AHP (Analytic Hierarchy Process).
Kode ini menghitung bobot kriteria, uji konsistensi (CI & CR), bobot alternatif, dan menampilkan hasil akhir berupa skor total serta peringkat lokasi lengkap dengan visualisasi grafik.

-Tujuan

Menentukan lokasi gudang beras paling optimal berdasarkan 4 kriteria utama:

Akses Transportasi

Ketersediaan Tenaga Kerja

Biaya Lahan

Kedekatan dengan Pusat Produksi

Alternatif lokasi yang dibandingkan:

Lamongan

Jember

Kediri

Madiun

-Teknologi yang Digunakan

Python 313

NumPy → untuk perhitungan matriks

Pandas → untuk membuat dan menampilkan tabel hasil

Matplotlib → untuk membuat grafik bobot dan ranking

- Cara Menjalankan Program
1. Pastikan Python sudah terinstal

Cek di terminal atau cmd:

python --version

2. Install library yang dibutuhkan

Ketik perintah berikut di terminal:

pip install numpy pandas matplotlib

3. Jalankan file Python

Pindah ke direktori tempat file AHP.py disimpan, lalu jalankan:

python AHP.py

4. Hasil yang Akan Ditampilkan

Setelah dijalankan, program akan menampilkan hasil di terminal seperti berikut:

Tabel Bobot Kriteria

Nilai λmax, CI, RI, dan CR (untuk uji konsistensi)

Tabel Skor Akhir dan Ranking Lokasi

Dua grafik otomatis:

Grafik Bobot Kriteria

Grafik Ranking Lokasi Gudang

- Penjelasan Singkat Output
Bagian	Keterangan
Bobot Kriteria	Menunjukkan tingkat kepentingan tiap faktor (Transportasi, Tenaga Kerja, dll).
Uji Konsistensi (CR)	Digunakan untuk mengecek apakah hasil perbandingan logis (CR harus < 0.1 agar konsisten).
Skor Akhir & Ranking	Menunjukkan lokasi terbaik berdasarkan hasil keseluruhan bobot dan prioritas.

- Contoh hasil akhir (berdasarkan data di kode ini):
Lokasi terbaik untuk gudang beras adalah Lamongan, dengan skor tertinggi 0.557892, dan nilai konsistensi CR = 0.043876 (konsisten).
