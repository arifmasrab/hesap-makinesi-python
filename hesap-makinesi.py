# variable
sayi_1 = int(input("bir sayı girin: "))
sayi_2 = int(input("ikinci sayıyı girin: "))

print("aşşağa yapılacak işlemin ikonunu girin mesela: x = çarpı, : = bölme, + = artı, - = çıkarma")

islem = input("ikon: ")

# işlemler
if islem == "x":
    print(sayi_1, "x", sayi_2, "=", sayi_1 * sayi_2)
elif islem == ":":
    print(sayi_1, ":", sayi_2, "=", sayi_1/ sayi_2)
elif islem == "+":
    print(sayi_1, "+", sayi_2, "=", sayi_1 + sayi_2)
elif islem == "-":
    print(sayi_1, "-", sayi_2, "=", sayi_1 - sayi_2)
else:
    print("!!! bu işlem yapılamaz !!!")
