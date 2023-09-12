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
