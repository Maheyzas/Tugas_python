jerukDibeli = int(input("Berapa Kilo Jeruk Yg Dibeli : "))
apelDibeli = int(input("Berapa Kilo Apel Yg Dibeli : "))
manggaDibeli = int(input("Berapa Kilo Mangga Yg Dibeli : "))
manggisDibeli = int(input("Berapa Kilo Manggis Yg Dibeli : "))
durenDibeli = int(input("Berapa Buah Duren Yg Dibeli : "))

hargaJeruk = 15000
hargaApel = 30000
hargaMangga = 20000
hargaManggis = 7000
hargaDuren = 50000

totalJeruk = hargaJeruk * jerukDibeli 
totalApel = hargaApel * apelDibeli
totalMangga = hargaMangga * manggaDibeli
totalManggis = hargaManggis * manggisDibeli
totalDuren = hargaDuren * durenDibeli

totalBelanja = totalJeruk + totalApel + totalMangga + totalManggis + totalDuren

print("Total Yg Anda Harus Bayar Adalah : " + str(totalBelanja))
print(str(jerukDibeli) + (" Kilo Jeruk : ") + str(totalJeruk))
print(str(apelDibeli) + (" Kilo Apel : ") + str(totalApel))
print(str(manggaDibeli) + (" Kilo Mangga : ") + str(totalMangga))
print(str(manggisDibeli) + (" Kilo Manggis : ") + str(totalManggis))
print(str(durenDibeli) + (" Buah Duren : ") + str(totalDuren))
print("Total belanja Anda : " + str(totalBelanja))