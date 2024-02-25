jerukDibeli = int(input("Berapa Kilo Jeruk Yg Dibeli : "))
apelDibeli = int(input("Berapa Kilo Apel Yg Dibeli : "))
manggaDibeli = int(input("Berapa Kilo Mangga Yg Dibeli : "))
manggisDibeli = int(input("Berapa Kilo Manggis Yg Dibeli : "))
durenDibeli = int(input("Berapa Buah Duren Yg Dibeli : "))

hargaJeruk = 15.000
hargaApel = 30.000
hargaMangga = 20.000
hargaManggis = 7.000
hargaDuren = 50.000

totalJeruk = hargaJeruk * jerukDibeli 
totalApel = hargaApel * apelDibeli
totalMangga = hargaMangga * manggaDibeli
totalManggis = hargaManggis * manggisDibeli
totalDuren = hargaDuren * durenDibeli

totalBelanja = totalJeruk + totalApel + totalMangga + totalManggis + totalDuren

print("Total Yg Anda Harus Bayar Adalah : %.3f"%(totalBelanja))
print(str(jerukDibeli) + (" Kilo Jeruk : %.3f"%(totalJeruk)))
print(str(apelDibeli) + (" Kilo Apel : %.3f"%(totalApel)))
print(str(manggaDibeli) + (" Kilo Mangga : %.3f"%(totalMangga)))
print(str(manggisDibeli) + (" Kilo Manggis : %.3f"%(totalManggis)))
print(str(durenDibeli) + (" Buah Duren : %.3f"%(totalDuren)))
print("Total belanja Anda : %.3f"%(totalBelanja))