#bolean

print("membuat bolean and")
print(True and True)
print(True and False)
print(False and True)
print(False and False)


print("membuat bolean or")
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print("membuat bolean not")
print( not False)
print( not True)

print("membuat operator perbandinan")
#> lebih dari
#< kurang dari
#>= lebih dari sama dengan
#<= kurang dari sama dengan
#== sama dengan
#!= tidak sama dengan

print("nilai yang benar/true")
print(8 > 4)
print(3 < 9)
print(10 >= 2)
print(4 <= 5)
print(5 == 5)
print(12 != 3)

print("nilai yang salah/false")
print(12 > 15)
print(14 < 10)
print(2 >= 3)
print(12 == 2)
print(35 != 35)

print("Latihan soal")
print("No.1 materi input-buatlah program yang menghasilkan pengguna memsasukkan nama,umur,hobi,dan terakhir tampilkan sapaan")
print("No.2 materi input number-buatlah program yang meminta pengguna memasukkan umur, lalu tampilkan umur 2 tahun lagi")
print("No.3 Materi perbandingan-Butlah program yang mengecek apakah umur seseorang itu antara 10 sampai 17 tahun disebut(remaja)")

print("jawaban No.1")
print("masukkan nama anda")
nama = input()
print("masukkan umur anda")
umur = input()
print("masukkan hobi anda")
hobi = input()
print(f"halo nama saya {nama}, umur saya {umur} tahun, dan hobi saya adalah{hobi}")

print("Jawaban No.2")
print("masukkan umur anda")
umur = int(input())
umur_2_tahun = umur + 2
print(f"umur anda 2 tahun lagi adalah {umur_2_tahun} tahun")

print("Jawaban no.3")
print("masukkan umur anda")
umur = int(input())
remaja = (10 <= umur <=17)
print(f"apakah anda remaja? {remaja}")



