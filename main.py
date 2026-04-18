def modul_juftlar(royxat1, royxat2):
    juftlar = list(zip(royxat1, royxat2))
    natijalar = [a % b for a, b in juftlar]
    return natijalar

royxat1 = [10, 20, 30]
royxat2 = [2, 4, 6]
print(modul_juftlar(royxat1, royxat2))
