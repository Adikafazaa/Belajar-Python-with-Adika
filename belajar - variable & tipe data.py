#Variable + Tipe Data

#Variable itu sebuah simbol, contohnya kayak X, Y, Z. Mereka bisa kita masukin sebuah value, contohnya : 

# 1. String(str), ini teh variable untuk huruf jadi pake tanda kutip ""
mobil = "Lamborghini"
nama = "adika"
lokasi = "kab.bandung"

# 2. Integer(int), nah kalau ini variable untuk bilangan bulat. Ga perlu pake tanda kutip juga gpp
umur = 18
tinggi = 164
kelas = 12

# 3. Float(float), kalau ini variable untuk bilangan desimal. Sama kayak int ga perlu pake tanda kutip juga kok
suhu_tubuh = 28.1
phi = 3.14

# 4. Boolean, ini tuh untuk melabel true/false dari suatu variable
is_charger_plugin = False #karna lagi ngga pake cas an -> bisa jadi true kalau pake 'if not'
is_computer_turned_on = True #karna sekarang kita lagi pake buat ngoding


#Output dari codingan tersebut : 
print(mobil)
print(nama)
print(lokasi)
print(umur)
print(tinggi)
print(kelas)
print(suhu_tubuh)
print(phi)
if is_charger_plugin: # kalau kita pake not di depan 'if' ntar dia bisa ngeprint
    print("laptop udah nyolog nih pler")
if is_computer_turned_on:
    print("komputer masih nyala karna lagi dipake ngoding")