import sqlite3
import os


print("Veritabanı şu konuma kaydedilecek:", os.getcwd())


baglanti = sqlite3.connect("filmlerim.db")
cursor = baglanti.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS filmler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ad TEXT,
        yil INTEGER,
        puan REAL
    )
""")
baglanti.commit()

def menu_goster():
    print("\n--- FİLM ARŞİV SİSTEMİ ---")
    print("1. Film Ekle")
    print("2. Filmleri Listele")
    print("3. Film Sil")
    print("4. Çıkış")

def film_ekle():
    print("\n-- Yeni Film Ekle --")
    ad = input("Film Adı: ")
    yil = int(input("Yapım Yılı: "))
    puan = float(input("IMDB Puanı: "))
    
    cursor.execute("INSERT INTO filmler (ad, yil, puan) VALUES (?, ?, ?)", (ad, yil, puan))
    baglanti.commit()
    print(f"\n✅ '{ad}' başarıyla veritabanına eklendi!")

def filmleri_listele():
    print("\n--- KAYITLI FİLMLER ---")
    cursor.execute("SELECT * FROM filmler")
    filmler = cursor.fetchall()
    
    if len(filmler) == 0:
        print("Henüz hiç film eklenmemiş.")
    else:
        for film in filmler:
            print(f"ID: {film[0]} | Film: {film[1]} ({film[2]}) | Puan: {film[3]}")

def film_sil():
    filmleri_listele()
    silinecek_id = input("\nSilmek istediğiniz filmin ID numarasını girin: ")
    
    cursor.execute("DELETE FROM filmler WHERE id = ?", (silinecek_id,))
    baglanti.commit()
    print("\n🗑️ Film başarıyla silindi.")


while True:
    menu_goster()
    secim = input("Seçiminiz (1-4): ")
    
    if secim == '1':
        film_ekle()
    elif secim == '2':
        filmleri_listele()
    elif secim == '3':
        film_sil()
    elif secim == '4':
        print("Çıkış yapılıyor...")
        baglanti.close()
        break
    else:
        print("Geçersiz seçim! Lütfen 1-4 arası bir sayı girin.")


