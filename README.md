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
