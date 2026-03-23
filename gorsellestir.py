import csv
import matplotlib.pyplot as plt
import os

def visualize_data():
    target_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(target_dir, "data.csv")
    img_path = os.path.join(target_dir, "veri_gorseli.png")
    
    study_hours = []
    scores = []
    
    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                study_hours.append(float(row["Ders_Calisma_Suresi"]))
                scores.append(int(row["Sinav_Notu"]))
    except FileNotFoundError:
        print(f"Hata: {csv_path} bulunamadi! Once veriyi olusturun.")
        return
        
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Grafik 1: Histogram (Çan Eğrisi / Normal Dağılım)
    axes[0].hist(scores, bins=20, color="skyblue", edgecolor="black", alpha=0.7)
    axes[0].set_title("Sinav Notu Dagilimi (Can Egrisi)")
    axes[0].set_xlabel("Sinav Notu")
    axes[0].set_ylabel("Ogrenci Sayisi")
    
    # Grafik 2: Scatter Plot (Ders Çalışma vs Not)
    axes[1].scatter(study_hours, scores, color="coral", alpha=0.6, edgecolors="None")
    axes[1].set_title("Ders Calisma Suresi vs Sinav Notu")
    axes[1].set_xlabel("Ders Calisma Suresi (Saat)")
    axes[1].set_ylabel("Sinav Notu")
    
    plt.tight_layout()
    plt.savefig(img_path, dpi=300)
    print(f"Grafikler basariyla '{img_path}' isimli gorsele kaydedildi.")

if __name__ == "__main__":
    visualize_data()
