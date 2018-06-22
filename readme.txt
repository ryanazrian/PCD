Cara aplikasi prediksi tingkat kematangan dan berat tomat

Bagian Pertama (MAIN)
1. Aplikasi terdiri atas beberapa bagian, aplikasi utama yang dapat langsung digunakan terdapat dalam folder "WEB"
2. Untuk menjalankan aplikasi dalam folder WEB dapat dengan mengetik "python app.py" dalam folder "WEB", (Harus mengistall flask python dan dependencies nya terlebih dahulu)
3. Kemudian membuka http://localhost:5000 dari browser
4. Aplikasi dapat dijalankan melalui browser dengan mengupload gambar tomat dan aplikasi akan memprediksi tingkat kematangan dan berat buah tomat tersebut
5. Aplikasi dijalankan pada script "app.py" dengan memanggil fungsi-fungsi pada script "kumpulankode.py", "object_size.py" dan "Testing1.py"

Bagian Kedua (ekstraksi fitur)
1. Untuk melakukan ekstraksi fitur data training dapat menjalankan script "code.py" pada root utama
2. Gambar yang akan di ekstraksi fiturnya adalah semua gambar yang terletak pada folder "tomat"
3. Hasil ekstraksi fitur akan disimpan ke dalam berkas bernama "tomat.csv"
4. Kemudian hasil ekstraksi fitur tersebut akan dilakukan tahapan oversampling menggunakan Rstudio (untuk menjalankan scriptnya bernama 'oversampling.r' yang terletak di directory utama)\
5. Hasil oversampling akan di export dalam bentuk csv yang bernama 'afteroversampling.csv'

Bagian Ketiga (Pembuatan Model)
1. Untuk melakukan pembuatan model jalankan script "klasifikasi.py" dengan mengetik di terminal "python klasifikasi.py"
2. Dari script tersebut akan dihasilkan 2 buah model, yaitu model untuk prediksi tingkat kematangan dan model untuk prediksi berat

Bagian Keempat (apps android)
1. Apps android dikembangkan menggunakan framework react native
2. Apps android terletak dalam folder "ANDROID"
3. Apps belum di deploy, sehingga untuk menjalankannya harus mengetik "react-native run android" di terminal pada folder "ANDROID"
4. Sebelum Menjalankankan petunjuk 3, diharuskan untuk menjalankan servernya dengan mengetik "python app.py" di terminal pada folder WEB