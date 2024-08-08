import pandas as pd
from datetime import datetime, timedelta

# Lire le CSV + inclure le delimiter
df = pd.read_csv('euromillions_202003.csv', delimiter=';')

# Conversion de la colonne date de tirage format FR jj/mm/aaaa
df['date_de_tirage'] = pd.to_datetime(df['date_de_tirage'], format='%d/%m/%Y')

# Dictionnaire de comptage
boules_counts = {i: 0 for i in range(1, 51)}
etoiles_counts = {i: 0 for i in range(1, 13)}

# Compter les occurrences de chaques boules et étoiles
for _, row in df.iterrows():
    for col in ['boule_1', 'boule_2', 'boule_3', 'boule_4', 'boule_5']:
        boules_counts[row[col]] += 1
    for col in ['etoile_1', 'etoile_2']:
        etoiles_counts[row[col]] += 1

# Calculer les probabilités
total_tirages = len(df)
boules_probs = {k: v / total_tirages for k, v in boules_counts.items()}
etoiles_probs = {k: v / total_tirages for k, v in etoiles_counts.items()}

# Convertir les dictionnaires de probabilités en DataFrames
boules_df = pd.DataFrame(list(boules_probs.items()), columns=["Boule", "Probabilité"])
etoiles_df = pd.DataFrame(list(etoiles_probs.items()), columns=["Étoile", "Probabilité"])

# Afficher les résultats
print("Probabilités des boules :")
print(boules_df)
print("\nProbabilités des étoiles :")
print(etoiles_df)

# Trier les boules et étoiles par leurs probabilités décroissantes
sorted_boules = sorted(boules_probs.items(), key=lambda x: x[1], reverse=True)
sorted_etoiles = sorted(etoiles_probs.items(), key=lambda x: x[1], reverse=True)

# Sélection des 5 premières boules et des 2 premières étoiles
top_5_boules = [b[0] for b in sorted_boules[:5]]
top_2_etoiles = [e[0] for e in sorted_etoiles[:2]]

# Calculer la prochaine date de tirage
latest_draw_date = df['date_de_tirage'].max()
existing_draw_dates = set(df['date_de_tirage'])

def date_previsionelle(current_date, existing_dates):
    next_date = current_date + timedelta(days=1)
    while next_date in existing_dates or next_date.weekday() not in [1, 4]:  # 1: Mardi, 4: Vendredi
        next_date += timedelta(days=1)
    return next_date

next_draw = date_previsionelle(latest_draw_date, existing_draw_dates)

# Extraire la combinaison la plus probable et la date du prochain tirage
print("Combinaison la plus probable:")
print(f"Boules: {top_5_boules}")
print(f"Étoiles: {top_2_etoiles}")
print(f"Prochaine date de tirage: {next_draw.strftime('%d/%m/%Y')}")