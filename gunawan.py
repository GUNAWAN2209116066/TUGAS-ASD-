import math

nama = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

def jump_search(arr, x):
    panjang = len(arr)
    jump = int(math.sqrt(panjang))
    kiri, kanan = 0, 0
    while kiri < panjang and arr[kiri] <= x:
        kanan = min(panjang- 1, kiri + jump)
        if arr[kiri] <= x and arr[kanan] >= x:
            break
        kiri += jump
    if kiri >= panjang or arr[kiri] > x:
        return -1
    kanan = min(panjang - 1, kanan)
    i = kiri
    while i <= kanan and arr[i] <= x:
        if arr[i] == x:
            return i
        i += 1
    return -1

def tampilanjump():
    print("")
    print("Jump Search")
        # Cari Arsel
    idx_arsel = jump_search(nama, "Arsel")
    if idx_arsel != -1:
        print("Arsel di Index", idx_arsel)
    else:
        print("Arsel tidak ditemukan")

    # Cari Avivah
    idx_avivah = jump_search(nama, "Avivah")
    if idx_avivah != -1:
        print("Avivah di Index", idx_avivah)
    else:
        print("Avivah tidak ditemukan")

    # Cari Daiva
    idx_daiva = jump_search(nama, "Daiva")
    if idx_daiva != -1:
        print("Daiva di Index", idx_daiva)
    else:
        print("Daiva tidak ditemukan")

    # Cari Wahyu
    idx_wahyu = jump_search(nama[3], "Wahyu")
    if idx_wahyu != -1:
        print("Wahyu pada Index 3 di kolom 0")
    else:
        print("Wahyu tidak ditemukan")

    # Cari Wibi
    idx_wibi = jump_search(nama[3], "Wibi")
    if idx_wibi != -1:
        print("Wibi pada Index 3 di kolom 1")
    else:
        print("Wibi tidak ditemukan")



def menu():
    print("Jump Search dari data ini", nama)
    input ("Tekan enter untuk melanjutkan")
    tampilanjump()
menu()        

