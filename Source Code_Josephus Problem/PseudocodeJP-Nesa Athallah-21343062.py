def josephus(n, k):
    # n: jumlah orang dalam kelompok
    # k: setiap k orang akan dibunuh

    # membuat list untuk menampung orang-orang dalam kelompok
    orang = list(range(1, n+1))

    # menghitung indeks awal dan jumlah orang yang tersisa
    indeks = 0
    sisa = n

    # melakukan loop sampai hanya satu orang yang tersisa
    while sisa > 1:
        # menghitung indeks orang yang akan dibunuh
        indeks = (indeks + k - 1) % sisa

        # menghapus orang yang akan dibunuh dari list
        orang.pop(indeks)

        # mengupdate jumlah orang yang tersisa
        sisa -= 1

    # mengembalikan orang yang tersisa sebagai jawaban
    return orang[0]
    # menjalankan algoritma untuk kelompok 7 orang, setiap 3 orang dibunuh
print(josephus(7, 3)) 
    # hasilnya adalah 4