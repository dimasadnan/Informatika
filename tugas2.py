nama = "mulyono"
usia = 63
tinggi_badan = 175, 0
presiden = False
if presiden:
    print("he president")
else:
    print("he not president")
print(nama, usia, tinggi_badan, presiden)

namamu = input()
print(namamu)


def kalkulator(x, y, operasi="+"):
    if operasi == "+":
        return x + y
    elif operasi == "-":
        return x - y
    elif operasi == "*":
        return x * y
    elif operasi == "/":
        return x / y


hasil = kalkulator(20, 10, "*")
print(hasil)

umur = 13
pendidikan = "s1"
jeniskelamin = "laki-laki"
status = "belum menikah"

if (pendidikan == "s1" or pendidikan == "d3") and umur >= 21 and jeniskelamin == "laki-laki" and status == "belum menikah":
    print("boleh kerja")
else:
    print("nda boleh")

