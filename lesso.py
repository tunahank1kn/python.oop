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


class Kitap(Kaynak): 
    def __init__(self, baslik, kayitNo, tur, dil):
        super().__init__(baslik, kayitNo) 
        self._tur = tur 
        self._dil = dil 

    @property
    def tur(self):
        return self._tur

    @tur.setter
    def tur(self, deger):
        self._tur = deger

    @property
    def dil(self):
        return self._dil

    @dil.setter
    def dil(self, deger):
        self._dil = deger
    def __str__(self):
        return f"[Kitap] Kayıt No: {self.kayitNo} | Başlık: {self.baslik} | Tür: {self.tur} | Dil: {self.dil}"


class Dergi(Kaynak):
    def __init__(self, baslik, kayitNo, yayin_donemi, kategori):
        super().__init__(baslik, kayitNo) 
     
        self._yayin_donemi = yayin_donemi 
        self._kategori = kategori         

    @property
    def yayin_donemi(self):
        return self._yayin_donemi

    @yayin_donemi.setter
    def yayin_donemi(self, deger):
        self._yayin_donemi = deger

    @property
    def kategori(self):
        return self._kategori

    @kategori.setter
    def kategori(self, deger):
        self._kategori = deger
    def __str__(self):
        return f"[Dergi] Kayıt No: {self.kayitNo} | Başlık: {self.baslik} | Dönem: {self.yayin_donemi} | Kategori: {self.kategori}"


class Islem(ABC): 
    @abstractmethod
    def ekle(self): pass
    
    @abstractmethod
    def sil(self): pass
    
    @abstractmethod
    def guncelle(self): pass
    
    @abstractmethod
    def listele(self): pass


class KitapIslem(Islem): 
    def __init__(self):
        self.kitaplar = [] 
        self.kitap_sayisi = 0 

    def ekle(self):
        print("--- Kitap Ekleme Ekranı ---")
        kayit_no = input("Kitabın kayıt numarasını girin: ")
        
        for k in self.kitaplar:
            if k.kayitNo == kayit_no:
                print("Bu kayıt numarası mevcut.")
                return

        baslik = input("Kitabın başlığını girin: ")
        tur = input("Kitabın türünü girin (Roman, Şiir vb.): ")
        dil = input("Kitabın dilini girin (Türkçe, İngilizce vb.): ")

        yeni_kitap = Kitap(baslik, kayit_no, tur, dil)
        self.kitaplar.append(yeni_kitap)
        self.kitap_sayisi += 1 
        print(" Kitap eklendi.")
        print(f"Toplam Kitap Sayısı: {self.kitap_sayisi}") 

    def listele(self):
        print("--- Kitap Listesi ---")
        if not self.kitaplar:
            print("Kayıt bulunamadı.")
            return
        
        for kitap in self.kitaplar:
            print(kitap) 
    def sil(self):
        print("--- Kitap Silme Ekranı ---")
        kayit_no = input("Silmek istediğiniz kitabın kayıt numarasını girin: ")
        for kitap in self.kitaplar:
            if kitap.kayitNo == kayit_no:
                self.kitaplar.remove(kitap) 
                self.kitap_sayisi -= 1
                print("Kitap silindi.")
                return
        print("Belirtilen kayıt numarasına ait kitap bulunamadı.")

    def guncelle(self):
        print("\n--- Kitap Güncelleme Ekranı ---")
        kayit_no = input("Güncellemek istediğiniz kitabın kayıt numarasını girin: ")
        for kitap in self.kitaplar:
            if kitap.kayitNo == kayit_no:
                print(f"Mevcut Bilgiler -> Başlık: {kitap.baslik}, Tür: {kitap.tur}, Dil: {kitap.dil}")
                
                kitap.baslik = input("Yeni Başlık girin: ")
                kitap.tur = input("Yeni Tür girin: ")
                kitap.dil = input("Yeni Dil girin: ")
                print(" Kitap bilgileri güncellendi.")
                return
        print("Belirtilen kayıt numarasına ait kitap bulunamadı.")


class DergiIslem(Islem):
    def __init__(self):
        self.dergiler = [] 
        self.dergi_sayisi = 0 

    def ekle(self):
        print("\n--- Dergi Ekleme Ekranı ---")
        kayit_no = input("Derginin kayıt numarasını girin: ")
        
        for d in self.dergiler:
            if d.kayitNo == kayit_no:
                print(" HATA: Bu kayıt numarası mevcut, İşlem iptal edildi.")
                return

        baslik = input("Derginin başlığını girin: ")
        yayin_donemi = input("Yayın dönemini girin (Aylık, Haftalık vb.): ")
        kategori = input("Derginin kategorisini girin (Bilim,macera vb.): ")

        yeni_dergi = Dergi(baslik, kayit_no, yayin_donemi, kategori)
        self.dergiler.append(yeni_dergi)
        self.dergi_sayisi += 1
        print(" Dergi başarıyla eklendi.")
        print(f"Toplam Dergi Sayısı: {self.dergi_sayisi}")

    def listele(self):
        print("\n--- Dergi Listesi ---")
    
        if not self.dergiler:
            print(" Kayıt bulunamadı.")
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
                print(" Dergi başarıyla silindi.")
                return
        print(" Belirtilen kayıt numarasına ait dergi bulunamadı.")

    def guncelle(self):
        print("\n--- Dergi Güncelleme Ekranı ---")
        kayit_no = input("Güncellemek istediğiniz derginin kayıt numarasını girin: ")
        for dergi in self.dergiler:
            if dergi.kayitNo == kayit_no:
                print(f"Mevcut Bilgiler -> Başlık: {dergi.baslik}, Dönem: {dergi.yayin_donemi}, Kategori: {dergi.kategori}")
                dergi.baslik = input("Yeni Başlık girin: ")
                dergi.yayin_donemi = input("Yeni Yayın Dönemi girin: ")
                dergi.kategori = input("Yeni Kategori girin: ")
                print("Dergi bilgileri başarıyla güncellendi.")
                return
        print("❌ Belirtilen kayıt numarasına ait dergi bulunamadı.")


class Menu: 
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
    kitap_yoneticisi = KitapIslem()
    dergi_yoneticisi = DergiIslem()

    while True:
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
            print(" İyi günler dilerim")
            break 
        else:
            print("Lütfen 1 ile 9 arasında bir rakam girin.")
if __name__ == "__main__":
    ana_program()