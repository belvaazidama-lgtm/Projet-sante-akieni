# ==========================
# DONNEES DES HOPITAUX
# ==========================

# Hôpital District Kinkala
budget_trim_kinkala = 12500000
consultations_ext_kinkala = 1847
hospitalisations_kinkala = 312
deces_hospitaliers_kinkala = 8
lits_totaux_kinkala = 45
lits_occupes_kinkala = 41
medecins_permanents_kinkala = 3
population_desservie_kinkala = 85000

# CMS de Vindza
budget_trim_vindza = 6800000
consultations_ext_vindza = 923
hospitalisations_vindza = 87
deces_hospitaliers_vindza = 2
lits_totaux_vindza = 20
lits_occupes_vindza = 14
medecins_permanents_vindza = 1
population_desservie_vindza = 42000

# Hôpital de Kindamba
budget_trim_kindamba = 9200000
consultations_ext_kindamba = 1234
hospitalisations_kindamba = 201
deces_hospitaliers_kindamba = 11
lits_totaux_kindamba = 35
lits_occupes_kindamba = 33
medecins_permanents_kindamba = 2
population_desservie_kindamba = 67000


# ==========================
# CALCUL DES KPI
# ==========================

# Kinkala
cout_kinkala = budget_trim_kinkala / consultations_ext_kinkala
occupation_kinkala = (lits_occupes_kinkala / lits_totaux_kinkala) * 100
densite_kinkala = (medecins_permanents_kinkala / population_desservie_kinkala) * 10000
mortalite_kinkala = (deces_hospitaliers_kinkala / hospitalisations_kinkala) * 100

# Vindza
cout_vindza = budget_trim_vindza / consultations_ext_vindza
occupation_vindza = (lits_occupes_vindza / lits_totaux_vindza) * 100
densite_vindza = (medecins_permanents_vindza / population_desservie_vindza) * 10000
mortalite_vindza = (deces_hospitaliers_vindza / hospitalisations_vindza) * 100

# Kindamba
cout_kindamba = budget_trim_kindamba / consultations_ext_kindamba
occupation_kindamba = (lits_occupes_kindamba / lits_totaux_kindamba) * 100
densite_kindamba = (medecins_permanents_kindamba / population_desservie_kindamba) * 10000
mortalite_kindamba = (deces_hospitaliers_kindamba / hospitalisations_kindamba) * 100


# ==========================
# IDENTIFICATION DES HOPITAUX CRITIQUES
# ==========================

critique_kinkala = mortalite_kinkala > 2 or densite_kinkala < 0.05
critique_vindza = mortalite_vindza > 2 or densite_vindza < 0.05
critique_kindamba = mortalite_kindamba > 2 or densite_kindamba < 0.05


# ==========================
# RAPPORT CONSOLIDE
# ==========================

print("=" * 60)
print("RAPPORT SANITAIRE DU DEPARTEMENT DU POOL")
print("=" * 60)

print("\nHôpital District Kinkala")
print("-" * 30)
print(f"Coût moyen par patient       : {cout_kinkala:.2f} FCFA")
print(f"Taux d'occupation            : {occupation_kinkala:.2f}%")
print(f"Densité médicale             : {densite_kinkala:.2f} médecins pour 10 000 habitants")
print(f"Taux de mortalité            : {mortalite_kinkala:.2f}%")
if critique_kinkala:
    print("ALERTE                    : établissement en situation critique.")

print("\nCMS de Vindza")
print("-" * 30)
print(f"Coût moyen par patient       : {cout_vindza:.2f} FCFA")
print(f"Taux d'occupation            : {occupation_vindza:.2f}%")
print(f"Densité médicale             : {densite_vindza:.2f} médecins pour 10 000 habitants")
print(f"Taux de mortalité            : {mortalite_vindza:.2f}%")
if critique_vindza:
    print("ALERTE : établissement en situation critique.")

print("\nHôpital de Kindamba")
print("-" * 30)
print(f"Coût moyen par patient       : {cout_kindamba:.2f} FCFA")
print(f"Taux d'occupation            : {occupation_kindamba:.2f}%")
print(f"Densité médicale             : {densite_kindamba:.2f} médecins pour 10 000 habitants")
print(f"Taux de mortalité            : {mortalite_kindamba:.2f}%")
if critique_kindamba:
    print("ALERTE : établissement en situation critique.")

print("\n" + "=" * 60)


# ==========================
# CHALLENGE BONUS
# ==========================

budget_total = budget_trim_kinkala + budget_trim_vindza + budget_trim_kindamba

medecins_actuels = (
    medecins_permanents_kinkala +
    medecins_permanents_vindza +
    medecins_permanents_kindamba
)

medecins_requis = 5 * 3
medecins_supplementaires = medecins_requis - medecins_actuels

cout_medecin = 1200000
cout_recrutement = medecins_supplementaires * cout_medecin

print("\nCHALLENGE BONUS")
print("-" * 30)

if budget_total >= cout_recrutement:
    print("Le budget est suffisant pour atteindre 5 médecins par hôpital.")
    print(f"Médecins à recruter      : {medecins_supplementaires}")
    print(f"Coût du recrutement      : {cout_recrutement:,} FCFA")
    print(f"Budget total disponible  : {budget_total:,} FCFA")
else:
    manque = cout_recrutement - budget_total
    print("Le budget est insuffisant.")
    print(f"Montant manquant         : {manque:,} FCFA")
  