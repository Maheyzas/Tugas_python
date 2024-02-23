uangBelanja = int(input("Masukan Uang Belanja Anda : "))
totalBelanja = int(input("Masukan Total Belanja Anda : "))

if totalBelanja >70000 :
    diskon = totalBelanja * (10/100)
else : diskon = 0

print("Anda Mendapatkan Diskon Sebesar " + str(diskon))


kembalian = uangBelanja - totalBelanja + diskon
print("Uang Kembalian Anda : " + str(kembalian))
