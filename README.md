Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Saya mengikuti checklist secara berurutan. Sebagai panduan, untuk tiap poin checklist, saya cari langkah-langkah lengkapnya di tutorial. Seiring dengan itu juga, saya menggunakan 
pemahaman saya untuk membantu memilah-milah apa yang harus dilakukan dan apa yang tidak.

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![](https://cdn.discordapp.com/attachments/1030834426126544907/1151216285246562314/S__10641478.jpg)
urls.py menentukan alamat web (URL) apa yang akan memanggil kode di views.py. views.py berisi kode yang menangani permintaan dari URL dan menentukan apa yang harus ditampilkan atau dilakukan. models.py digunakan untuk mendefinisikan struktur data dan database yang digunakan oleh aplikasi. Berkas HTML (misalnya, index.html) adalah tampilan yang digunakan oleh views.py untuk menampilkan informasi kepada pengguna.

Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment berguna untuk menjaga alat-alat proyek secara terpisah agar terhindar dari konflik, membuat proyek menjadi lebih rapi dan mudah diatur, agar kita bisa pilih versi 
alat-alat yang digunakan, dan agar mudah dipindahkan ke komputer lain. Tanpa virtual environment, bisa saja terjadi masalah saat mengembangkan proyek. Jadi, sebaiknya selalu gunakan 
virtual environment saat membuat aplikasi web Django.

Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC (Model-View-Controller): Ini adalah pola desain yang memisahkan aplikasi menjadi tiga komponen utama: Model (data dan logika), View (tampilan), dan Controller (pengaturan input dan respons). Tujuannya adalah memisahkan logika bisnis dari tampilan.
MVT (Model-View-Template): MVT adalah konsep yang digunakan dalam kerangka kerja Django untuk pengembangan web. Ini mirip dengan MVC, tetapi dalam konteks Django, Template (pemisahan 
tampilan) diimplementasikan sebagai bagian dari View.
MVVM (Model-View-ViewModel): MVVM adalah pola desain yang digunakan dalam pengembangan aplikasi berbasis data. Ini memisahkan Model (data dan logika), View (tampilan), dan ViewModel 
(penghubung antara Model dan View). Tujuannya adalah memisahkan logika tampilan dari logika bisnis.
Perbedaannya terutama pada penggunaan dan konsep-konsep yang berbeda dalam pengembangan aplikasi. MVC dan MVT lebih umum digunakan dalam pengembangan web, sedangkan MVVM lebih umum digunakan dalam pengembangan aplikasi berbasis data seperti aplikasi mobile.

# Tugas 3: Implementasi Form dan Data Delivery pada Django

### Apa perbedaan antara form `POST` dan form `GET` dalam Django?

Formulir POST dan GET dalam Django adalah dua metode pengiriman data dari formulir HTML ke server. Dalam POST, data dikirim sebagai bagian dari badan permintaan HTTP dan sering digunakan untuk operasi yang mengubah data di server, lebih aman karena data tidak terlihat dalam URL. Di sisi lain, GET mengirim data sebagai parameter dalam URL dan cocok untuk mengambil data dari server tanpa mengubahnya, tetapi kurang aman karena data terlihat dalam URL.

### Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

XML, JSON, dan HTML adalah format berbeda dalam pengiriman data. XML digunakan untuk pertukaran data terstruktur antar aplikasi, JSON umumnya digunakan dalam pengembangan aplikasi web dan layanan web untuk representasi data dalam format yang mudah dibaca, sedangkan HTML digunakan untuk membuat tampilan halaman web dan menampilkan konten kepada pengguna melalui peramban web. Perbedaan utama adalah dalam notasi dan tujuan penggunaan masing-masing format.

### Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena ia ringan, mudah dibaca, memiliki overhead bandwidth yang rendah, dapat diurai oleh berbagai bahasa pemrograman, mendukung struktur data yang fleksibel, kompatibel dengan JavaScript, dan cocok untuk digunakan dalam API RESTful, memudahkan pengembangan aplikasi web yang efisien dan responsif.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Pertama, saya perhatikan setiap instruksi pada masing-masing poin. Lalu, dengan mengingat apa yang ingin dilakukan, saya melihat panduan di tutorial untuk mencapai tujuan tersebut, saya harus mulai dan berhenti di mana.

### *Postman

#### HTML
![](https://cdn.discordapp.com/attachments/1030834426126544907/1153736509061599262/image.png)

#### XML
![](https://cdn.discordapp.com/attachments/1030834426126544907/1153737203596415046/image.png)

#### JSON
![](https://cdn.discordapp.com/attachments/1030834426126544907/1153737441312776192/image.png)

#### XML _by ID_ 
![](https://cdn.discordapp.com/attachments/1030834426126544907/1153737762273501284/image.png)

#### JSON _by ID_
![](https://cdn.discordapp.com/attachments/1030834426126544907/1153737982780653660/image.png)


# Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django

### Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?

Django `UserCreationForm` adalah kerangka formulir bawaan Python yang memungkinkan pengembang membuat fitur pendaftaran pengguna ke dalam aplikasinya tanpa harus membuat kodenya dari awal. Selain itu, `UserCreationForm` juga sudah mencakup fungsi untuk memvalidasi data yang dimasukkan ke dalam aplikasi, misalnya apakah email sudah pernah digunakan atau belum, serta apakah kata sandi sudah memenuhi syarat atau belum. Di sisi lain, Django `UserCreationForm` memadai untuk fungsi _register_ yang sederhana saja. Untuk mendapatkan fungsi yang lebih kompleks atau dengan kustomisasi tertentu, pengembang harus menulis kode sendiri. Tampilan yang dihasilkan juga sederhana. Kita harus menambahkan CSS dan HTML jika ingin memperoleh tampilan yang diinginkan.

### Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

Auntentikasi adalah proses memverifikasi data yang _user_ masukkan saat login, sedangkan otorisasi adalah proses memastikan bahwa _user_ tersebut mempunyai akses pada aplikasi tersebut. Autentikasi penting untuk melindungi pengguna, mengingat bahwa tiap pengguna memiliki data yang unik dan merupakan privasi masing-masing. Otorisasi penting untuk pemilik aplikasi agar ia tahu siapa yang sedang mengakses sehingga dapat mengatur peran dan izin pengguna, serta untuk memastikan bahwa yang sedang mengakses merupakan pengguna yang sah.

### Apa itu _cookies_ dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

_Cookies_ merupakan tempat menyimpan ID yang menunjuk ke data sesi pengguna agar pengguna dapat mengakses suatu aplikasi dalam satu _login_ saja setiap sesinya. Untuk menggunakan _cookies_, Django, mengimpor `HttpResponseRedirect` dan `reverse`. Lalu, `response.set_cookie('last_login', str(datetime.datetime.now()))` akan membuat _cookie_ **_last login_** dan menambahkannya ke dalam _response_. Selanjutnya, `'last_login': request.COOKIES['last_login']` akan menambahkan informasi _cookie_. Lalu, `delete_cookie()` akan menghapus data pengguna saat _logout_

### Apakah penggunaan _cookies_ aman secara _default_ dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Penggunaan _cookies_ secara _default_ sebenarnya sudah cukup aman. Namun, ada beberapa risiko potensial yang dapat dipertimbangkan untuk privasi aplikasi, antara lain, pencurian _cookie_ XSS, _session_ _fixation_, dan _cookie_ _poisoning_.

### Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).

Saya mengikuti _checklist_ satu per satu dari awal dan untuk setiap intruksi, saya melihat panduan pada tutorial. Misal, pada langkah membuat fungsi _register_, _login_, dan _logout_, saya mengimplementasikan langkah-langkah untuk mengaplikasikan ketiga fungsi tersebut agar dapat digunakan sesuai keinginan, dan begitu seterusnya.


# Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS

### Jelaskan manfaat dari setiap _element_ _selector_ dan kapan waktu yang tepat untuk menggunakannya.

1. **Element Selector (Tag Selector)**:
   - **Manfaat**: Selector ini memungkinkan kita untuk memilih semua elemen dalam dokumen HTML yang memiliki tag yang sama (misalnya, `<p>` atau `<div>`).
   - **Kapan Menggunakannya**: Element selector berguna ketika kita ingin memberikan gaya khusus pada semua elemen dengan tag yang sama. Ini bisa digunakan untuk memberikan gaya dasar pada elemen-elemen ini secara umum.

2. **ID Selector**:
   - **Manfaat**: Selector ID memungkinkan kita untuk memilih elemen dengan atribut `id` tertentu. Elemen dengan ID adalah elemen yang unik dalam halaman.
   - **Kapan Menggunakannya**: ID selector ideal untuk memberikan gaya atau manipulasi JavaScript pada elemen yang unik dan berbeda dalam halaman. Satu elemen hanya boleh memiliki satu ID, sehingga kita dapat merujuk elemen ini secara spesifik.

3. **Class Selector**:
   - **Manfaat**: Class selector memungkinkan kita untuk memilih elemen yang memiliki atribut `class` tertentu. Elemen dengan kelas yang sama dapat diidentifikasi dan diberi gaya dengan mudah.
   - **Kapan Menggunakannya**: Class selector berguna ketika kita ingin memberikan gaya yang sama pada beberapa elemen yang memiliki karakteristik atau peran yang sama dalam halaman.

### Jelaskan HTML5 Tag yang kamu ketahui.

1. **Tag `<body>`**:
   - **Fungsi**: Tag `<body>` digunakan sebagai wadah utama untuk semua konten yang akan ditampilkan di halaman web. Semua elemen, seperti teks, gambar, dan elemen lainnya, biasanya ditempatkan di dalam tag `<body>`.
   - **Contoh Penggunaan**: 
     ```html
     <body>
         <!-- Konten halaman web di sini -->
     </body>
     ```

2. **Tag `<div>`**:
   - **Fungsi**: Tag `<div>` digunakan untuk mengelompokkan atau mengatur elemen-elemen HTML lainnya dalam satu kotak. Ini memungkinkan Anda untuk membuat bagian-bagian dalam halaman web yang dapat diatur dengan gaya atau diubah dengan JavaScript.
   - **Contoh Penggunaan**: 
     ```html
     <div>
         <!-- Elemen-elemen di dalam div -->
     </div>
     ```

3. **Tag `<br>`**:
   - **Fungsi**: Tag `<br>` digunakan untuk membuat baris baru atau memindahkan teks atau elemen ke baris berikutnya. Ini sering digunakan untuk mengatur tata letak atau memberikan jarak vertikal antara elemen-elemen.
   - **Contoh Penggunaan**: 
     ```html
     <p>Satu baris<br>dua baris</p>
     ```

4. **Tag `<tr>`**:
   - **Fungsi**: Tag `<tr>` digunakan dalam tabel HTML untuk mendefinisikan baris tabel.
   - **Contoh Penggunaan**: 
     ```html
     <table>
         <tr>
             <td>Kolom 1</td>
             <td>Kolom 2</td>
         </tr>
     </table>
     ```

5. **Tag `<th>`**:
   - **Fungsi**: Tag `<th>` digunakan dalam tabel HTML untuk mendefinisikan sel kepala (header) tabel. Biasanya digunakan dalam baris pertama atau pertama dari setiap kolom dalam tabel.
   - **Contoh Penggunaan**: 
     ```html
     <table>
         <tr>
             <th>Nama</th>
             <th>Usia</th>
         </tr>
     </table>
     ```

### Jelaskan perbedaan antara _margin_ dan _padding_.

Dalam CSS, **Margin** dan **Padding** adalah dua konsep penting yang digunakan untuk mengatur tata letak dan jarak antara elemen-elemen HTML. Keduanya memiliki perbedaan dalam fungsinya dan lokasi relatif di dalam model kotak CSS yang disebut "Box Model."

#### Margin:

- **Fungsi**: Margin adalah unsur Box Model CSS yang bertanggung jawab untuk mengatur jarak antara elemen saat berada di luar _border_ elemen tersebut. Margin adalah area di sekitar elemen yang bersifat transparan dan tidak dapat diisi dengan warna atau konten. Margin sering digunakan untuk memberikan jarak antara elemen dengan elemen lain di sekitarnya, sehingga mengontrol tata letak keseluruhan halaman.
- **Lokasi**: Margin terletak di luar elemen HTML.
- **Contoh Penggunaan**: Misalnya, ketika kita ingin memberikan jarak antara dua elemen div dalam layout halaman, kita akan mengatur margin di atas, bawah, kiri, atau kanan elemen tersebut.

#### Padding:

- **Fungsi**: Padding adalah unsur Box Model CSS yang mengatur jarak antara _border_ elemen dengan kontennya. Padding adalah area di sekitar konten elemen yang dapat diisi dengan warna atau konten tambahan. Padding berguna untuk mengontrol jarak antara konten elemen dan _border_nya.
- **Lokasi**: Padding terletak di dalam elemen HTML, di antara konten dan _border_.
- **Contoh Penggunaan**: Misalnya, ketika kita ingin memberikan ruang di dalam elemen tombol untuk membuat teks atau ikon terlihat lebih baik, kita akan mengatur padding di dalam elemen tersebut.

### Jelaskan perbedaan antara _framework_ CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

- **Tailwind CSS** membangun tampilan dengan menggabungkan kelas-kelas utilitas yang telah didefinisikan sebelumnya, sedangkan **Bootstrap** menggunakan gaya dan komponen yang telah didefinisikan dan siap digunakan.
- **Tailwind CSS** memiliki file CSS yang lebih kecil dan hanya memuat kelas-kelas utilitas yang diperlukan, sementara **Bootstrap** memiliki file CSS yang lebih besar karena termasuk banyak komponen yang telah didefinisikan.
- **Tailwind CSS** memberikan fleksibilitas dan adaptabilitas yang tinggi terhadap proyek, sementara **Bootstrap** sering menghasilkan tampilan yang lebih konsisten di seluruh proyek berkat komponen yang telah didefinisikan.

**Tailwind CSS** sebaiknya digunakan ketika:

- Kita ingin memiliki kendali yang lebih besar atas tampilan dan gaya elemen-elemen Anda dengan menggabungkan kelas-kelas utilitas.
- Kita paham tentang kelas-kelas utilitas yang tersedia dan bagaimana menggabungkannya untuk mencapai tampilan yang diinginkan.

**Bootstrap** sebaiknya digunakan ketika:

- Kita ingin mempercepat pengembangan dan tidak memiliki banyak waktu untuk menyesuaikan tampilan.
- masih pemula atau tidak memiliki pengetahuan mendalam tentang CSS, karena Bootstrap menyediakan komponen siap pakai.

### Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).

Pertama, saya menambahkan Bootstrap ke aplikasi dengan menambahkan tag ke `base.html`. Lalu, saya menambahkan sedikit desain untuk halaman `main` (daftar inventori), `login`, `register`, serta halaman **Add Product** dengan beberapa referensi Bootstrap di internet dan dari apa yang telah saya kerjakan di Tutorial 4 juga.


# Tugas 6: JavaScript dan Asynchronous JavaScript

### Jelaskan perbedaan antara _asynchronous programming_ dengan _synchronous programming_.

**Synchronous Programming (Pemrograman Sinkron):**

- Tugas dieksekusi satu per satu secara berurutan.
- Program menunggu setiap tugas selesai sebelum melanjutkan.

**Asynchronous Programming (Pemrograman Asinkron):**

- Tugas dieksekusi tanpa harus menunggu tugas sebelumnya selesai.
- Program melanjutkan eksekusi sementara tugas yang mungkin memakan waktu dilakukan di latar belakang.

### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma _event-driven programming_. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Paradigma **event-driven programming** adalah pendekatan dalam pemrograman di mana program merespons peristiwa atau kejadian (events) yang terjadi, daripada menjalankan tugas secara berurutan. Dalam paradigma ini, program akan "mendengarkan" atau "mengamati" peristiwa dan mengeksekusi tindakan tertentu ketika peristiwa tersebut terjadi. Ini memungkinkan program untuk menjadi responsif terhadap input pengguna dan perubahan keadaan tanpa harus menunggu tugas sebelumnya selesai.

Dalam blok JavaScript, terdapat event listener yang mengamati peristiwa "DOMContentLoaded". Event ini akan dipicu ketika halaman HTML telah sepenuhnya dimuat. Ini memungkinkan kode JavaScript untuk dijalankan setelah halaman siap.

**Contoh:**

```javascript
document.addEventListener("DOMContentLoaded", function () {
    // Kode yang akan dijalankan setelah halaman dimuat.
});
```

### Jelaskan penerapan asynchronous programming pada AJAX.

Penerapan asynchronous programming pada AJAX memungkinkan permintaan asinkronus ke server, yang berarti program dapat melanjutkan eksekusi tanpa harus menunggu respons dari server selesai. Dengan event handling, pengembang dapat menentukan tindakan yang harus diambil ketika respons diterima, menjadikan aplikasi web lebih responsif.

### Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada _library_ jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

#### Fetch API

- **Natif**: Fetch API adalah bagian dari JavaScript, sehingga tidak memerlukan pustaka tambahan. Ini adalah standar modern yang didukung oleh semua browser utama.

- **Promise-based**: Fetch API menggunakan konsep Promise, yang membuat pengkodean asynchronous lebih mudah dibaca dan dipahami.

- **Fungsionalitas Dasar**: Meskipun fetch sangat kuat, ia biasanya digunakan untuk mengambil data dari server (GET) dan mengirimkan data (POST). Operasi lain seperti PUT dan DELETE juga bisa diimplementasikan, tetapi memerlukan kode tambahan.

#### jQuery

- **Pustaka Tambahan**: jQuery adalah pustaka JavaScript yang mencakup banyak fungsi bawaan. Ini lebih besar dalam ukuran daripada Fetch API, yang berarti pengguna harus mengunduh lebih banyak data saat memuat halaman.

- **Callback-based**: jQuery menggunakan gaya callback yang lebih lama untuk mengelola permintaan AJAX. Ini bisa membuat kode terlihat lebih rumit, terutama dalam proyek-proyek besar.

- **Kemudahan Penggunaan**: jQuery memiliki fungsi AJAX yang cukup kuat dan mudah digunakan. Ini memiliki banyak utilitas yang memudahkan dalam menangani permintaan AJAX.

Keputusan akhir tergantung pada kebutuhan proyek, preferensi pribadi, dan apakah ingin mengadopsi pendekatan yang lebih modern dengan Fetch API atau tetap menggunakan utilitas kaya jQuery dalam proyek.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Pertama, saya membuat fungsi untuk mengembalikan data JSON. Lalu, saya mengubah sedikit kode untuk men-_display_ data karena sebelumnya saya belum menggunakan _cards_. Selanjutnya, saya membuat fungsi untuk menambahkan data dengan AJAX, dilanjutkan dengan membuat _form_ untuk menambahkan produk.