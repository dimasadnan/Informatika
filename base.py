  def cekumur(umur):
       if umur < 18:
            print("anak-anak")
        elif umur > 18:
            print("dewasa")


a = 10
b = a
c = 78
print(b)

print("ini adalah hasil penjumlahan dari  b ditambah dengan c = ", b + c)

data_integer = 18
print(" data : ", data_integer)
print("-berjenis : ", type(data_integer))

data_int = 18
print("data = ", data_int, "type = ", type(data_int))
data_float = float(data_int)
print("data = ", data_float, "type = ", type(data_float))

biner = bool(int(input("masukan nilai boolean")))
print("Data =", biner, "type =", type(biner))

w = 290
z = 82
wz = w % z
wzd = w // z
print("w", "%", "z", "=", wz)
print(w, "//", z, "=", wzd)

umur = 10
pendidikan = "s1"
jeniskelamin = "laki-laki"
status = "belum menikah"

if (pendidikan == "s1" or pendidikan == "d3") and umur >= 21 and jeniskelamin == "laki-laki" and status == "belum menikah":
    print("boleh kerja")
else:
    print("nda boleh")


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


def dollars_to_float(d):
    # Remove non-numeric characters and convert to float
    cleaned_str = ''.join(char for char in d if char.isdigit() or char == '.')

    # Convert the cleaned string to a float
    try:
        result = float(cleaned_str)
    except ValueError:
        result = 0.0  # Set a default value or handle the error as needed

    return result


# Example usage
dollars_str = input("Enter the dollar amount: ")
dollars_float = dollars_to_float(dollars_str)
print(f"Converted to float: ${dollars_float:.2f}")

dollar_string = "$50.00"
float_value = float(dollar_string.replace('$', ''))

print(float_value)


def dollars_to_float(d):
    # TODO: Implementasi dollars_to_floatl
    dollars = str(float())
    float_value = float(dollars.replace("$", ""))


def percent_to_float(p):
    # TODO: Implementasi percent_to_float
    percent = str(float())
    float_value = float(percent.replace("%", ""))


5/9(f-32)

fahrenheit = float(input("masukan suhu nya brooo"))
celcius = (5/9)*(fahrenheit-32)
kelvin = celcius + 273
print(kelvin)

# 9/5 c+32
kelvin = float(input("masukan atthiya"))
celcius = kelvin - 273
fahrenheit = (9/5)*celcius+32
print(fahrenheit)


suruh membuat true semua angka 0-5, 8-11
i
isbetone = float(
    input("masukan angka yang bernilai lebih dari 0 dan kurang dari 5 atau lebih dari 8 dan kurang dari 11:"))
isbettwo = isbetone > 0
print("lebih dari 0:", isbettwo)
isbetthree = isbetone < 5
print("kurang dari 5:", isbetthree)
isbetfour = isbetone > 8
print("kurang dari 8:", isbetfour)
isbetfive = isbetone < 11
print("kurang dari 11:", isbetfive)

print("bilangan yang dimasukkan:",
      isbettwo and isbetthree or isbetfour and isbetfive)

isbetone = float(
    input("jika ingin true maka masukan angka yang kurang dari 0 atau lebih dari lima dan kurang dari 8 atau lebih dari 11:"))
isbettwo = isbetone < 0
print("kurang dari 0:", isbettwo)
isbetthree = isbetone > 5
print("lebih dari 5:", isbetthree)
isbetfour = isbetone < 8
print("kurang dari 8:", isbetfour)
isbetfive = isbetone > 11
print("lebih dari 11:", isbetfive)

print("bilangan yang dimasukkan:",
      isbettwo or isbetthree and isbetfour or isbetfive)

udah pernah tapi nyoba masih inget apa gak yaa").replace(": (", "")
indoor.py
masukan = input("inpo ne mazzeh")
p = masukan.lower()
print(p)

playback speed.py
inp = input("wogweehh")
pay = inp.replace(" ", "...")
print(pay)

faces.py
waj = input()
wajh = waj.replace(":)", "\U0001F600").replace(":(", "\U0001F641")
print(wajh)

einstein.py
mau = int(input("massa"))
E = mau * 300000000 ** 2
print("E:", E)

tip.py


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(
        input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    (d) = (d).replace("$", "")
    return float(d)


def percent_to_float(p):
    # TODO
    (p) = (p).replace("%", "")
    ret//urn float(p) / 100


print(main())
x = int(input("x"))
op = input("operasi")
y = int(input("y"))


def kalkulator(x, y, operasi="+"):
    if operasi == "+":
        return x + y
    elif operasi == "-":
        return x - y
    elif operasi == "*":
        return x * y
    elif operasi == "/":
        return x / y


print(kalkulator)
