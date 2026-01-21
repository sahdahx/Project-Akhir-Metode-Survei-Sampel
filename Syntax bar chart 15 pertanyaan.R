library(readxl)
library(dplyr)
library(tidyr)
library(ggplot2)

# ============================
# 1. Import data
# ============================
data <- read_excel("C:/Users/Asus Vivobook/Downloads/Dataset 2023-2025.xlsx")

# Hapus baris terakhir (mean)
data <- data[-nrow(data), ]

# ============================
# 2. Ubah ke format long
# Kolom pertanyaan berbentuk: 1_1, 1_2, 2_1, 2_2, dst
# ============================
data_long <- data %>% 
  pivot_longer(cols = matches("^[0-9]+_[0-9]+$"),
               names_to = "Pertanyaan",
               values_to = "Likert")

# ============================
# 3. Rekap jumlah & persentase
# ============================
rekap <- data_long %>% 
  group_by(Pertanyaan, Angkatan, Likert) %>% 
  summarise(Jumlah = n(), .groups = "drop") %>% 
  group_by(Pertanyaan, Likert) %>% 
  mutate(Persen = round(Jumlah / sum(Jumlah) * 100, 1))

# ============================
# 4. Visualisasi per butir
# ============================
warna_angkatan <- c(
  "2023" = "#ffb703",  # biru
  "2024" = "#fb8500",  # hijau
  "2025" = "#219ebc"   # oranye
)
for (i in unique(rekap$Pertanyaan)) {
  
  p <- ggplot(filter(rekap, Pertanyaan == i),
              aes(x = factor(Likert),
                  y = Jumlah,
                  fill = factor(Angkatan))) +
    
    geom_bar(stat = "identity",
             position = position_dodge(width = 0.8)) +
    
    geom_text(aes(label = paste0(Persen, "%")),
              position = position_dodge(width = 0.8),
              vjust = -0.3,
              size = 2.3) +
    scale_fill_manual(values = warna_angkatan) +
    
    labs(title = paste("Distribusi Jawaban Pertanyaan", i),
         x = "Skala Likert",
         y = "Jumlah Responden",
         fill = "Angkatan") +
    
    theme_minimal() +
    theme(
      plot.title = element_text(hjust = 0.5, face = "bold"),
      legend.position = "top"
    )
  
  print(p)
}
