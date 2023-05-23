aplikasi = {
    1: ['A', 'B','D','E','F'],
    2: ['B','D','G'],
    3: ['C','F','G','B']
}

set_aplikasi = []
for keys in aplikasi.keys():
    set_aplikasi.append(set(aplikasi[keys]))

# tampilkan semua aplikasi di semua kategori(tanpa duplikat)
hasil = set_aplikasi[0] | set_aplikasi[1] | set_aplikasi[2]
print(f"semua aplikasi yang ada: {hasil}")

# tampilkan aplikasi yang muncul di semua kategori
hasil = set_aplikasi[0] & set_aplikasi[1] & set_aplikasi[2] # harus dibuat dinamis
print(f"Aplikasi disemua kategori: {hasil}")