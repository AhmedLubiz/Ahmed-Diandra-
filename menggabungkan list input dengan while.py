listkota = [
    'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
    'Yokjakarta', 'semarang', 'makasar'
]

KotaYangDicari = input('Masukkan nama kota yang dicari: ')

i = 0 
while i < len(listkota):
    if listkota[i].lower() == KotaYangDicari.lower():
        print(listkota[i])
        break

    print('Bukan', listkota[i])
    i += 1
else:
    print('Maaf, kota yang anda cari tidak ditemukan')
