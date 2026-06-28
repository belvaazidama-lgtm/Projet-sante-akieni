
#============================================================ 
# MODULE FONDATEUR — Projet Sante Publique / Akieni Academy 
# Ce fichier centralise toutes les constantes et variables metier 
# Il sera enrichi chaque semaine jusqu'a S24 
# ============================================================ 
 
# === SECTION A : CONSTANTES NATIONALES ET NORMES OMS ======== 
TAUX_EUR_FCFA = 655.957 

TAUX_USD_FCFA = 600.0 
SEUIL_OMS_DENSITE_MEDICALE = 2.3    # medecins pour 1000 habitants 
SEUIL_OMS_COUVERTURE_VACCIN = 95.0  # pourcentage minimum OMS 
SEUIL_MORTALITE_ALERTE = 2.0        # % deces / hospitalisations 
SEUIL_RUPTURE_STOCK_JOURS = 30      # jours minimum de stock 
DEPARTEMENTS_CONGO = [              # 12 departements officiels 
    'Brazzaville', 'Pointe-Noire', 'Bouenza', 'Cuvette', 
    'Cuvette-Ouest', 'Kouilou', 'Lekoumou', 'Likouala', 
    'Niari', 'Plateaux', 'Pool', 'Sangha' 
] 
 
# === SECTION B : VARIABLES DES 5 HOPITAUX =================== 
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
 
# === SECTION C : VARIABLES DES 5 MEDICAMENTS ================ 
# TODO : Declarer les 5 medicaments essentiels 

medicament1 = "artemether-lumefatrine"
quantite_disponible_art = 1500
seuil_de_rupture_art = 100
cout_unitaire_art = 5000.00

medicament2 = "amoxiciline"
quantite_disponible_amoxi = 1650
seuil_de_rupture_amoxi = 200
cout_unitaire_amoxi = 1500.00

medicament3 = "paracetamol"
quantite_disponible_para = 1400
seuil_de_rupture_para = 100
cout_unitaire_para = 2000.00

medicament4 = "SRO"
quantite_disponible_SRO = 1700
seuil_de_rupture_SRO = 300
cout_unitaire_SRO = 1000.00

medicament5 = "vaccin antipaludeen"
quantite_disponible_vac = 2000
seuil_de_rupture_vac = 100
cout_unitaire_vac = 2000.00
 
# === SECTION D : CALCULS D'INITIALISATION =================== 
# TODO : Calculer les KPIs globaux initiaux 

nombre_total_medecins = h1_nb_medecins + h2_nb_medecins + h3_nb_medecins + h4_nb_medecins + h5_nb_medecins
population_total = h1_population_zone + h2_population_zone + h3_population_zone + h4_population_zone + h5_population_zone

densite_medical_nationale = nombre_total_medecins / population_total * 1000

taux_occupation_moyen = (taux_occupation_h1 + taux_occupation_h2 + taux_occupation_h3 + taux_occupation_h4 + taux_occupation_h5) / 5
val_tot_stock_med = (quantite_disponible_art * cout_unitaire_art) + (quantite_disponible_amoxi * cout_unitaire_amoxi) + (quantite_disponible_para * cout_unitaire_para) + (quantite_disponible_SRO * cout_unitaire_SRO) + (quantite_disponible_vac * cout_unitaire_vac)
 
print("===== KPI GLOBAUX INITIAUX =====")
print(f"Densité médicale nationale   : {densite_medical_nationale:.2f} médecins pour 10 000 habitants")
print(f"Taux d'occupation moyen      : {taux_occupation_moyen:.2f}%")
print(f"Valeur totale du stock       : {val_tot_stock_med:,.0f} FCFA")

# === SECTION E : RAPPORT D'INVENTAIRE ======================= 
# TODO : Afficher le rapport initial du systeme de sante 

print("\n" + "="*60)
print("       RAPPORT D'INVENTAIRE INITIAL")
print("="*60)

# Informations des hôpitaux
print("\n--- HÔPITAUX ---")
print(f"CHU Brazzaville              : {h1_nb_lits} lits, {h1_nb_lits_occupes} patients")
print(f"Hôpital Général Pointe-Noire : {h2_nb_lits} lits, {h2_nb_lits_occupes} patients")
print(f"Hôpital de Dolisie           : {h3_nb_lits} lits, {h3_nb_lits_occupes} patients")
print(f"Hôpital de district Owando   : {h4_nb_lits} lits, {h4_nb_lits_occupes} patients")
print(f"Centre de santé d'Impfondo   : {h5_nb_lits} lits, {h5_nb_lits_occupes} patients")

# Informations des médicaments
print("\n--- STOCK DES MÉDICAMENTS ---")
print(f"Artéméther-Luméfantrine      : {quantite_disponible_art} unités | "
      f"Seuil                        : {seuil_de_rupture_art} | "
      f"Prix unitaire                : {cout_unitaire_art} FCFA")

