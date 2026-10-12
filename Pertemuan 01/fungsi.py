# Tugas 1
import math
def hitung_jarak(x1, y1, x2, y2):
    jarak = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return jarak

x1 = int(input("Masukan x1 :"))
y1 = int(input("Masukan y1 :"))
x2 = int(input("Masukan x2 :"))
y2 = int(input("Masukan y2 :"))

hasil = hitung_jarak(x1,y1,x2, y2)
print(f"hasil antara dia titik {hasil}")