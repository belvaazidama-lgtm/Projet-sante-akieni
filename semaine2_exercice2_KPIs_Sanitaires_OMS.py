# ============================================================ 
# AKIENI ACADEMY — Projet Sante Publique 
# Semaine 2 — Exercice 2 : KPIs Sanitaires OMS 
# ============================================================ 
 
# --- DONNEES BRUTES --- 
budget_fcfa          = 87_450_000   # underscore pour lisibilite des grands nombres 
nb_consultations_ext = 4823 
nb_hospitalisations  = 1247 
nb_deces             = 18 
nb_lits_total        = 180 
nb_lits_occupes      = 143 
nb_medecins          = 22 
nb_infirmiers        = 58 
population_dept      = 128_000 
taux_eur_fcfa        = 655.957 
taux_usd_fcfa        = 600.0 
 
# --- A COMPLETER --- 
# 1. Conversions devises 
budget_eur = budget_fcfa / 655.957
budget_usd = budget_fcfa / 600.0
 
# 2. Indicateurs OMS 
densite_medicale     = (nb_medecins / population_dept) * 1000
taux_mortalite       = (nb_deces / nb_hospitalisations) * 100 
taux_occupation      = (nb_lits_occupes / nb_lits_total) * 100
 
# 3. Division entiere et modulo 
budget_medicaments   = (budget_fcfa * 0.35) 
cout_journalier_meds = 450_000 
jours_stock          = (budget_medicaments // cout_journalier_meds)   # division entiere // 
jours_restants       = budget_medicaments % cout_journalier_meds # modulo % 
 
# 4. Puissance pour projection 
budget_n_plus_2      = budget_fcfa * (1.08 ** 2)    # ** pour la puissance 
 
# --- AFFICHAGE RAPPORT --- 
print(f'=== RAPPORT TRIMESTRIEL Q4 2025 - Hopital General Pointe-Noire ===') 
print("BUDGET")
print("  Depenses Q4       :", f'{budget_fcfa:_}', "FCFA")
print("  En euros          : ",f'{round(budget_eur):_}', "EUR ")
print("  En dollars        : ",f'{budget_usd:_}', "USD" )
print("INDICATEURS OMS ")
print("  Densite medicale  :",f'{densite_medicale:.1f}'" medecins / 1000 hab [Norme OMS : >= 2.3] ")
print("  Taux mortalite    : ",f'{taux_mortalite:.1f}'"%                     [Seuil alerte : > 2%] ")
print("  Taux occupation   : ",f'{taux_occupation:.1f}'"%                    [Optimal : 70-85%] ")
print("ANALYSE PHARMACIE ")
print("  Budget medicaments: ", f'{round(budget_medicaments):_}', "FCFA")
print("  Jours de stock    : ", jours_stock, "jours")
print("  Jours depassement : ", jours_restants, "jours")
print("PROJECTION ")
print("  Budget N+2 (8%/an): ", f'{round (budget_n_plus_2):_}' )
print("ALERTE : Densite medicale CRITIQUE (0.2 pour 1000 hab — norme OMS : 2.3)")
