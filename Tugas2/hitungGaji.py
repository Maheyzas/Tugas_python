gajiPokok = float(input("Masukan Gaji Pokok Anda : "))
hariKerja = int(input("Masukan Total Hari Kerja Dalam Sebulan : "))
jamLembur = int(input("Masukan Total Jam Lembur : "))

transportHarian = 50.000
makanHarian = 50.000
tunjanganJabatan = 500.000
honorLembur = 15.000

transportBulan = transportHarian * hariKerja
makanBulan = makanHarian * hariKerja
totalLembur = honorLembur * jamLembur

totalGaji = gajiPokok + transportBulan + makanBulan + tunjanganJabatan + totalLembur

print("Total Gaji Anda  Sebulan : %.3f"%(totalGaji))