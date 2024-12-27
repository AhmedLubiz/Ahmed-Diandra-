# Meminta input usia dari pengguna
try:
    usia = int(input("Masukkan usia Anda: "))
    
    # Menentukan kategori usia menggunakan if-elif-else
    if 0 <= usia <= 5:
        kategori = "Balita"
    elif 6 <= usia <= 12:
        kategori = "Anak-anak"
    elif 13 <= usia <= 17:
        kategori = "Remaja"
    elif 18 <= usia <= 59:
        kategori = "Dewasa"
    elif usia >= 60:
        kategori = "Lansia"
    else:
        kategori = "Usia tidak valid"
    
    # Menampilkan hasil kategori
    print(f"Kategori usia Anda: {kategori}")

except ValueError:
    print("Kesalahan: Masukkan angka yang valid untuk usia.")