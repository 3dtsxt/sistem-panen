$ mkdir sistem-panen
$ cd sistem-panen
$ git init
Initialized empty Git repository in /path/to/sistem-panen/.git/

$ echo 'def hitung_total(berat, harga_per_kg):
    return berat * harga_per_kg

# Catatan panen sawi hijau
print(f"Total: Rp{hitung_total(50, 15000)}")' > panen.py

$ git add panen.py
$ git commit -m "Inisialisasi program pencatatan panen sawi hijau"
[main (root-commit) 7a8b9c0] Inisialisasi program pencatatan panen sawi hijau
 1 file changed, 5 insertions(+)
 create mode 100644 panen.py
