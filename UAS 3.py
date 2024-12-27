# Fungsi untuk menghitung gaji bulanan
def hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja):
    total_gaji = 0  # Inisialisasi total gaji

    for hari in range(1, hari_kerja + 1):
        if jam_kerja_per_hari[hari - 1] > 8:
            # Jam kerja lebih dari 8 jam, hitung lembur
            lembur = jam_kerja_per_hari[hari - 1] - 8
            gaji_harian = (8 * tarif_per_jam) + (lembur * tarif_per_jam * 1.5)
        else:
            # Jam kerja normal
            gaji_harian = jam_kerja_per_hari[hari - 1] * tarif_per_jam

        total_gaji += gaji_harian

    return total_gaji


# Input dari pengguna
tarif_per_jam = float(input("Masukkan tarif gaji per jam: "))
hari_kerja = int(input("Masukkan jumlah hari kerja dalam sebulan: "))

# Input jam kerja setiap hari
jam_kerja_per_hari = []
print("Masukkan jam kerja untuk setiap hari:")
for i in range(hari_kerja):
    jam_kerja = float(input(f"Jam kerja hari ke-{i + 1}: "))
    jam_kerja_per_hari.append(jam_kerja)

# Hitung total gaji
total_gaji = hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja)

# Cetak total gaji bulanan
print(f"\nTotal gaji bulanan Anda adalah: Rp {total_gaji:,.2f}")