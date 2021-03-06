# PastiSampai-by-Group-3-Mechatronics-AI-UPI-EDU
Repository ini merupakan dokumentasi projek UAS mata kuliah database &amp; DBMS.

I. Anggota Tim :

- Geralda Livia Nugraha (2100179)

- Vinka Reviansa (2101918)

- Faiza Latifah (2103319)

II. PastiSampai

III. Latar Belakang

  Untuk memudahkan pengaksesan data dalam sebuah perusahan logistik, diperlukan manajemen basis data yang baik. Database management system digunakan untuk mengakses satu data dengan data yang lain. Selain untuk melihat data, database management system juga akan memudahkan apabila pengguna ingin mencari, menambahkan, menghapus, hingga membuat data baru. Hal ini dilakukan untuk meminimalisir ketidaksesuaian data antara database dan apa yang diterima.

IV. Solusi

  Berdasarkan latar belakang yang ada, kami membuat aplikasi CRUD (Create, Read, Update, Delete) berbasis console dimana CRUD ini akan memudahkan pengguna untuk dapat mengetahui status pengiriman hanya dengan mengakses id pengiriman. Selain itu, pengguna dapat mencari, menambahkan dan menghapus data melalui aplikasi CRUD ini. 

V. Flowchart

Berikut merupakan link akses google drive flowchart :

https://drive.google.com/drive/u/0/folders/19gAp2Scc4RgXs-3SUBAY7TzYKTUdW1s6

VI. Panduan Penggunaan Aplikasi

- Pada tampilan awal, User akan diberikan 5 pilihan. Dimana pada setiap pilihan user akan diarahkan untuk melengkapi data sesuai dengan perintah atau pertanyaan yang diberikan.

- Saat user memilih pilihan <1> yaitu menu input, user harus melengkapi beberapa data yaitu tanggal pengiriman, jenis pengiriman, jenis barang yang dikirim, asal pengiriman, tujuan pengiriman, dan status pengiriman. Pada tanggal pengiriman format yang diinputkan  harus (YYYY-MM-DD), jika tidak sistem akan terus meminta user untuk menginputkan data sesuai format. Demikian juga dengan jenis pengiriman, user hanya diberikan tiga pilihan (darat, laut, udara) untuk dapat dipilih. Jika user memasukan data diluar dari tiga pilihan tersebut, sistem akan terus meminta user untuk memasukan data sesuai pilihan yang diberikan. Pada asal pengiriman dan tujuan pengiriman user melengkapi kedua data dan bisa disesuaikan dengan keadaan karna tidak memerlukan kodisi khusus atau pilihan. Pada status pilihan user diberikan dua pilihan (Sudah/Tidak) dimana user hanya dapat memilih salah satu kondisi di antara kedua pilihan tersebut. Jika user menginputkan data diluar pilihan tersebut, sistem akan terus meminta user untuk menginputkan data sesuai dengan pilihan yang diberikan.

- Saat user memilih pilihan <2> yaitu Read Data Barang, sistem akan menampilkan data yang tersimpan pada sistem.

- Saat user memilih pilihan <3> yaitu Update Data Barang, sistem akan menampilkan data yang sudah tersimpan sebelumnya. Sistem menu ketiga sama dengan menu nomor 1, apabila user memasukkan input yang tidak sesuai, maka program akan terus meminta input yang sesuai, apabila kondisi telah terpenuhi, maka sistem akan menampilkan pesan ???Data Barang Baru Berhasil Dibuat???

- Saat user memilih pilihan <4> yaitu Delete Data Barang, sistem akan menampilkan data yang sudah tersimpan sebelumnya. User diminta untuk mengisi ID Pengiriman, kemudian user memilih data yang akan dihapus dari tabel. Ketika user telah menginputkan data yang dihapus dengan sesuai, system akan menampilkan ???Data Barang Berhasil Dihapus!???. Data akan dihapus berdasarkan ID pengiriman yang dimasukkan.

- Saat user memilih pilihan <5> yaitu Cari Data Barang, user menginputkan keyword seperti angka atau kata yang kemudian sistem akan mencari data sesuai keyword yang sesuai dengan input user.

- Saat user memilih pilihan <0> yaitu Keluar, sistem akan memberhentikan aplikasi console.

VII. Demo

https://drive.google.com/drive/u/0/folders/197nsN_bXnJdPaCK3KVk3qq23oGMPiJek

VIII. Referensi

- https://pypi.org/project/prettytable/
- https://wwww.javatpoint.com/prettytable-in-python
- https://www.petanikode.com/tutorial-php-mysql/
