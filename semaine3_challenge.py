# Hopital 1 — CHU de Brazzaville 
h1_nom              = 'CHU de Brazzaville' 
h1_ville            = 'Brazzaville' 
h1_departement      = 'Brazzaville' 
h1_type             = 'CHU' 
h1_nb_lits          = 320 
h1_nb_lits_occupes  = 284 
h1_nb_medecins      = 47 
h1_nb_infirmiers    = 123 
h1_population_zone  = 1_800_000 
taux_occupation_h1 = (h1_nb_lits_occupes / h1_nb_lits) * 100
nb_meds_rupture_h1 = 2
nb_alertes_h1 = 2

# Hopital 2 — HG POINTE NOIR

h2_nom              = 'HG de Pointe-Noire' 
h2_ville            = 'pointe-Noire' 
h2_departement      = 'Pointe-Noire' 
h2_type             = 'HG' 
h2_nb_lits          = 310 
h2_nb_lits_occupes  = 204 
h2_nb_medecins      = 50 
h2_nb_infirmiers    = 120
h2_population_zone  = 1_500_000 
taux_occupation_h2 = (h2_nb_lits_occupes / h2_nb_lits) * 100
nb_meds_rupture_h2 = 0
nb_alertes_h2 = 1

# Hopital 3 — Hopital de Dolisie

h3_nom              = 'Hopital de Dolisie' 
h3_ville            = 'Niari' 
h3_departement      = 'Niari' 
h3_type             = 'HG' 
h3_nb_lits          = 220 
h3_nb_lits_occupes  = 174 
h3_nb_medecins      = 38 
h3_nb_infirmiers    = 95 
h3_population_zone  = 1_000_000 
taux_occupation_h3 = (h3_nb_lits_occupes / h3_nb_lits) * 100
nb_meds_rupture_h3 = 1
nb_alertes_h3 = 2

# Hopital 4 — Hopital de district Owando

h4_nom              = 'Hopital de district Owando' 
h4_ville            = 'Cuvette' 
h4_departement      = 'Cuvette' 
h4_type             = 'HG' 
h4_nb_lits          = 520 
h4_nb_lits_occupes  = 250
h4_nb_medecins      = 48 
h4_nb_infirmiers    = 150
h4_population_zone  = 64_358
taux_occupation_h4 = (h4_nb_lits_occupes / h4_nb_lits) * 100
nb_meds_rupture_h4 = 3
nb_alertes_h4 = 0

# Hopital 5 — CS de Impfondo

h5_nom              = 'CS de Impfondo' 
h5_ville            = 'Niari' 
h5_departement      = 'Niari' 
h5_type             = 'CS' 
h5_nb_lits          = 220 
h5_nb_lits_occupes  = 174 
h5_nb_medecins      = 38 
h5_nb_infirmiers    = 95 
h5_population_zone  = 1_000_000
taux_occupation_h5 = (h5_nb_lits_occupes / h5_nb_lits) * 100
nb_meds_rupture_h5 = 2
nb_alertes_h5 = 1


print("=" * 75)
print("TABLEAU DE BORD SANITAIRE - MINISTERE DE LA SANTE")
print("Date : 16 janvier 2026  |  Pour le Conseil des Ministres")
print("=" * 75)

nombre_critiques = 0
ruptures_nationales = 0

    # Niveau triage occupation h1
if taux_occupation_h1 >= 95:
    triage = "CRI"
elif taux_occupation_h1 >= 85:
    triage = "ALT"
else:
    triage = "OK"
        # Niveau d'alerte global h1
if nb_meds_rupture_h1 >= 2 or taux_occupation_h1 >= 95:
    niveau_global_h1 = "CRITIQUE"
    nombre_critiques += 1

elif (nb_alertes_h1 >= 1 or
        taux_occupation_h1 >= 85 or
        (nb_alertes_h1 >= 2 and h1_nb_medecins < 5)):
    niveau_global_1 = "PREOCCUPANT"

else:
    niveau_global_h1 = "SATISFAISANT"

    ruptures_nationales += nb_meds_rupture_h1
    
 # Niveau triage occupation h2
    if taux_occupation_h2 >= 95:
        triage = "CRI"
    elif taux_occupation_h2 >= 85:
        triage = "ALT"
    else:
        triage = "OK"
    # Niveau d'alerte global h2
if nb_meds_rupture_h2 >= 2 or taux_occupation_h2 >= 95:
    niveau_global_h2 = "CRITIQUE"
    nombre_critiques += 1

elif (nb_meds_rupture_h2 >= 1 or
        taux_occupation_h2 >= 85 or
        (nb_alertes_h2>= 2 and h2_nb_medecins < 5)):
    niveau_global_h2 = "PREOCCUPANT"

