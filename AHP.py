# AHP pemilihan lokasi gudang beras
# hasil: Bobot Kriteria, CI/CR, Bobot Alternatif,
# Skor Akhir, Ranking, dan Visualisasi Grafik

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# perhitungan AHP
def ahp_priority_from_pairwise(A):
    """
    Menghitung bobot prioritas AHP menggunakan metode normalisasi kolom.
    Menghasilkan:
      - priority : bobot (vektor eigen aproksimasi)
      - A_norm   : matriks ternormalisasi
      - Aw, lambda_max, CI, RI, CR untuk mengecek konsistensi
    """
    n = A.shape[0]
    col_sum = A.sum(axis=0)        # jumlah per kolom
    A_norm = A / col_sum           
    w = A_norm.mean(axis=1)        # bobot = rata-rata per baris
    Aw = A.dot(w)                  
    ratios = Aw / w
    lambda_max = ratios.mean()
    CI = (lambda_max - n) / (n - 1)

    # index random konsistensinya
    RI_dict = {1:0.00,2:0.00,3:0.58,4:0.90,5:1.12,6:1.24,7:1.32,8:1.41,9:1.45,10:1.49}
    RI = RI_dict.get(n, None)
    CR = CI / RI if RI and RI != 0 else np.nan

    return {
        'priority': w,
        'A_norm': A_norm,
        'Aw': Aw,
        'lambda_max': lambda_max,
        'CI': CI,
        'RI': RI,
        'CR': CR,
        'col_sum': col_sum
    }

# matriks perbandingan
# urutan kriteria: Transportasi, Tenaga Kerja, Biaya Lahan, Kedekatan Produksi
# urutan alternatif: Lamongan, Jember, Kediri, Madiun

pairwise_criteria = np.array([
    [1,   3,   5,   7],
    [1/3, 1,   3,   5],
    [1/5, 1/3, 1,   3],
    [1/7, 1/5, 1/3, 1]
], dtype=float)

# matriks alternatif
pairwise_alt_T  = pairwise_criteria.copy() # transprotasi
pairwise_alt_TK = pairwise_criteria.copy() # tenaga kerja
pairwise_alt_BL = pairwise_criteria.copy() # biaya lahan
pairwise_alt_KP = pairwise_criteria.copy() # kedekatan prodduksi

# perhitungan bobot kriteria
crit_res = ahp_priority_from_pairwise(pairwise_criteria)
criteria_weights = crit_res['priority']

# perhitungan bobot alternatif per kriteria ---
alt_res_T  = ahp_priority_from_pairwise(pairwise_alt_T)
alt_res_TK = ahp_priority_from_pairwise(pairwise_alt_TK)
alt_res_BL = ahp_priority_from_pairwise(pairwise_alt_BL)
alt_res_KP = ahp_priority_from_pairwise(pairwise_alt_KP)

locations = ['Lamongan', 'Jember', 'Kediri', 'Madiun']
alt_weights_df = pd.DataFrame({
    'Lokasi': locations,
    'Transportasi': alt_res_T['priority'],
    'Tenaga Kerja': alt_res_TK['priority'],
    'Biaya Lahan': alt_res_BL['priority'],
    'Kedekatan Produksi': alt_res_KP['priority']
})

# perhitungan skor akhir dan ranking alternatif
final_scores = (
    alt_weights_df['Transportasi'] * criteria_weights[0] +
    alt_weights_df['Tenaga Kerja'] * criteria_weights[1] +
    alt_weights_df['Biaya Lahan'] * criteria_weights[2] +
    alt_weights_df['Kedekatan Produksi'] * criteria_weights[3]
)

alt_weights_df['Skor Akhir'] = final_scores
alt_weights_df['Ranking'] = alt_weights_df['Skor Akhir'].rank(ascending=False, method='min').astype(int)
alt_weights_df = alt_weights_df.sort_values(by='Skor Akhir', ascending=False).reset_index(drop=True)

# hasil
pd.set_option('display.float_format', '{:,.6f}'.format)

print("\n=== BOBOT KRITERIA ===\n")
crit_w_df = pd.DataFrame({
    'Kriteria':['Transportasi','Tenaga Kerja','Biaya Lahan','Kedekatan Produksi'],
    'Bobot': criteria_weights
})
print(crit_w_df.to_string(index=False))

print("\n=== UJI KONSISTENSI KRITERIA ===\n")
print(f"lambda_max = {crit_res['lambda_max']:.6f}")
print(f"CI = {crit_res['CI']:.6f}")
print(f"RI (n=4) = {crit_res['RI']:.6f}")
print(f"CR = {crit_res['CR']:.6f}   (CR < 0.1 = Konsisten)")

print("\n=== PRIORITAS ALTERNATIF PER KRITERIA ===\n")
print(alt_weights_df[['Lokasi','Transportasi','Tenaga Kerja','Biaya Lahan','Kedekatan Produksi']].to_string(index=False))

print("\n=== SKOR AKHIR & RANKING ===\n")
print(alt_weights_df[['Lokasi','Skor Akhir','Ranking']].to_string(index=False))

# visualisasi
plt.rcParams.update({'figure.autolayout': True})

# grafik bobot kriteria
plt.figure(figsize=(8,5))
plt.bar(crit_w_df['Kriteria'], crit_w_df['Bobot'])
plt.ylabel('Nilai Bobot')
plt.title('Bobot Kriteria AHP')
plt.show()

# grafik ranking alternatif
plt.figure(figsize=(8,5))
plt.barh(alt_weights_df['Lokasi'], alt_weights_df['Skor Akhir'], color='green')
plt.xlabel('Skor Akhir')
plt.title('Ranking Lokasi Gudang Beras')
plt.gca().invert_yaxis()
plt.show()