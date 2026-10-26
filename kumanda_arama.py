#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kumanda Kaybolma Teorisi - Bilimsel Arama Simülatörü
Bu kod, kaybolan kumandanın yerini bulmak için evrenin en gelişmiş algoritmasını kullanır.
(Aslında rastgele bahane üretir.)
"""

import random
import time

bahaneler = [
    "Kumanda koltuk minderinin altında, çünkü kedi onu yastık sanmış.",
    "Televizyonun arkasında, çünkü uzay-zaman bükülmesi yaşandı.",
    "Buzdolabının içinde, dün gece gece yarısı açık açık yemeye çalışırken unutulmuş.",
    "Komşunun balkonunda, rüzgar onu kaçırmış (komşu da kabul etmiyor).",
    "Yastığın altında, çünkü rüyanda kumanda ile uzay gemisi kullanıyordun.",
    "Çamaşır makinesinde, çamaşırlarla birlikte yıkanmayı sevdiği için.",
    "Kitaplığın en üst rafında, çünkü kumanda da kitap okumayı seviyor.",
    "Koltukların arasında kaybolmuş, çünkü o da senin gibi 'biraz dinleneyim' demiş.",
    "Banyoda, çünkü televizyon izlerken tuvalete gitmek için yanına almışsın.",
    "Hiçbir yerde yok, çünkü kumanda quantum tünellemesi yaparak başka bir boyuta geçti."
]

def kumanda_ara():
    print("Kumanda arama protokolü başlatılıyor...")
    print("Evrenin tüm köşeleri taranıyor (bu 3 saniye sürebilir)...")
    time.sleep(3)
    bahane = random.choice(bahaneler)
    print(f"\nSONUÇ: {bahane}")
    print("\nTeori doğrulandı. Kumanda yine kayıp. Bir daha arama.")
    # Gizli not: Bu sistem aslında devletin bütçe açığını da açıklayabilir ama kimse sormasın.

if __name__ == "__main__":
    kumanda_ara()
