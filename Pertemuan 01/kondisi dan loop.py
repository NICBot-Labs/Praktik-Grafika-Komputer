x = int(input("Masukan nilai X : "))

if x > 0:
    print("titik di kanan layar")
elif x < 0:
    print("titik di kiri layar")
else:
    print("titik di tengah")

perulangan  = int(input("Masukan jumlah perulangan : "))
i = 0
print(f"Sisa perulangan {perulangan - i}, titik ke-P{i}")
for i in range (1, perulangan):
    print(f"Sisa perulangan {perulangan - i}, titik ke-P{i}")