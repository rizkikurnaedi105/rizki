# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 20:41:32 2021

"""

import datetime
times = datetime.datetime.now()


gapok = [2500000,4500000,6500000]
tunis = [0.01,0.03,0.05]
tunak = 0.02
jk = ["Laki-Laki","Perempuan"]
status = ["Belum Kawin","Sudah Kawin"]
b_jabatan = 0.05
iuran_pensiun = 15500
iuran_organisasi = 3500
golongan = [1,2,3]


nama = str(input("Masukkan Nama Anda >> "))
print("1. GOLONGAN 1    =    Rp.2.500.000")
print("2. GOLONGAN 2    =    Rp.4.500.000")
print("3. GOLONGAN 3    =    Rp.6.500.000")
gol = int(input("Anda Termasuk dalam Golongan keberapa? (1-3) >> "))
if gol == 1:
    idx = 0
if gol == 2:
    idx = 1
if gol == 3:
    idx = 2


golongans = golongan[idx]
gajipokok = gapok[idx]
ti = tunis[idx]




print("1. Laki-Laki")
print("2. Perempuan")
cek_jk = int(input("Pilih Jenis Kelamin Anda >> "))
if cek_jk == 1:
    idx = 0
if cek_jk == 2:
    idx = 1
    
jenis_kelamin = jk[idx]


cek_status = str(input("Apakah Anda Sudah Kawin? (Y/T) >> "))
if cek_status == 't':
    idx = 0
if cek_status == 'y':
    idx = 1
    cek_anak = int(input("Masukkan Jumlah Anak (Isi 0 Apabila Tidak Punya) >> "))
    if cek_anak != 0:
        sts_anak = True
    else:
        sts_anak = False
   
status_kawin = status[idx]

    
if jenis_kelamin == "Laki-Laki" and status_kawin == "Sudah Kawin":
    tunjangan_istri = ti * gajipokok
else:
    tunjangan_istri = 0

if status_kawin == "Sudah Kawin" and sts_anak == True:
    tunjangan_anak = tunak * gajipokok
else:
    tunjangan_anak = 0
    
gaji_bruto = gajipokok + tunjangan_anak + tunjangan_istri

biaya_jabatan = b_jabatan * gaji_bruto

gaji_netto = gaji_bruto - biaya_jabatan - iuran_pensiun - iuran_organisasi

detail = input("Tekan Enter Untuk Lihat Detail")

print()
print("{:13}".format("") + "SLIP GAJI")
print("{:5}".format("") + str(times))
print("{:19}".format("Nama") + "{:5}".format("=") + nama)
print("{:19}".format("Golongan") + "{:5}".format("=") + str(golongans))
print("{:19}".format("Jenis Kelamin") + "{:5}".format("=") + jenis_kelamin)
print("{:19}".format("Status Kawin") + "{:5}".format("=") + status_kawin)
print("{:19}".format("Gaji Pokok") + "{:5}".format("=") + "Rp" + format(gajipokok,',.2f'))
print("{:19}".format("Tunjangan Istri") + "{:5}".format("=") + "Rp" + format(tunjangan_istri,',.2f'))
print("{:19}".format("Tunjangan Anak") + "{:5}".format("=") + "Rp" + format(tunjangan_anak,',.2f'))
print("{:19}".format(">> Gaji Bruto") + "{:5}".format("=") + "Rp" + format(gaji_bruto,',.2f'))
print("---------------------------------------")
print("{:19}".format("Biaya Jabatan") + "{:5}".format("=") + "Rp" + format(biaya_jabatan,',.2f'))
print("{:19}".format("Iuran Pensiun") + "{:5}".format("=") + "Rp" + format(iuran_pensiun,',.2f'))
print("{:19}".format("Iuran Organisasi") + "{:5}".format("=") + "Rp" + format(iuran_organisasi,',.2f'))
print("{:19}".format(">> Gaji Netto") + "{:5}".format("=") + "Rp" + format(gaji_netto,',.2f'))

leave = input("Klik Enter untuk Keluar")