else:
    niveau_global_h2 = "SATISFAISANT"

    ruptures_nationales += nb_meds_rupture_h2

 # Niveau triage occupation h3
    if taux_occupation_h3 >= 95:
        triage = "CRI"
    elif taux_occupation_h3 >= 85:
        triage = "ALT"
    else:
        triage = "OK"
    # Niveau d'alerte global h3
if nb_meds_rupture_h3 >= 2 or taux_occupation_h3 >= 95:
    niveau_global_h3 = "CRITIQUE"
    nombre_critiques += 1

elif (nb_meds_rupture_h3 >= 1 or
        taux_occupation_h3 >= 85 or
        (nb_alertes_h3 >= 2 and h3_nb_medecins < 5)):
    niveau_global_h3 = "PREOCCUPANT"

else:
    niveau_global_h3 = "SATISFAISANT"

    ruptures_nationales += nb_meds_rupture_h3

 # Niveau triage occupation h4
    if taux_occupation_h4 >= 95:
        triage = "CRI"
    elif taux_occupation_h4 >= 85:
        triage = "ALT"
    else:
        triage = "OK"
    # Niveau d'alerte global h3
if nb_meds_rupture_h4 >= 2 or taux_occupation_h4 >= 95:
    niveau_global_h4 = "CRITIQUE"
    nombre_critiques += 1

elif (nb_meds_rupture_h4 >= 1 or
        taux_occupation_h4 >= 85 or
        (nb_alertes_h4 >= 2 and h4_nb_medecins < 5)):
    niveau_global_h4 = "PREOCCUPANT"

else:
    niveau_global_h4 = "SATISFAISANT"

    ruptures_nationales += nb_meds_rupture_h4
        
 # Niveau triage occupation h5
    if taux_occupation_h5 >= 95:
        triage = "CRI"
    elif taux_occupation_h5 >= 85:
        triage = "ALT"
    else:
        triage = "OK" 
    # Niveau d'alerte global h5
if nb_meds_rupture_h5 >= 2 or taux_occupation_h5 >= 95:
    niveau_global_h5 = "CRITIQUE"
    nombre_critiques += 1

elif (nb_meds_rupture_h5 >= 1 or
        taux_occupation_h5 >= 85 or
        (nb_alertes_h5 >= 2 and h5_nb_medecins < 5)):
    niveau_global_h5 = "PREOCCUPANT"

else:
    niveau_global_h5 = "SATISFAISANT"

    ruptures_nationales += nb_meds_rupture_h5    

print(f"{'HOPITAL':<28} {'OCCUPATION':<12} {'ALERTES':<9} {'NIVEAU GLOBAL'}")    

print(
    f"{h1_nom:<25}"
    f"{taux_occupation_h1:>8.1f}% "
    f"[{triage}]   "
    f"{nb_meds_rupture_h1}R + "
    f"{nb_alertes_h1}A   "
    f"[{niveau_global_h1}]"
)

print(
    f"{h2_nom:<25}"
    f"{taux_occupation_h2:>8.1f}% "
    f"[{triage}]   "
    f"{nb_meds_rupture_h2}R + "
    f"{nb_alertes_h2}A   "
    f"[{niveau_global_h2}]"
)

print(
    f"{h3_nom:<25}"
    f"{taux_occupation_h3:>8.1f}% "
    f"[{triage}]   "
    f"{nb_meds_rupture_h3}R + "
    f"{nb_alertes_h3}A   "
    f"[{niveau_global_h3}]"
)

print(
    f"{h4_nom:<25}"
    f"{taux_occupation_h4:>8.1f}% "
    f"[{triage}]   "
    f"{nb_meds_rupture_h4}R + "
    f"{nb_alertes_h4}A   "
    f"[{niveau_global_h4}]"
)

print(
    f"{h5_nom:<25}"
    f"{taux_occupation_h5:>8.1f}% "
    f"[{triage}]   "
    f"{nb_meds_rupture_h5}R + "
    f"{nb_alertes_h5}A   "
    f"[{niveau_global_h5}]"
)

print("-" * 75)

print(f"{nombre_critiques} hôpitaux sur 5 sont en situation CRITIQUE")

print(
    f"{ruptures_nationales} ruptures de stock "
    f"identifiées à l'échelle nationale"
)


# RECOMMANDATION PRIORITAIRE


if nombre_critiques >= 3:
    recommandation = "Mobiliser la réserve nationale PNA"

elif ruptures_nationales >= 5:
    recommandation = "Lancer une commande urgente de médicaments"

else:
    recommandation = "Maintenir la surveillance hebdomadaire"

print(f"RECOMMANDATION PRIORITAIRE : {recommandation}")


# BONUS


cout_commande_express = 450000
cout_total_commandes = ruptures_nationales * cout_commande_express

print("\n===== BONUS =====")
print(f"Nombre total de ruptures : {ruptures_nationales}")
print(
    f"Coût estimé des commandes urgentes : "
    f"{cout_total_commandes:,} FCFA"
)
