import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# IMPORT DES DONNÉES

df = pd.read_excel("Temperatures_Paris_2000 et 2026.xlsx")

df["YEAR"] = df["YEAR"].astype(int)
df["DOY"] = df["DOY"].astype(int)
df["T2M_MAX"] = df["T2M_MAX"].astype(float)


# CRÉATION DES DATES

df["Date"] = (pd.to_datetime(df["YEAR"], format="%Y")+ pd.to_timedelta(df["DOY"]-1, unit="D"))

df["Mois"] = df["Date"].dt.month


# ÉTÉ UNIQUEMENT

ete = df[df["Mois"].isin([6,7,8])].copy()


# CONSTRUCTION DU HEAT INDEX

SEUIL = 35

ete["Contribution"] = np.maximum(ete["T2M_MAX"]-SEUIL,0)

heat_index = (ete.groupby("YEAR")["Contribution"].sum().reset_index())

print(heat_index)



# BOOTSTRAP

N = 10000

HI_simules = np.random.choice(heat_index["Contribution"],size=N,replace=True)

# Paramètres financiers
r = 0.02
T = 1


# VALORISATION

# Strike = 95e percentile
strike_reference = np.percentile(heat_index["Contribution"], 95)

print("Strike :", round(strike_reference, 2))

payoff = np.maximum(HI_simules - strike_reference, 0)

prime = np.exp(-r*T) * payoff.mean()


print("Prime :", round(prime,2),"€")

print("50% :", np.percentile(heat_index["Contribution"],50))
print("75% :", np.percentile(heat_index["Contribution"],75))
print("90% :", np.percentile(heat_index["Contribution"],90))
print("95% :", np.percentile(heat_index["Contribution"],95))
print("99% :", np.percentile(heat_index["Contribution"],99))



# PROBABILITÉ D'EXERCICE

proba = np.mean(HI_simules > strike_reference)

print("Probabilité d'exercice :",round(proba*100,2),"%")



# Analyse de sensibilité

strikes = np.arange(20, 61, 5)

primes = []

for strike in strikes:

    payoff = np.maximum(HI_simules - strike, 0)

    prime = np.exp(-r*T) * payoff.mean()

    primes.append(prime)


# GRAPHIQUES

plt.figure(figsize=(10,5))

plt.bar(heat_index["YEAR"],heat_index["Contribution"],color="steelblue")

plt.xlabel("Année")

plt.ylabel("Heat Index")

plt.title("Heat Index estival (2000-2026)")

plt.show()

plt.figure(figsize=(8,5))

plt.hist(HI_simules,bins=30)

plt.xlabel("Heat Index simulé")

plt.ylabel("Fréquence")

plt.title("Distribution des scénarios simulés")

plt.show()

plt.figure(figsize=(8,5))

plt.plot(strikes,primes,marker="o")

plt.xlabel("Strike")

plt.ylabel("Prime")

plt.title("Influence du strike sur la prime de la CPO")

plt.grid()

plt.show()

plt.figure(figsize=(8,5))

plt.hist(heat_index["Contribution"], bins=10)

plt.axvline(
    strike_reference,
    color="red",
    linestyle="--",
    linewidth=2.5,
    label=f"Strike (95e percentile) = {strike_reference:.2f}"
)

plt.xlabel("Heat Index")
plt.ylabel("Nombre d'étés")
plt.title("Distribution historique du Heat Index")

plt.legend()

plt.show()
