#Percabangan + Operator
 
# Percabangan itu kayak suatu kondisi yang menghasilkan output True / False

# 1. if (kondisi ke-1), ini teh bikin simulasi kondisi pertama kalau boolean nya true maka kondisi ke-1 sukses dan ngga akan lanjut ke kondisi ke-2
is_beat_pertalite = True
if is_beat_pertalite:
    print("Beat pake pertalite makin irit") #Ini bakal langsung ke print kalau is_beat_pertalite adalah True

# 2. elif (kondisi ke-2), nah ini dipake kalau kamu pake string
beat = "pertalite"

if beat == "pertalite":
    print("cocok bangat jir")

elif beat == "pertamax":
    print("Beat pake pertamax kurang cocok")

# 3. else (kondisi selain ke-1, dan 2), ini dipake kalau ngga ada jawaban/value yang sesuai. Bisa pake string maupun boolean

is_yogi_kurus = True #ini kalau pengkondisian nya boolean
if is_yogi_kurus:
    print("yogi sekarang kurusan yaa")

else:
    print("yogi kok gendutan yaa")
 
# Pembatas - Pembatas - Pembatas

yogi = "kurus"

if yogi == "kurus":
    print("jir kamu gantenk banget")
else:
    print("jir kamu gendud banget")


# Operator itu ada 3 jenis, yaitu : 

# 1. Operator Aritmatika
#Penjumlahan
penjumlahan = 1+2

print(penjumlahan)

#Pengurangan
pengurangan = 20-1

print(pengurangan)

#Perkalian
perkalian = 904*15

print(perkalian)

#Pembagian
pembagian = 1420/6

print(pembagian)

#Pembagian bulat | jadi dibulatkan alias ngga ada angka desimal
pembagian_bulat = 1420//6

print(pembagian_bulat)

#Sisa bagi | jadi ini tuh angka sisa dari bilangan yang sudah di bagi
sisa_bagi = 10%3

print(sisa_bagi)

#Perpangkatan
pangkat = 21**2

print(pangkat)


# 2. Operator Perbandingan | kalau bilangan tersebut bener maka outputnya akan True, kalau salah maka False
#Sama dengan
sama_dengan = 5==5

print(sama_dengan)

#Tidak sama dengan | kalau bilangan tersebut bener maka outputnya akan True, kalau salah maka False
tidak_sama_dengan = 5!=3

print(tidak_sama_dengan)

#Lebih besar | kalau bilangan tersebut bener maka outputnya akan True, kalau salah maka False
lebih_besar = 3 > 1

print(lebih_besar)

#Lebih kecil | kalau bilangan tersebut bener maka outputnya akan True, kalau salah maka False
lebih_kecil = 1 < 3

print(lebih_kecil)

#Lebih dari sama dengan | kalau bilangan tersebut bener maka outputnya akan True, kalau salah maka False
lebih_dari_sama_dengan = 1 >= 0.5

print(lebih_dari_sama_dengan)

#Lebih kurang sama dengan | kalau bilangan tersebut bener maka outputnya akan True, kalau salah maka False
lebih_kurang_sama_dengan = 1 <= 1.5

print(lebih_kurang_sama_dengan)


# 3. Operator Logika | ini bisa digabung sama if, elif, else
# and | kalau (and) ini nilai variable harus sama, kalau ngga maka akan jadi false
is_yogigay = True
is_sultangay = True

if is_yogigay and is_sultangay:
    print("KALIAN MAKHLUK GAY")
else:
    print("Setidaknya ada yang ngga gay 1")

# or | kalau (or) ini nilai dari variable setidaknya ada yang True 1, kalau ngga ada yang True maka jadi false
is_nasrulstraight = True
is_gajistraight = False

if is_nasrulstraight or is_gajistraight:
    print("ada yang masih suka lubang")
else:
    print("sama sama suka batank")

# not | ini tuh buat ngebalikin nilai. contoh : True = False, False = True

is_aditsehat = False

if not is_aditsehat:
    print("alhamdulilah adit sehat")
else:
    print("gewees adit")