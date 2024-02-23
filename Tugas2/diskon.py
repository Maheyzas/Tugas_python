uangBelanja = float(input("Masukan Uang Belanja Anda : "))
totalBelanja = float(input("Masukan Total Belanja Anda : "))

if totalBelanja >70.000 :
    diskon = totalBelanja * (10/100)
    print("Anda Mendapatkan Diskon Sebesar %.3f"%(diskon))
else : diskon = 0

kembalian = uangBelanja - totalBelanja + diskon
print("Uang Kembalian Anda : %.3f"%(kembalian))
