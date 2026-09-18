# hitung_panen.py

# Data hasil panen (dalam kg) dan harga per kg (Rp)
komoditas = {
    "Padi": {"bobot": 1200, "harga": 6500},
    "Jagung": {"bobot": 850, "harga": 5000},
    "Kedelai": {"bobot": 400, "harga": 9500},
}

total_pendapatan = 0
total_bobot = 0

print("=== REKAP HASIL PANEN ===")
for nama, data in komoditas.items():
  subtotal = data["bobot"] * data["harga"]
  total_bobot += data["bobot"]
  total_pendapatan += subtotal
  print(
      f"- {nama:<8}: {data['bobot']:>5} kg @ Rp{data['harga']:,} = Rp"
      f" {subtotal:,}"
  )

print("-" * 35)
print(f"Total Bobot Panen : {total_bobot:,} kg")
print(f"Total Nilai Panen : Rp {total_pendapatan:,}")