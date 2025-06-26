import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Lire le fichier CSV en sécurisant les types
try:
    df = pd.read_csv('euromillions_202002.csv', delimiter=';')
except FileNotFoundError:
    print("Fichier introuvable. Vérifiez le nom et le chemin du fichier.")
    exit()

# Conversion de la colonne date
df['date_de_tirage'] = pd.to_datetime(df['date_de_tirage'], format='%d/%m/%Y', errors='coerce')
df.dropna(subset=['date_de_tirage'], inplace=True)

# Vérifier que les colonnes nécessaires existent
required_columns = ['boule_1', 'boule_2', 'boule_3', 'boule_4', 'boule_5', 'etoile_1', 'etoile_2']
for col in required_columns:
    if col not in df.columns:
        print(f"Colonne manquante : {col}")
        exit()

# Initialiser les compteurs
boules_counts = {i: 0 for i in range(1, 51)}
etoiles_counts = {i: 0 for i in range(1, 13)}

# Pondération selon la récence (optionnel)
today = datetime.today()
use_weighting = True  # Mettre False pour désactiver

# Parcourir les lignes
for _, row in df.iterrows():
    poids = 1
    if use_weighting:
        jours_depuis = (today - row['date_de_tirage']).days
        poids = 1 / (jours_depuis + 1)

    # Comptage pondéré des boules
    try:
        for col in ['boule_1', 'boule_2', 'boule_3', 'boule_4', 'boule_5']:
            boules_counts[int(row[col])] += poids
        for col in ['etoile_1', 'etoile_2']:
            etoiles_counts[int(row[col])] += poids
    except Exception as e:
        print(f"Erreur lors du traitement d'une ligne : {e}")

# Calcul des ratios (en pourcentage)
total_tirages = len(df)
boules_ratios = {k: v / total_tirages * 100 for k, v in boules_counts.items()}
etoiles_ratios = {k: v / total_tirages * 100 for k, v in etoiles_counts.items()}

# DataFrames pour tri et affichage
boules_df = pd.DataFrame(list(boules_ratios.items()), columns=["Boule", "Ratio (%)"])
etoiles_df = pd.DataFrame(list(etoiles_ratios.items()), columns=["Étoile", "Ratio (%)"])

# Affichage des 10 boules / 5 étoiles les plus fréquentes
print("Top 10 Boules les plus fréquentes :")
print(boules_df.sort_values(by="Ratio (%)", ascending=False).head(10))

print("\nTop 5 Étoiles les plus fréquentes :")
print(etoiles_df.sort_values(by="Ratio (%)", ascending=False).head(5))

# Visualisation
boules_df.sort_values("Ratio (%)", ascending=False).head(10).plot(
    kind="bar", x="Boule", y="Ratio (%)", title="Top 10 Boules les plus fréquentes", legend=False
)
plt.tight_layout()
plt.show()

etoiles_df.sort_values("Ratio (%)", ascending=False).head(5).plot(
    kind="bar", x="Étoile", y="Ratio (%)", title="Top 5 Étoiles les plus fréquentes", legend=False, color='orange'
)
plt.tight_layout()
plt.show()

# Sauvegarde CSV
boules_df.sort_values(by="Ratio (%)", ascending=False).to_csv("ratios_boules.csv", index=False)
etoiles_df.sort_values(by="Ratio (%)", ascending=False).to_csv("ratios_etoiles.csv", index=False)

# Combinaison la plus probable
top_5_boules = boules_df.sort_values(by="Ratio (%)", ascending=False).head(5)["Boule"].tolist()
top_2_etoiles = etoiles_df.sort_values(by="Ratio (%)", ascending=False).head(2)["Étoile"].tolist()

# Prochaine date de tirage
latest_draw_date = df['date_de_tirage'].max()
existing_draw_dates = set(df['date_de_tirage'])

def date_previsionelle(current_date, existing_dates):
    next_date = current_date + timedelta(days=1)
    while next_date in existing_dates or next_date.weekday() not in [1, 4]:  # Mardi ou Vendredi
        next_date += timedelta(days=1)
    return next_date

next_draw = date_previsionelle(latest_draw_date, existing_draw_dates)

# Résumé
print("\n=== Résumé ===")
print(f"Combinaison la plus probable : Boules = {top_5_boules}, Étoiles = {top_2_etoiles}")
print(f"Prochaine date de tirage estimée : {next_draw.strftime('%d/%m/%Y')}")
