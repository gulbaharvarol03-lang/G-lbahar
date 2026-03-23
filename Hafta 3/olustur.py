import csv
import random
import os

def generate_csv():
    # Dosya yolu: bu dosyanin oldugu dizin (Hafta 3)
    target_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(target_dir, "data.csv")
    
    header = ["ID", "Ders_Calisma_Suresi", "Sinav_Notu"]
    rows = []
    
    for i in range(1, 501):
        student_id = i
        
        # 0.0 ile 6.0 saat arasında 1 ondalıklı rastgele sayı (örn: 4.8)
        study_hours = round(random.uniform(0, 6), 1) 
        
        # Sınav notu (10 ile 100 arasında, normal dağılımlı)
        score = random.gauss(55, 15)
        score = max(10, min(100, score))
        score = round(score)
        
        rows.append([student_id, study_hours, score])
        
    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)
        
    print(f"{file_path} basariyla saat tabanli (eski haline) guncellendi.")

if __name__ == "__main__":
    generate_csv()
