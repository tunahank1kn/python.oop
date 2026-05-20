from abc import ABC, abstractmethod 

class Kaynak(ABC): 
    def __init__(self, baslik, kayitNo):
        self._baslik = baslik   
        self._kayitNo = kayitNo 

    @property
    def baslik(self):
        return self._baslik

    @baslik.setter
    def baslik(self, deger):
        self._baslik = deger

    @property
    def kayitNo(self):
        return self._kayitNo

    @kayitNo.setter
    def kayitNo(self, deger):
        self._kayitNo = deger


class Kitap(Kaynak): # 2.2 Kalıtım Kuralı: Kitap sınıfı Kaynak'tan miras alıyor.
    def __init__(self, baslik, kayitNo, tur, dil):
        # super().__init__() kullanarak üst sınıfın constructor'ını tetikliyoruz.
        super().__init__(baslik, kayitNo) 
        # Senin seçtiğin kitaba özel 2 yeni özellik:
        self._tur = tur 
        self._dil = dil 

    # Tür özelliği için Getter ve Setter
    @property
    def tur(self):
        return self._tur

    @tur.setter
    def tur(self, deger):
        self._tur = deger

    # Dil özelliği için Getter ve Setter
    @property
    def dil(self):
        return self._dil

    @dil.setter
    def dil(self, deger):
        self._dil = deger

    # BÖLÜM 3 (Bonus): print(kitap) deyince ekrana düzgün çıktı versin diye __str__ metodu
    def __str__(self):
        return f"[Kitap] Kayıt No: {self.kayitNo} | Başlık: {self.baslik} | Tür: {self.tur} | Dil: {self.dil}"


class Dergi(Kaynak): # 2.2 Kalıtım Kuralı: Dergi sınıfı Kaynak'tan miras alıyor.
    def __init__(self, baslik, kayitNo, yayin_donemi, kategori):
        super().__init__(baslik, kayitNo) # Üst sınıfı başlattık
        # Senin seçtiğin dergiye özel 2 yeni özellik:
        self._yayin_donemi = yayin_donemi 
        self._kategori = kategori         

    # Yayın Dönemi özelliği için Getter ve Setter
    @property
    def yayin_donemi(self):
        return self._yayin_donemi

    @yayin_donemi.setter
    def yayin_donemi(self, deger):
        self._yayin_donemi = deger

    # Kategori özelliği için Getter ve Setter
    @property
    def kategori(self):
        return self._kategori

    @kategori.setter
    def kategori(self, deger):
        self._kategori = deger

    # BÖLÜM 3 (Bonus): print(dergi) için __str__ metodu
    def __str__(self):
        return f"[Dergi] Kayıt No: {self.kayitNo} | Başlık: {self.baslik} | Dönem: {self.yayin_donemi} | Kategori: {self.kategori}"


# ==========================================
# 2. BÖLÜM: İŞLEM VE CRUD MANTIKSAL KATMANI
# ==========================================

class Islem(ABC): # 2.3 Soyut İşlem Sınıfı (Şemadaki üst sağ kutu)
    # İçindeki tüm metodlar @abstractmethod oldu. Alt sınıflar bunları override etmek zorunda!
    @abstractmethod
    def ekle(self): pass
    
    @abstractmethod
    def sil(self): pass
    
    @abstractmethod
    def guncelle(self): pass
    
    @abstractmethod
    def listele(self): pass