print(f"Amoxicilline                 : {quantite_disponible_amoxi} unités | "
      f"Seuil                        : {seuil_de_rupture_amoxi} | "
      f"Prix unitaire                : {cout_unitaire_amoxi} FCFA")

print(f"Paracétamol                  : {quantite_disponible_para} unités | "
      f"Seuil                        : {seuil_de_rupture_para} | "
      f"Prix unitaire                : {cout_unitaire_para} FCFA")

print(f"SRO                          : {quantite_disponible_SRO} unités | "
      f"Seuil                        : {seuil_de_rupture_SRO} | "
      f"Prix unitaire                : {cout_unitaire_SRO} FCFA")

print(f"Vaccin antipaludéen          : {quantite_disponible_vac} unités | "
      f"Seuil                        : {seuil_de_rupture_vac} | "
      f"Prix unitaire                : {cout_unitaire_vac} FCFA")

# Alertes de rupture
print("\n--- ALERTES DE STOCK ---")

if quantite_disponible_art <= seuil_de_rupture_art:
    print("⚠ Artéméther-Luméfantrine proche de la rupture")

if quantite_disponible_amoxi <= seuil_de_rupture_amoxi:
    print("⚠ Amoxicilline proche de la rupture")

if quantite_disponible_para <= seuil_de_rupture_para:
    print("⚠ Paracétamol proche de la rupture")

if quantite_disponible_SRO <= seuil_de_rupture_SRO:
    print("⚠ SRO proche de la rupture")

if quantite_disponible_vac <= seuil_de_rupture_vac:
    print("⚠ Vaccin antipaludéen proche de la rupture")

# KPI globaux
print("\n--- INDICATEURS NATIONAUX ---")
print(f"Densité médicale nationale   : {densite_medical_nationale:.2f} médecins pour 10 000 habitants")
print(f"Taux d'occupation moyen      : {taux_occupation_moyen:.2f}%")
print(f"Valeur totale du stock       : {val_tot_stock_med:,.0f} FCFA")

print("\n" + "="*60)

# === SECTION F : Classification statut stocks (NEW S3) ======
print("\n--- CLASSIFICATION STOCKS ---")

if quantite_disponible_art <= seuil_de_rupture_art:
    print("Artéméther-Luméfantrine : STOCK CRITIQUE")
elif quantite_disponible_art <= seuil_de_rupture_art * 2:
    print("Artéméther-Luméfantrine : STOCK FAIBLE")
else:
    print("Artéméther-Luméfantrine : STOCK NORMAL")

if quantite_disponible_amoxi <= seuil_de_rupture_amoxi:
    print("Amoxicilline : STOCK CRITIQUE")
elif quantite_disponible_amoxi <= seuil_de_rupture_amoxi * 2:
    print("Amoxicilline : STOCK FAIBLE")
else:
    print("Amoxicilline : STOCK NORMAL")

if quantite_disponible_para <= seuil_de_rupture_para:
    print("Paracétamol : STOCK CRITIQUE")
elif quantite_disponible_para <= seuil_de_rupture_para * 2:
    print("Paracétamol : STOCK FAIBLE")
else:
    print("Paracétamol : STOCK NORMAL")

if quantite_disponible_SRO <= seuil_de_rupture_SRO:
    print("SRO : STOCK CRITIQUE")
elif quantite_disponible_SRO <= seuil_de_rupture_SRO * 2:
    print("SRO : STOCK FAIBLE")
else:
    print("SRO : STOCK NORMAL")

if quantite_disponible_vac <= seuil_de_rupture_vac:
    print("Vaccin antipaludéen : STOCK CRITIQUE")
elif quantite_disponible_vac <= seuil_de_rupture_vac * 2:
    print("Vaccin antipaludéen : STOCK FAIBLE")
else:
    print("Vaccin antipaludéen : STOCK NORMAL")


# === SECTION G : Classification occupation hôpitaux (NEW S3) ===
print("\n--- CLASSIFICATION OCCUPATION HÔPITAUX ---")

if taux_occupation_h1 >= 90:
    print("CHU Brazzaville : SURCHARGE")
elif taux_occupation_h1 >= 75:
    print("CHU Brazzaville : TENSION")
else:
    print("CHU Brazzaville : NORMAL")

if taux_occupation_h2 >= 90:
    print("HG Pointe-Noire : SURCHARGE")
elif taux_occupation_h2 >= 75:
    print("HG Pointe-Noire : TENSION")
else:
    print(" HG Pointe-Noire : NORMAL")

if taux_occupation_h3 >= 90:
    print("Hôpital de Dolisie : SURCHARGE")
elif taux_occupation_h3 >= 75:
    print("Hôpital de Dolisie : TENSION")
else:
    print("Hôpital de Dolisie : NORMAL")

if taux_occupation_h4 >= 90:
    print("Hôpital Owando : SURCHARGE")
elif taux_occupation_h4 >= 75:
    print("Hôpital Owando : TENSION")
else:
    print("Hôpital Owando : NORMAL")

if taux_occupation_h5 >= 90:
    print("CS Impfondo : SURCHARGE")
