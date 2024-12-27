# Fungsi untuk operasi dasar
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:  # Menangani pembagian dengan nol
        return "Kesalahan: Tidak dapat membagi dengan nol"
    return a / b

# Menampilkan menu operasi kepada pengguna
print("Pilih operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

# Meminta pengguna memilih operasi
pilihan = input("Masukkan pilihan (1/2/3/4): ")

# Meminta pengguna memasukkan dua angka
try:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
except ValueError:
    print("Kesalahan: Input harus berupa angka.")
    exit()

# Melakukan operasi berdasarkan pilihan pengguna
if pilihan == "1":
    print(f"Hasil: {tambah(angka1, angka2)}")
elif pilihan == "2":
    print(f"Hasil: {kurang(angka1, angka2)}")
elif pilihan == "3":
    print(f"Hasil: {kali(angka1, angka2)}")
elif pilihan == "4":
    print(f"Hasil: {bagi(angka1, angka2)}")
else:
    print("Kesalahan: Pilihan tidak valid.")