class KitapIslem(Islem): # İşlem sınıfından türetilen Kitap CRUD katmanı
    def __init__(self):
        self.kitaplar = [] # Eklenen kitap nesnelerini bu dinamik listede saklayacağız
        self.kitap_sayisi = 0 # BÖLÜM 3 (Bonus): Toplam kayıt sayısını tutan değişken

    def ekle(self):
        print("\n--- Kitap Ekleme Ekranı ---")
        kayit_no = input("Kitabın kayıt numarasını girin: ")
        
        # BÖLÜM 3 (Bonus): Aynı kayıt numarasıyla ikinci kayıt eklenmesini engelleme kontrolü
        for k in self.kitaplar:
            if k.kayitNo == kayit_no:
                print("❌ HATA: Bu kayıt numarası zaten sistemde mevcut! İşlem iptal edildi.")
                return

        baslik = input("Kitabın başlığını girin: ")
        tur = input("Kitabın türünü girin (Roman, Şiir vb.): ")
        dil = input("Kitabın dilini girin (Türkçe, İngilizce vb.): ")

        # Alınan bilgilerle yeni bir Kitap nesnesi oluşturup listeye atıyoruz
        yeni_kitap = Kitap(baslik, kayit_no, tur, dil)
        self.kitaplar.append(yeni_kitap)
        self.kitap_sayisi += 1 # Sayacı 1 arttırdık
        print("✔️ Kitap başarıyla eklendi.")
        print(f"Toplam Kitap Sayısı: {self.kitap_sayisi}") # Bonus puanı garantileme

    def listele(self):
        print("\n--- Kitap Listesi ---")
        # BÖLÜM 3 (Bonus): Liste boşken "Kayıt bulunamadı" mesajı gösterme kontrolü
        if not self.kitaplar:
            print("⚠️ Kayıt bulunamadı.")
            return
        
        for kitap in self.kitaplar:
            print(kitap) # Yukarıda yazdığımız __str__ metodu sayesinde ekrana şık basılacak

    def sil(self):
        print("\n--- Kitap Silme Ekranı ---")
        kayit_no = input("Silmek istediğiniz kitabın kayıt numarasını girin: ")
        for kitap in self.kitaplar:
            if kitap.kayitNo == kayit_no:
                self.kitaplar.remove(kitap) # Listeden nesneyi siliyoruz
                self.kitap_sayisi -= 1
                print("✔️ Kitap başarıyla silindi.")
                return
        print("❌ Belirtilen kayıt numarasına ait kitap bulunamadı.")

    def guncelle(self):
        print("\n--- Kitap Güncelleme Ekranı ---")
        kayit_no = input("Güncellemek istediğiniz kitabın kayıt numarasını girin: ")
        for kitap in self.kitaplar:
            if kitap.kayitNo == kayit_no:
                print(f"Mevcut Bilgiler -> Başlık: {kitap.baslik}, Tür: {kitap.tur}, Dil: {kitap.dil}")
                # Setter metodlarını tetikleyerek verileri güncelliyoruz
                kitap.baslik = input("Yeni Başlık girin: ")
                kitap.tur = input("Yeni Tür girin: ")
                kitap.dil = input("Yeni Dil girin: ")
                print("✔️ Kitap bilgileri başarıyla güncellendi.")
                return
        print("❌ Belirtilen kayıt numarasına ait kitap bulunamadı.")


