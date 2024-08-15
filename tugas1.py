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
