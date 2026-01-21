# -*- coding: utf-8 -*-
"""# Project MSS"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --- Data ---
angkatan = ['2023', '2024', '2025']
jumlah_mahasiswa = [52, 53, 76]
jumlah_responden = [24, 32, 44]

proporsi = [r/m*100 for r, m in zip(jumlah_responden, jumlah_mahasiswa)]

# --- Style aesthetic ---
sns.set(style="whitegrid", palette="muted")

plt.figure(figsize=(10, 6))

# Bar chart
x = np.arange(len(angkatan))
bar_width = 0.35

plt.bar(x - bar_width/2, jumlah_mahasiswa, width=bar_width, label='Jumlah Mahasiswa', color='#8ecae6')
plt.bar(x + bar_width/2, jumlah_responden, width=bar_width, label='Jumlah Responden', color='#219ebc')

# Tambahkan persentase di atas bar responden
for i, p in enumerate(proporsi):
    plt.text(i + bar_width/2, jumlah_responden[i] + 1,
             f"{p:.1f}%", ha='center', fontsize=10, color='black')

plt.xticks(x, angkatan, fontsize=11)
plt.title("Grafik Jumlah Responden dari Prodi Statistika UGM Angkatan 2023-2025",
          fontsize=14, weight='bold')
plt.ylabel("Jumlah", fontsize=12)
plt.legend()

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# Data
angkatan = ['2023', '2024', '2025']
jumlah_responden = [24, 32, 44]

colors = ['#ffb703', '#fb8500', '#219ebc']

plt.figure(figsize=(7, 7))
plt.pie(jumlah_responden,
        labels=angkatan,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        wedgeprops={'edgecolor': 'white', 'linewidth': 1},
        textprops={'fontsize': 12})

plt.title("Proporsi Jumlah Responden", fontsize=14, weight='bold')
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------------------------------
# 1. MASUKKAN DATA MANUAL KE DALAM DATAFRAME
# -------------------------------------------------------

data_2025 = [
    3.727272727, 3.977272727, 3.931818182,
    3.954545455, 3.954545455, 3.522727273,
    3.909090909, 3.590909091, 3.704545455,
    2.886363636, 3.5, 3.272727273,
    4.181818182, 4.5, 4.295454545
]

data_2024 = [
    3.4375, 3.75, 3.6875,
    3.65625, 4.1875, 3.78125,
    3.84375, 3.84375, 3.625,
    2.875, 3.21875, 3,
    4.125, 4.53125, 4.1875
]

data_2023 = [
    3.916666667, 4.041666667, 3.75,
    4.25, 4.416666667, 4.291666667,
    4.416666667, 4.5, 4,
    3.125, 3.75, 3.583333333,
    4.375, 4.75, 4.5
]

# Nama item pertanyaan
items = [
    "1_1","1_2","1_3","2_1","2_2","2_3","3_1","3_2","3_3",
    "4_1","4_2","4_3","5_1","5_2","5_3"
]

# Buat DataFrame
df = pd.DataFrame({
    "Item": items,
    "2023": data_2023,
    "2024": data_2024,
    "2025": data_2025
})

# Melt untuk format long
df_long = df.melt(id_vars="Item", var_name="Angkatan", value_name="Rata-rata")

# -------------------------------------------------------
# 2. VISUALISASI BAR CHART MULTI-ANGKATAN
# -------------------------------------------------------

sns.set(style="whitegrid")
palette = ["cyan", "#8ecae6", "#219ebc"]  # aesthetic colors

plt.figure(figsize=(16, 8))

sns.barplot(
    data=df_long,
    x="Item",
    y="Rata-rata",
    hue="Angkatan",
    palette=palette
)

plt.title("Perbandingan Rata-rata Persepsi Tiap Angkatan terhadap Kurikulum Statistika",
          fontsize=16, weight='bold')
plt.xlabel("Butir Pertanyaan", fontsize=12)
plt.ylabel("Rata-rata Jawaban Likert", fontsize=12)

plt.xticks(rotation=45)
plt.ylim(0, 5)
plt.legend(title="Angkatan")

plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
items = [
    "1_1","1_2","1_3","2_1","2_2","2_3","3_1","3_2","3_3",
    "4_1","4_2","4_3","5_1","5_2","5_3"
]

data_2025 = [3.727272727,3.977272727,3.931818182,3.954545455,3.954545455,3.522727273,3.909090909,3.590909091,3.704545455,2.886363636,3.5,3.272727273,4.181818182,4.5,4.295454545]
data_2024 = [3.4375,3.75,3.6875,3.65625,4.1875,3.78125,3.84375,3.84375,3.625,2.875,3.21875,3,4.125,4.53125,4.1875]
data_2023 = [3.916666667,4.041666667,3.75,4.25,4.416666667,4.291666667,4.416666667,4.5,4,3.125,3.75,3.583333333,4.375,4.75,4.5]

df = pd.DataFrame({
    "Item": items,
    "2023": data_2023,
    "2024": data_2024,
    "2025": data_2025
})

sns.set(style="whitegrid")

plt.figure(figsize=(16,7))
pastel = sns.color_palette("pastel")

plt.plot(df["Item"], df["2023"], marker="o", color=pastel[0], linewidth=2.5, label="2023")
plt.plot(df["Item"], df["2024"], marker="o", color=pastel[1], linewidth=2.5, label="2024")
plt.plot(df["Item"], df["2025"], marker="o", color=pastel[2], linewidth=2.5, label="2025")

plt.title("Perbandingan Tren Persepsi per Item – Angkatan 2023–2025", fontsize=16, weight='bold')
plt.ylim(0, 5)
plt.xticks(rotation=45)
plt.ylabel("Rata-rata Likert")
plt.xlabel("Butir Pertanyaan")
plt.legend()
plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Kelompok variabel (3 item per variabel)
V1_2025 = np.mean(data_2025[0:3])
V2_2025 = np.mean(data_2025[3:6])
V3_2025 = np.mean(data_2025[6:9])
V4_2025 = np.mean(data_2025[9:12])
V5_2025 = np.mean(data_2025[12:15])

V1_2024 = np.mean(data_2024[0:3])
V2_2024 = np.mean(data_2024[3:6])
V3_2024 = np.mean(data_2024[6:9])
V4_2024 = np.mean(data_2024[9:12])
V5_2024 = np.mean(data_2024[12:15])

V1_2023 = np.mean(data_2023[0:3])
V2_2023 = np.mean(data_2023[3:6])
V3_2023 = np.mean(data_2023[6:9])
V4_2023 = np.mean(data_2023[9:12])
V5_2023 = np.mean(data_2023[12:15])

labels = ["V1","V2","V3","V4","V5"]

vals2023 = [V1_2023, V2_2023, V3_2023, V4_2023, V5_2023]
vals2024 = [V1_2024, V2_2024, V3_2024, V4_2024, V5_2024]
vals2025 = [V1_2025, V2_2025, V3_2025, V4_2025, V5_2025]

angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
vals2023 += vals2023[:1]
vals2024 += vals2024[:1]
vals2025 += vals2025[:1]
angles += angles[:1]

plt.figure(figsize=(8,8))
ax = plt.subplot(111, polar=True)

pastel = sns.color_palette("pastel")

ax.plot(angles, vals2023, color=pastel[0], linewidth=2.5, label="2023")
ax.fill(angles, vals2023, color=pastel[0], alpha=0.25)

ax.plot(angles, vals2024, color=pastel[1], linewidth=2.5, label="2024")
ax.fill(angles, vals2024, color=pastel[1], alpha=0.25)

ax.plot(angles, vals2025, color=pastel[2], linewidth=2.5, label="2025")
ax.fill(angles, vals2025, color=pastel[2], alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
ax.set_yticklabels([])

plt.title("Radar Chart Persepsi per Variabel – Angkatan 2023–2025", fontsize=16, weight='bold')
plt.legend(loc="upper right", bbox_to_anchor=(1.1, 0.8))
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_heat = df.set_index("Item")

plt.figure(figsize=(10,8))
sns.heatmap(df_heat, annot=True, cmap="YlGnBu", linewidths=.5)

plt.title("Heatmap Rata-rata per Item – Angkatan 2023–2025",
          fontsize=16, weight='bold')
plt.xlabel("Angkatan")
plt.ylabel("Butir Pertanyaan")
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# --- pastikan df kamu seperti ini ---
# df = pd.DataFrame({
#     "Item": items,
#     "2023": data_2023,
#     "2024": data_2024,
#     "2025": data_2025
# })

sns.set(style="whitegrid")
pastel = sns.color_palette("pastel")

plt.figure(figsize=(14,8))

# setiap angkatan kita plotting titiknya
plt.scatter(df["2023"], df["Item"], s=120, color=pastel[0], label="2023")
plt.scatter(df["2024"], df["Item"], s=120, color=pastel[1], label="2024")
plt.scatter(df["2025"], df["Item"], s=120, color=pastel[2], label="2025")

plt.title("Cleveland Dot Plot — Perbandingan Rata-rata per Item", fontsize=16, weight='bold')
plt.xlabel("Rata-rata Likert")
plt.ylabel("Item Pertanyaan")
plt.xlim(0, 5)
plt.legend()

plt.tight_layout()
plt.show()