def kalkulator(x, y, operasi="+"):
    if operasi == "+":
        return x + y
    elif operasi == "-":
        return x - y
    elif operasi == "*":
        return x * y
    elif operasi == "/":
        return x / y


hasil = kalkulator(20, 2, "/")
print(hasil)

def cekumur(umur):
    if umur < 18:
        print("masih bocah")
    else:
        print("wes gerang masseh")


Hasil = cekumur(20)
print(Hasil)

a = 17
b = a
c = 19

print("ini adalah hasil penjumlahan dari  b ditambah dengan c = ", b + c)

umur = 10
pendidikan = "s1"
jeniskelamin = "laki-laki"
status = "belum menikah"

if (pendidikan == "s1" or pendidikan == "d3") and umur >= 21 and jeniskelamin == "laki-laki" and status == "belum menikah":
    print("boleh kerja")
else:
    print("nda boleh")

x = 19

if x > 5:
    print("x is more than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")


