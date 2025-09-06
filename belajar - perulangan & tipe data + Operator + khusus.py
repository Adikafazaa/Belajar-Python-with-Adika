#Perulangan + Tipe data + Operator + Tipe data khusus

# Perulangan itu ada 2 jenis aja yaitu : 'for' & 'while'

print("'For' Looping")
# 1. For(for), ini teh bisa ngambil data dari list + bikin perulangan dari range + operator. Contohnya : 
# Contoh 1, ngambil data dari list : 

jenis_handphone = { #disini pake dictionary karna ada key(item) dan value(harga dari item)
    "asus" : 2000000,
    "lenovo" : 3000000,
    "xiaomi" : 3000000,
    "iphone" : 15000000,
    "samsung" : 15000000
}

for handphone, harga in jenis_handphone.items(): 
    print(f"{handphone} : {harga}") #disini urang pake print(f) karna nambahin value didalem print biar gercep  
# Kok bisa ada nampilin banyak item walaupun dalam 1 syntax sih dik ? karna urang pake tambahan syntax ini : .items()

# Contoh 2, bikin perulangan dari range (ke-1) :

for angka in range(10): #variable "angka" yang ada disini hanya sementara, alias hanya untuk proses (for) ini saja. kemudian (range) ini untuk bikin deretan angka. ada banyak contoh, tapi ini contoh ke 1. terus sistem reading di python ini pake index yang dimana selalu mulai dari 0. ini pake range(start) aja
    print("angka", angka)


# Contoh 2, bikin perulangan dari range (ke-2) :

for angka in range(20, 31): #ini pake range(start, stop) yang dimana angkanya bakal stop sebelum nyampe angka 31.
    print("urutan", angka)


# Contoh 2, bikin perulangan dari range (ke-3) :

for angka in range(30, 41, 2): #nah ini baru pake range(start, stop, step) yang dimana angkanya bakal stop sebelum angka 41 dan bakal ngitung 2 angka dalam 1x perulangan.
    print("deret", angka)


# Contoh 3, bikin perulangan yang tersusun dari range :

for bintang in range(1, 6): #disini pake range(start, stop) supaya urutannya ga bablas jir
    print('*' * bintang) #terus tambahin operator (*) untuk meng-kalikan string '*' bintang persetiap deret dari angka 1 - 5 (kenapa 5 ? karna disitu ada stop yang dimana fungsinya untuk stoping angka sebelum angka tersebut)


# Contoh 4, bikin perulangan dari operator perbandingan (>, <, <=, >=, ==, !=)

for angka in range(5):
    if angka > 0:
        print(angka)

for angka in range(10, 16):
    if angka < 16:
        print(angka)

for angka in range(100, 106):
    if angka <= 106:
        print(angka)

for angka in range(1000, 1006):
    if angka >= 1000:
        print(angka)

for angka in range(194, 201):
    if angka == 200:
        print("ketemu", angka)

for angka in range(30, 33):
    if angka != 33:
        print("ketemu angka yang bukan urutan 33 :", angka)
print()


print("'While' Looping")
# 2. While

# While(while), ini teh bisa bikin perulangan terus menerus selama kondisi nya masih sesuai/True. Contohnya :
# Contoh 1, bikin perulangan terus menerus selama kondisi nya masih sesuai/True 
a = 1
while a <= 3: #selama variable a masih dibawah 5, maka perulangan akan terus jalan
    print("halo", a)
    a += 1 #ini sama aja kayak a = a + 1, jadi setiap perulangan variable a bakal nambah 1 terus sampe variable a nya lebih dari 5

#Pembatas
print("--")

# Contoh 2, bikin perulangan terus menerus selama kondisi nya masih sesuai/True + operator (+)
jumlah = 1
while jumlah <= 3:
    penjumlahan = jumlah + 1
    print(f"Penjumlahan {jumlah}+1 = {penjumlahan}")
    jumlah += 1

#Pembatas
print("--")

# Contoh 3, bikin perulangan terus menerus selama kondisi nya masih sesuai/True + operator (-)
kurang = 3
while kurang >= 1:
    pengurangan = kurang - 1 #ini angka yang bisa di ubah
    print(f"Pengurangan {kurang}-1 = {pengurangan}")
    kurang -= 1

#Pembatas
print("--")

# Contoh 4, bikin perulangan pake (*)
kali = 1
while kali <= 3:
    perkalian = kali * 2 #ini angka yang bisa di ubah
    print(f"Perkalian {kali}*2 = {perkalian}")
   
    kali += 1

#Pembatas
print("--")

# Contoh 5, bikin perulangan pake (/) ke-1 
bagi = 8
while bagi <= 10:
    pembagian = bagi / 2 #ini angka yang bisa di ubah
    print(f"Pembagian {bagi}/2 = {pembagian}")
    bagi += 1

#Pembatas
print("--")

# Contoh 5, bikin perulangan pake (//) ke-2
bagi = 8
while bagi <= 10:
    pembagian_bulat = bagi // 2 #ini angka yang bisa di ubah
    print(f"Pembagian Bulat {bagi}//2 = {pembagian_bulat}")
    bagi += 1

#Pembatas
print("--")

# Contoh 6, bikin perulangan pake (**)
pangkat = 1
while pangkat <= 3:
    perpangkatan = pangkat**2
    print(f"Perpangkatan {pangkat}**2 = {perpangkatan}")
    pangkat += 1

#Pembatas
print("--")

# Contoh 7, bikin perulangan pake (%)
sisa_bagi = 1
while sisa_bagi <= 3:
    sisa_pembagian = sisa_bagi % 2
    print(f"Sisa Bagi {sisa_bagi} % 2 = {sisa_pembagian}")
    sisa_bagi += 1