elif taux_occupation_h5 >= 75:
    print("CS Impfondo : TENSION")
else:
    print("CS Impfondo : NORMAL")

# Exemple : calculer couverture vaccinale fictive
couverture_vaccinale_h1 = (1500000 / h1_population_zone) * 100
couverture_vaccinale_h2 = (1450000 / h2_population_zone) * 100
couverture_vaccinale_h3 = (880000 / h3_population_zone) * 100
couverture_vaccinale_h4 = (60000 / h4_population_zone) * 100
couverture_vaccinale_h5 = (930000 / h5_population_zone) * 100

# === SECTION H : Classification couverture vaccinale (NEW S3) ===
print("\n--- CLASSIFICATION COUVERTURE VACCINALE ---")

if couverture_vaccinale_h1 < 80:
    print("CHU Brazzaville : COUVERTURE INSUFFISANTE")
elif couverture_vaccinale_h1 < SEUIL_OMS_COUVERTURE_VACCIN:
    print("CHU Brazzaville : EN DESSOUS DU SEUIL OMS")
else:
    print("CHU Brazzaville : CONFORME OMS")

if couverture_vaccinale_h2 < 80:
    print("HG Pointe-Noire : COUVERTURE INSUFFISANTE")
elif couverture_vaccinale_h2 < SEUIL_OMS_COUVERTURE_VACCIN:
    print("HG Pointe-Noire : EN DESSOUS DU SEUIL OMS")
else:
    print("HG Pointe-Noire : CONFORME OMS")

if couverture_vaccinale_h3 < 80:
    print("Hôpital de Dolisie : COUVERTURE INSUFFISANTE")
elif couverture_vaccinale_h3 < SEUIL_OMS_COUVERTURE_VACCIN:
    print("Hôpital de Dolisie : EN DESSOUS DU SEUIL OMS")
else:
    print("Hôpital de Dolisie : CONFORME OMS")

if couverture_vaccinale_h4 < 80:
    print("Hôpital Owando : COUVERTURE INSUFFISANTE")
elif couverture_vaccinale_h4 < SEUIL_OMS_COUVERTURE_VACCIN:
    print("Hôpital Owando : EN DESSOUS DU SEUIL OMS")
else:
    print("Hôpital Owando : CONFORME OMS")

if couverture_vaccinale_h5 < 80:
    print("CS Impfondo : COUVERTURE INSUFFISANTE")
elif couverture_vaccinale_h5 < SEUIL_OMS_COUVERTURE_VACCIN:
    print("CS Impfondo : EN DESSOUS DU SEUIL OMS")
else:
    print("CS Impfondo : CONFORME OMS")


# === SECTION I : Rapport d'état global avec alertes (NEW S3) ===
print("\n" + "="*60)
print("       RAPPORT GLOBAL AVEC ALERTES")
print("="*60)

alertes_stock = 0
alertes_occupation = 0
alertes_vaccin = 0

# Comptage sans boucle
if quantite_disponible_art <= seuil_de_rupture_art:
    alertes_stock += 1
if quantite_disponible_amoxi <= seuil_de_rupture_amoxi:
    alertes_stock += 1
if quantite_disponible_para <= seuil_de_rupture_para:
    alertes_stock += 1
if quantite_disponible_SRO <= seuil_de_rupture_SRO:
    alertes_stock += 1
if quantite_disponible_vac <= seuil_de_rupture_vac:
    alertes_stock += 1

if taux_occupation_h1 >= 90:
    alertes_occupation += 1
if taux_occupation_h2 >= 90:
    alertes_occupation += 1
if taux_occupation_h3 >= 90:
    alertes_occupation += 1
if taux_occupation_h4 >= 90:
    alertes_occupation += 1
if taux_occupation_h5 >= 90:
    alertes_occupation += 1

if couverture_vaccinale_h1 < SEUIL_OMS_COUVERTURE_VACCIN:
    alertes_vaccin += 1
if couverture_vaccinale_h2 < SEUIL_OMS_COUVERTURE_VACCIN:
    alertes_vaccin += 1
if couverture_vaccinale_h3 < SEUIL_OMS_COUVERTURE_VACCIN:
    alertes_vaccin += 1
if couverture_vaccinale_h4 < SEUIL_OMS_COUVERTURE_VACCIN:
    alertes_vaccin += 1
if couverture_vaccinale_h5 < SEUIL_OMS_COUVERTURE_VACCIN:
    alertes_vaccin += 1

print(f"Alertes stock critique     : {alertes_stock}")
print(f"Hôpitaux en surcharge      : {alertes_occupation}")
print(f"Couverture vaccinale < OMS : {alertes_vaccin}")

print("\nÉtat global :")
if alertes_stock + alertes_occupation + alertes_vaccin == 0:
    print("Système de santé STABLE")
elif alertes_stock + alertes_occupation + alertes_vaccin <= 3:
    print("Système de santé sous TENSION")
else:
    print("Système de santé en CRISE")
print("="*60)