class DergiIslem(Islem): # İşlem sınıfından türetilen Dergi CRUD katmanı
    def __init__(self):
        self.dergiler = [] # Dergi nesnelerini tutan liste
        self.dergi_sayisi = 0 # BÖLÜM 3 (Bonus): Toplam dergi sayısı

    def ekle(self):
        print("\n--- Dergi Ekleme Ekranı ---")
        kayit_no = input("Derginin kayıt numarasını girin: ")
        
        # BÖLÜM 3 (Bonus): Kayıt numarası benzersizlik kontrolü
        for d in self.dergiler:
            if d.kayitNo == kayit_no:
                print("❌ HATA: Bu kayıt numarası zaten sistemde mevcut! İşlem iptal edildi.")
                return

        baslik = input("Derginin başlığını girin: ")
        yayin_donemi = input("Yayın dönemini girin (Aylık, Haftalık vb.): ")
        kategori = input("Derginin kategorisini girin (Bilim, Spor vb.): ")

        yeni_dergi = Dergi(baslik, kayit_no, yayin_donemi, kategori)
        self.dergiler.append(yeni_dergi)
        self.dergi_sayisi += 1
        print("✔️ Dergi başarıyla eklendi.")
        print(f"Toplam Dergi Sayısı: {self.dergi_sayisi}")

    def listele(self):
        print("\n--- Dergi Listesi ---")
        # BÖLÜM 3 (Bonus): Boş liste uyarısı
        if not self.dergiler:
            print("⚠️ Kayıt bulunamadı.")
            return
        
        for dergi in self.dergiler:
            print(dergi)

    def sil(self):
        print("\n--- Dergi Silme Ekranı ---")
        kayit_no = input("Silmek istediğiniz derginin kayıt numarasını girin: ")
        for dergi in self.dergiler:
            if dergi.kayitNo == kayit_no:
                self.dergiler.remove(dergi)
                self.dergi_sayisi -= 1
                print("✔️ Dergi başarıyla silindi.")
                return
        print("❌ Belirtilen kayıt numarasına ait dergi bulunamadı.")

    def guncelle(self):
        print("\n--- Dergi Güncelleme Ekranı ---")
        kayit_no = input("Güncellemek istediğiniz derginin kayıt numarasını girin: ")
        for dergi in self.dergiler:
            if dergi.kayitNo == kayit_no:
                print(f"Mevcut Bilgiler -> Başlık: {dergi.baslik}, Dönem: {dergi.yayin_donemi}, Kategori: {dergi.kategori}")
                dergi.baslik = input("Yeni Başlık girin: ")
                dergi.yayin_donemi = input("Yeni Yayın Dönemi girin: ")
                dergi.kategori = input("Yeni Kategori girin: ")
                print("✔️ Dergi bilgileri başarıyla güncellendi.")
                return
        print("❌ Belirtilen kayıt numarasına ait dergi bulunamadı.")


# ==========================================
# 3. BÖLÜM: MENÜ TASARIMI VE ANA PROGRAM DÖNGÜSÜ
# ==========================================

class Menu: # Ekrana menüyü basan normal sınıfımız
    @staticmethod
    def menuyu_goster():
        print("\n" + "="*35)
        print(" KÜTÜPHANE YÖNETİM SİSTEMİ MENÜSÜ")
        print("="*35)
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitap Güncelle")
        print("4. Kitapları Listele")
        print("5. Dergi Ekle")
        print("6. Dergi Sil")
        print("7. Dergi Güncelle")
        print("8. Dergileri Listele")
        print("9. Çıkış")
        print("="*35)


def ana_program():
    # İşlemleri yönetebilmek için kontrolcü sınıflardan nesnelerimizi (nesne örneklerini) türetiyoruz
    kitap_yoneticisi = KitapIslem()
    dergi_yoneticisi = DergiIslem()

    while True: # 2.4 Menü Döngüsü Kuralı: Program 9'a basana kadar sonsuz döngüde çalışır.
        Menu.menuyu_goster()
        secim = input("Yapmak istediğiniz işlemi seçin (1-9): ")

        if secim == "1":
            kitap_yoneticisi.ekle()
        elif secim == "2":
            kitap_yoneticisi.sil()
        elif secim == "3":
            kitap_yoneticisi.guncelle()
        elif secim == "4":
            kitap_yoneticisi.listele()
        elif secim == "5":
            dergi_yoneticisi.ekle()
        elif secim == "6":
            dergi_yoneticisi.sil()
        elif secim == "7":
            dergi_yoneticisi.guncelle()
        elif secim == "8":
            dergi_yoneticisi.listele()
        elif secim == "9":
            print("👋 Sistemden çıkılıyor. Başarılar dileriz, reis!")
            break # Döngüyü kırar ve uygulamayı kapatır.
        else:
            print("⚠️ Geçersiz seçim! Lütfen 1 ile 9 arasında bir rakam girin.")

# Python projelerinde kodun ana tetikleyicisi (Main fonksiyonu gibi çalışır)
if __name__ == "__main__":
    ana_program()