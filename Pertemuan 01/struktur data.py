# A. list berisi tiga pasangan titik: [(0,0), (50,50), (100,0)]. Tampilkan semua titik
titik = [(0,0), (50, 50), (100, 0)]
for i in titik:
    print(i)

# B. satu titik dalam tuple bernama pusat = (0, 0) dan tampilkan nilainya
pusat = (0,1)
print(f"\nTitik pusat ({pusat[0]}, {pusat[1]})" )

# C. dictionary berisi atribut objek: {"x": 10, "y": 20, "warna": "biru"} dan tampilkan isi dengan format teks: Titik (10,20) berwarna biru.
objek ={
    "x":int(10),
    "y":int(20),
    "warna":"biru"
}
print(f"\nTitik ({objek['x']}, {objek['y']}) berwarna {objek['warna']}" )
