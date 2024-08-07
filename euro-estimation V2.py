import pandas as pd

# Lire le fichier CSV
df = pd.read_csv('euromillions_202002.csv', delimiter=';')

# Initialiser les dictionnaires de comptage
boules_counts = {i: 0 for i in range(1, 51)}
etoiles_counts = {i: 0 for i in range(1, 13)}

# Compter les occurrences de chaque boule et étoile
for _, row in df.iterrows():
    for col in ['boule_1', 'boule_2', 'boule_3', 'boule_4', 'boule_5']:
        boules_counts[row[col]] += 1
    for col in ['etoile_1', 'etoile_2']:
        etoiles_counts[row[col]] += 1

# Calculer les probabilités
total_tirages = len(df)
boules_probs = {k: v / total_tirages for k, v in boules_counts.items()}
etoiles_probs = {k: v / total_tirages for k, v in etoiles_counts.items()}

# Convertir les dictionnaires de probabilités en DataFrames (Merci  pour cette partie Monsieur G.P.T)
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

# Sélectionner les 5 premières boules et les 2 premières étoiles
top_5_boules = [b[0] for b in sorted_boules[:5]]
top_2_etoiles = [e[0] for e in sorted_etoiles[:2]]

# Afficher la combinaison la plus probable
print("Combinaison la plus probable:")
print(f"Boules: {top_5_boules}")
print(f"Étoiles: {top_2_etoiles}")