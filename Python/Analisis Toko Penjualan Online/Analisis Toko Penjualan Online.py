# ANALISIS DATA PENJUALAN TOKO ONLINE
# TUJUAN : UNTUK MENGANALISIS DATA PENJUALAN BULANAN MENGGUNAKAN LIBRARY PYTHON
# TOOLS : NUMPY, MATPLOTLIB

#IMPORT LIBRARY
import numpy as np

#BUAT ARRAY
bulan = np.arange(1,13)
penjualan = np.random.randint(151,181,12)
print(f'Penjualan adalah {penjualan}')
biaya_operasional = np.random.randint(80,351,12)
print(f"Biaya Operasional adalah {biaya_operasional}")

#LABA PER BULAN
laba_per_bulan = penjualan - biaya_operasional
print(f'Laba per bulan : {laba_per_bulan}')

#RATA-RATA PENJUALAN
rata_rata = np.mean(penjualan)
print(f'Rata-rata penjualan adalah {round(rata_rata,2)}')

#TOTAL PENJUALAN
total = np.sum(penjualan)
print(f'Total penjualan adalah {round(total,2)}')

#BULAN DENGAN PENJUALAN TERTINGGI DAN TERENDAH
max = np.max(penjualan)
min = np.min(penjualan)
idx_max = np.argmax(penjualan)
idx_min = np.argmin(penjualan)
bulan_terbaik = bulan[idx_max]
bulan_terburuk = bulan[idx_min]

print(f'Bulan dengan perjualan tertinggi berada di bulan {bulan_terbaik} dengan penjualan sebesar {max}')
print(f'Bulan dengan penjualan terendah berada di bulan {bulan_terburuk} dengan penjualan sebesar {min}')

#VISUALISASI
import matplotlib.pyplot as plt

#FIGURE 1
plt.figure(figsize=(10,5))
plt.plot(bulan, penjualan, marker='o', label = 'Penjualan', color = 'b')
plt.plot(bulan, biaya_operasional, marker = 'o',label = 'Biaya Operasional', color = 'r')

plt.title('Total Penjualan dan Biaya Operasional', fontsize = 14)
plt.xlabel('Bulan', fontsize = 11)
plt.ylabel('Nilai', fontsize = 11)
plt.xticks(bulan)
plt.legend()
plt.grid(alpha = 0.3)
plt.tight_layout()
plt.show()

#FIGURE 2
warna = ['g' if x>0 else 'r' for x in laba_per_bulan]
plt.figure(figsize=(10,5))
plt.bar(bulan, laba_per_bulan)
plt.title('Laba Setiap Bulan', fontsize = 14)
plt.xlabel('Bulan', fontsize = 12)
plt.ylabel('Nilai Laba', fontsize = 12)
plt.xticks(bulan)
plt.axhline(y=0, color='black', linestyle='--')
plt.grid(axis = 'y',alpha = 0.3)
plt.tight_layout()
plt.show()