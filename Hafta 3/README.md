# Hafta 3: Sentetik Öğrenci Veri Seti

Bu proje ve veri seti (data.csv), 500 hayali öğrencinin ders çalışma alışkanlıkları ile sınav notları arasındaki ilişkiyi analiz etmek ve görselleştirmek amacıyla otomatik kodla üretilmiş **sentetik (kurgusal)** bir veri setidir.

Veri setindeki değişkenlerin isimleri, temsil ettikleri alanlar ve birimleri şu şekildedir:

1. **Ders Çalışma Süresi (`Ders_Calisma_Suresi`):** Öğrencilerin sınava hazırlanırken harcadıkları toplam zamandır. Birimi **Saat**'tir. 0.0 ile 6.0 saat arasında, 1 ondalıklı rasgele sayılarla (örneğin 4.8 saat) kurgulanmıştır.
2. **Sınav Notu (`Sinav_Notu`):** Öğrencilerin sınav sonucunda elde ettikleri başarı puanıdır. Birimi 100 üzerinden **Puan**'dır (10 ile 100 arasında tam sayılar bölgesindedir). Bu notlar standart bir rastgelelikte değil, gerçeğe çok daha yakın olması adına **normal dağılım (çan eğrisi)** formunda (ortalama: 55, standart sapma: 15) özel olarak üretilmiştir.
