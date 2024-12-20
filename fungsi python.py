# Membuat Fungsi
def salam():
    print ("Hello, Selamat Pagi")

## Pemanggilan Fungsi
salam()
salam()
salam()

# Membuat fungsi dengan parameter
def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    print ("Luas segitiga: %f" % luas)

# Pemanggilan fungsi
luas_segitiga(4, 6)

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

# pemanggilan fungsi
print ("Luas persegi: %d" % luas_persegi(6))

# rumus sisi x sisi
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

# rumus sisi x sisi x sisi
def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi

# contoh penggunaan
sisi = 3
print("Luas persegi:", luas_persegi(sisi))
print("Volume kubus:", volume_persegi(sisi))

# pemanggilan fungsi
print ("volume_persegi: %d" % luas_persegi(5))

# membuat variabel global
nama = "Belajar Kode"
versi = "1.0.0"

def help():
    # ini variabel lokal
    nama = "Programku"
    versi = "1.0.1"
    # mengakses variabel lokal
    print ("Nama: %5" % nama)
    print ("Versi: %5" % versi)

# mengakses variabel global
print ("Nama: %5" % nama)
print ("Versi: %5" % versi)

# memanggil fungsi help()
help()