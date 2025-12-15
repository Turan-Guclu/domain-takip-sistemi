📌 Proje Hakkında

Bu proje, Python ile geliştirilmiş bir domain (alan adı) takip sistemidir.
Belirlenen domainlerin sürelerini düzenli olarak kontrol eder ve süresi geçmiş veya süresi dolmak üzere olan domainler için tanımlanan e-posta adreslerine otomatik bildirim gönderir.

Proje, Linux sunucularda crontab üzerinden çalışacak şekilde tasarlanmıştır ve tamamen zamanlanmış (otomatik) bir yapıya sahiptir.

⚙️ Kullanılan Paketler

Projede Python’un standart kütüphaneleri kullanılmıştır:

smtplib – E-posta gönderimi

subprocess – Sistem komutlarının çalıştırılması

re – Domain çıktılarının düzenli ifadelerle işlenmesi

datetime – Tarih ve süre hesaplamaları

Ekstra bir paket kurulumu gerektirmez.

⏱️ Çalışma Mantığı

Belirlenen domain listesi kontrol edilir

Domain süresi dolmuş veya sona yaklaşmışsa tespit edilir

Tanımlı e-posta adreslerine otomatik uyarı maili gönderilir

Sistem, crontab ile istenilen gün ve saatte çalıştırılabilir

🐧 Sistem Gereksinimleri

Linux tabanlı bir sunucu

Python 3.x

Crontab erişimi

✉️ Kullanım Senaryosu

Bu proje özellikle:

Birden fazla domain yönetenler

Hosting firmaları

Sistem yöneticileri

Süre takibini manuel yapmak istemeyen kullanıcılar

için uygundur.
