# Implementasi Perangkat Lunak AsrayMedika+
> Implementasi Perangkat Lunak berbasis GUI AsrayMedika+ dengan Python dan PyQt5 

## Table of contents
* [General Info](#general-info)
* [Features](#features)
* [Screenshot](#screenshot)
* [Modul](#modul)
* [Database](#database)
* [Technologies](#technologies)
* [System requirements](#system-requirements)
* [How to use](#how-to-use)
* [Status](#status)
* [Authors](#authors)

## General Info
Perangkat lunak AsrayMedika+ dibuat untuk memenuhi Milestone 8 Tugas Besar IF2250 RPL Semester Genap tahun 2021. AsrayMedika+ merupakan bentuk digitalisasi klinik/apotek Asray Medika. AsrayMedika+ mengakomodir user memilih dan menambahkan obat ke keranjang pembelian, menambahkan obat ke keranjang berdasarkan file eksternal, menampilkan dokter dan jadwal praktik dokter, dan mengokomodir chatbot.

## Features
- Menampilkan obat dan identitas obat (nama, stok, harga, deskripsi, gambar)
- Memilih atau melalui input file untuk menambahkan obat ke keranjang belanja
- Menampilkan isi dan total harga obat di keranjang belanja
- Menampilkan dokter dan jadwal praktik dokter yang tersedia
- Menyediakan fitur chatbot 

## Screenshot
![Halaman Utama](/doc/Modul_HalamanUtama.png?raw=true "Halaman Utama")
![Halaman Dokter](/doc/Modul_Dokter.png?raw=true "Halaman Dokter")
![Halaman Obat](/doc/Modul_Obat.png?raw=true "Halaman Obat")
![Halaman Chat](/doc/Modul_Chat.png?raw=true "Halaman Chat")

## Modul
1. Modul Obat (Rezda Abdullah Fachrezzi - 13519194/K-04)
2. Modul Dokter (Rayhan Asadel - 13519196/K-04) 
3. Modul Chatbot (Muhammad Rayhan Ravianda - 13519202/K-04)
4. Modul Input Resep Dokter (Alif Bhadrika Parikesit - 13519186/K-04)

## Database
1. obat.csv (id_obat,nama_obat,stok,harga,desc,url_image)
2. Jadwal1.csv (id_jadwal,jadwal,ketersediaan)
3. Jadwal2.csv (id_jadwal,jadwal,ketersediaan)
4. Jadwal3.csv (id_jadwal,jadwal,ketersediaan)

## Technologies
- python3
- requests module
- PyQt5 module

## System requirements
1. Make sure you have python installed in your device. Download python **[here](https://www.python.org/downloads/)**.
2. Install pip. Check **[this](https://pip.pypa.io/en/stable/installing/)**.
3. Install requests
```
    $ pip install requests
```
3. Install PyQt5
```
    $ pip install pyqt5
    $ pip install pyqt5-tools
```

## How to use
1. Jalankan app.py di shell atau dengan klik app.py
``` $ py app.py ``` 
2. Pilih fitur yang mau Anda coba
3. Untuk fitur beli obat, Anda bisa menambahkan obat dan menghapus obat dari keranjang
4. Anda juga dapat mengupload resep dokter dengan format file .txt
```
Text file format:

    amoxicillin : 3
    paracetamol : 4
    
``` 
5. Untuk fitur cari dokter, Anda dapat melihat dokter yang tersedia dan jadwal praktiknya
6. Untuk fitur chatbot, Anda dapat mengikuti instruksi lebih lanjut yang diberikann chatbot


## Status
Project is finished.

## Inspiration
Spesifikasi Tugas Besar IF2250 RPL Semester Genap tahun 2021.

## Authors
* Alif Bhadrika Parikesit - 13519186/K-04
* Rezda Abdullah Fachrezzi - 13519194/K-04
* Rayhan Asadel - 13519196/K-04
* Muhammad Rayhan Ravianda - 13519202/K-04
