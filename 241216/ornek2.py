# Kullanıcıdan kısa ve uzun kenarı alına dikdörtgenin alanı ve çevresi
kisa_kenar = int( input("Kısa Kenarı Girin :") ) #kısa kenarı oku
uzun_kenar = int( input("Uzun Kenarı Girin :") ) #uzun kenarı oku

alan = kisa_kenar *uzun_kenar
cevre = (kisa_kenar + uzun_kenar) * 2

print("Alanı: ",alan,"Çevresi:",cevre)  #Alanı: 200 Çevresi: 60

print(f"Alanı:{alan} Çevresi:{cevre}")  #farklı yöntem

